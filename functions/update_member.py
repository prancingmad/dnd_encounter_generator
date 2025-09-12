import tkinter as tk
import os
import json
from .show_error import show_error
from .player import *

def update_member(root, left_frame=None, right_frame=None):
    popup = tk.Toplevel(root)
    popup.title("Update Party Member")

    instr_label = tk.Label(popup, text="Which character would you like to update, and what?\nIf adding a multiclass, you can input that here under the Character Class and Level.")
    instr_label.pack(pady=10)

    result = {"data": None}

    def on_submit():
        name_val = name_entry.get()
        ac_val = ac_entry.get()
        magic_items_val = items_entry.get()
        class_val = class_entry.get()
        level_val = level_entry.get()

        class_val_input = class_val.lower()
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

        if class_val_input not in valid_map:
            show_error(f"Invalid class. Must be one of: {', '.join(VALID_CLASSES)} (Not case sensitive).", root)
            return

        class_obj = valid_map[class_val_input]

        players_list = []
        if os.path.exists(PARTY_FILE_PATH):
            with open(PARTY_FILE_PATH, "r") as f:
                content = f.read().strip()
                if content:
                    players_list = json.loads(content)

        if players_list == []:
            show_error("No players found, add players first!", root)
            return

        for player in players_list:
            if player["name"] == name_val:
                player_update = Player(name_val, player["armor_class"], player["magic_items"])
                players_list.remove(player)
                if ac_val:
                    player_update["armor_class"] = ac_val
                if magic_items_val:
                    player_update["magic_items"] = magic_items_val
                if class_val:
                    for cls in player["classes"]:
                        if cls["name"] == class_val:
                            cls["level"] = level_val
                        else:
                            player["classes"].append[{"name": class_val, "level": level_value}]

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