import tkinter as tk
import os
import json
from .show_error import show_error
from .config import (PARTY_FILE_PATH, VALID_CLASSES, ARTI_MOD, BARB_MOD, BARD_MOD, CLER_MOD, DRUI_MOD, FIGH_MOD, MONK_MOD, PALA_MOD, RANG_MOD, ROGU_MOD, SORC_MOD, WARL_MOD, WIZA_MOD)
from .player import Player
from .character_classes import (Artificer, Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard)

def update_member(root, left_frame=None, right_frame=None):
    popup = tk.Toplevel(root)
    popup.title("Update Party Member")

    instr_label = tk.Label(popup, text="Which character would you like to update, and what?\nIf adding a multiclass, you can input that here under the Character Class and Level.\nIf a section does not need to be updated, it can be left blank!")
    instr_label.pack(pady=10)

    result = {"data": None}

    def on_submit():
        name_val = name_entry.get().strip().title()
        ac_val = ac_entry.get()
        magic_items_val = items_entry.get()
        class_val = class_entry.get().strip().title()
        level_val = level_entry.get()

        valid_map = {
            "artificer": Artificer,
            "barbarian": Barbarian,
            "bard": Bard,
            "cleric": Cleric,
            "druid": Druid,
            "fighter": Fighter,
            "monk": Monk,
            "paladin": Paladin,
            "ranger": Ranger,
            "rogue": Rogue,
            "sorcerer": Sorcerer,
            "warlock": Warlock,
            "wizard": Wizard,
        }

        if class_val:
            class_val_input = class_val.lower()
            if class_val_input not in valid_map:
                show_error(f"Invalid class. Must be one of: {', '.join(VALID_CLASSES)} (Not case sensitive).", root)
                return
            class_obj = valid_map[class_val_input]
        else:
            class_obj = None

        players_list = []
        if os.path.exists(PARTY_FILE_PATH):
            with open(PARTY_FILE_PATH, "r") as f:
                content = f.read().strip()
                if content:
                    players_list = json.loads(content)

        found = False
        for player in players_list:
            if player["name"].lower() == name_val.lower():
                found = True
                player_update = Player(name_val, player["armor_class"], player["magic_items"])
                for cls in player["classes"]:
                    class_type = valid_map[cls["name"].lower()]
                    player_update.add_class(class_type, cls["level"])
                if ac_val:
                    try:
                        player_update.armor_class = int(ac_val)
                    except ValueError:
                        show_error("Armor Class must be a number.", root)
                        return
                if magic_items_val:
                    try:
                        player_update.magic_items = int(magic_items_val)
                    except ValueError:
                        show_error("Magic Items must be a number.", root)
                        return
                if (class_val and not level_val) or (level_val and not class_val):
                    show_error("If updating Class, both Class and Level must be provided.", root)
                    return
                if class_val and level_val:
                    existing_classes = [cls.name.lower() for cls in player_update.classes]
                    class_val_lower = class_val.lower()
                    if class_val_lower in existing_classes:
                        player_update.update_class_level(class_val, int(level_val))
                    else:
                        player_update.add_class(class_obj, int(level_val))

                players_list.remove(player)

                players_list.append(player_update.to_dict())

                with open(PARTY_FILE_PATH, "w") as f:
                    json.dump(players_list, f, indent=4)

                popup.destroy()

                if left_frame and right_frame:
                    from .gui_functions import manage_party_page
                    manage_party_page(root, left_frame, right_frame)
                break

        if not found:
            show_error(f"No player named '{name_val}' found in party.", root)
            return

    def on_cancel():
        result["data"] = None
        popup.destroy()

    name_label = tk.Label(popup, text="Name:")
    name_label.pack()
    name_entry = tk.Entry(popup)
    name_entry.pack()
    name_entry.focus_set()
    ac_label = tk.Label(popup, text="Armor Class:")
    ac_label.pack()
    ac_entry = tk.Entry(popup)
    ac_entry.pack()
    items_label = tk.Label(popup, text="Combat Magic Item Count:")
    items_label.pack()
    items_entry = tk.Entry(popup)
    items_entry.pack()
    class_label = tk.Label(popup, text="Character Class:")
    class_label.pack()
    class_entry = tk.Entry(popup)
    class_entry.pack()
    level_label = tk.Label(popup, text="Class Level:")
    level_label.pack()
    level_entry = tk.Entry(popup)
    level_entry.pack()
    submit_btn = tk.Button(popup, text="Submit", command=on_submit)
    submit_btn.pack(pady=10)
    cancel_btn = tk.Button(popup, text="Cancel", command=on_cancel)
    cancel_btn.pack(pady=10)