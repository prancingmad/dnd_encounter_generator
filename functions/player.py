from .config import *
from .character_classes import BaseClass
import json
import os

class Player():
    def __init__(self, name, armor_class, magic_items):
        self.name = name
        self.armor_class = armor_class
        self.magic_items = magic_items
        self.classes = []

    def add_class(self, class_obj, level):
        for cls in self.classes:
            if cls.name == class_obj.__name__:
                raise Exception("Duplicate class name")
        self.classes.append(class_obj(level))

    def update_class_level(self, class_name, level):
        for cls in self.classes:
            if cls.name == class_name:
                cls.level = level
                break
        else:
            raise ValueError(f"{self.name} does not have {class_name}.")
        

    def get_combat_value(self):
        combat_value = 0
        armor_value = max(0, 0.01 * (self.armor_class - 10))
        barb_level = sum(cls.level for cls in self.classes if cls.name == "Barbarian")
        figh_level = sum(cls.level for cls in self.classes if cls.name == "Fighter")
        monk_level = sum(cls.level for cls in self.classes if cls.name == "Monk")
        pala_level = sum(cls.level for cls in self.classes if cls.name == "Paladin")
        rang_level = sum(cls.level for cls in self.classes if cls.name == "Ranger")
        for cls in self.classes:
            combat_value += cls.get_combat_value()
        if barb_level >= 5 or figh_level >= 5 or monk_level >= 5 or pala_level >= 5 or rang_level >= 5:
            combat_value += EXTRA_ATTACK_MOD
        if barb_level >= 2:
            combat_value += RECKLESS_MOD
        if pala_level >= 2:
            combat_value += SMITE_MOD
        if figh_level >= 2:
            combat_value += SURGE_MOD
        if monk_level >= 5:
            combat_value += STUN_STRIKE_MOD
        return combat_value + armor_value + (self.magic_items * 0.1)

    def to_dict(self):
        player_dict = {}
        classes_list = []
        player_dict["name"] = self.name
        player_dict["armor_class"] = self.armor_class
        player_dict["magic_items"] = self.magic_items
        player_dict["combat_value"] = self.get_combat_value()
        for cls in self.classes:
            classes_list.append({"name": cls.name, "level": cls.level})
        player_dict["classes"] = classes_list
        return player_dict

    def save_to_file(self):
        players_list = []
        if os.path.exists(PARTY_FILE_PATH):
            with open(PARTY_FILE_PATH, "r") as f:
                content = f.read().strip()
                if content:
                    players_list = json.loads(content)
        player_dict = self.to_dict()
        players_list.append(player_dict)
        with open(PARTY_FILE_PATH, "w") as f:
            json.dump(players_list, f, indent=4)