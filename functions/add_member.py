from .show_error import show_error
import tkinter as tk
import os
import json
from .config import *

def add_member(root, left_frame=None, right_frame=None):
    popup = tk.Toplevel(root)
    popup.title("Add New Party Member")

    result = {"data": None}

    instr_label = tk.Label(popup, text="Please enter the character's details.\nIf the character is multi-classed, put one\nand then use Update Member to add other classes.")
    instr_label.pack(pady=10)

    def on_submit():
        name_val = name_entry.get()
        ac_val = ac_entry.get()
        magic_items_val = items_entry.get()
        class_val = class_entry.get()
        level_val = level_entry.get()

        for key, value in [("Name", name_val), ("Armor Class", ac_val), ("Magic Items", magic_items_val), ("Class", class_val), ("Level", level_val)]:
            if value.strip() == "":
                show_error("Missing a Value.", root)
                return

        ac_val = int(ac_val)
        magic_items_val = int(magic_items_val)
        level_val = int(level_val)

        result["data"] = {
            "name": name_val,
            "armor_class": ac_val,
            "magic_items": magic_items_val,
            "classes": [{"name": class_val, "level": level_val}]
        }

        if os.path.exists(PARTY_FILE_PATH):
            with open(PARTY_FILE_PATH, "r") as f:
                content = f.read().strip()
                if content:
                    players_list = json.loads(content)
                else:
                    players_list = []
            for player in players_list:
                if player["name"] == name_val:
                    show_error("Player already exists in party.", root)
                    return
        players_list.append(result["data"])
        with open(PARTY_FILE_PATH, "w") as f:
            json.dump(players_list, f, indent=4)
            popup.destroy()

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

    popup.grab_set()
    root.wait_window(popup)
    return result["data"]