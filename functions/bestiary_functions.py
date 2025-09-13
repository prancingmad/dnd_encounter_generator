import json
import tkinter as tk
import os
from .gui_functions import clear_widgets, create_scrollable_frame, on_button_click
from .show_error import show_error
from .config import ARCHIVE_FILE_PATH, ARCHIVE_BUTTON_LABELS, BUTTON_PACK_OPTIONS

bestiary_flag = "archive"

class Monster():
    def __init__(self, name, challenge_rating):
        self.name = name
        self.challenge_rating = challenge_rating

    def to_dict(self):
        enemy_dict = {}
        enemy_dict["name"] = self.name
        enemy_dict["challenge_rating"] = self.challenge_rating
        return enemy_dict

    def save_to_file(self):
        global bestiary_flag
        if bestiary_flag == "archive":
            file_path = ARCHIVE_FILE_PATH
        else:
            return

        monster_list = []
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                content = f.read().strip()
                if content:
                    monster_list = json.loads(content)

        monster_list.append(self.to_dict())

        with open(file_path, "w") as f:
            json.dump(monster_list, f, indent=4)

def archive_page(root, left_frame, right_frame):
    clear_widgets(left_frame)
    clear_widgets(right_frame)
    global bestiary_flag
    bestiary_flag = "archive"

    scroll_frame = create_scrollable_frame(left_frame)
    with open(ARCHIVE_FILE_PATH, "r") as f:
        content = f.read().strip()
        if content:
            f.seek(0)
            archive_data = json.load(f)

            for creature in archive_data:
                creature_text = f"{creature['name']} - Challenge Rating: {creature['challenge_rating']}"
                label = tk.Label(scroll_frame, text=creature_text, anchor="w", justify="left")
                label.pack(fill="x", pady=2)
        else:
            placeholder_label = tk.Label(left_frame, text="", anchor="nw", justify="left")
            placeholder_label.pack(fill=tk.BOTH, expand=True)

    button_frame = tk.Frame(right_frame)
    button_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    for label in ARCHIVE_BUTTON_LABELS:
        btn = tk.Button(button_frame, text=label, command=lambda l=label: on_button_click(l, root, left_frame, right_frame))
        btn.pack(**BUTTON_PACK_OPTIONS)

def add_monster(root, left_frame=None, right_frame=None):
    global bestiary_flag
    if bestiary_flag == "archive":
        add_monster_flag = ARCHIVE_FILE_PATH

    popup = tk.Toplevel(root)
    popup.title(f"Add New Monster to {bestiary_flag}")

    result = {"data": None}

    instr_label = tk.Label(popup, text="Adding a monster.\nFor Challenge Rating, please put either an integer or a decimal.\n(0.25 instead of 1/4)")
    instr_label.pack(pady=10)

    def on_submit():
        name_val = name_entry.get().strip().title()
        cr_val = cr_entry.get()

        for key, value in [("Name", name_val), ("Challenge Rating", cr_val)]:
            if value.strip() == "":
                show_error("Missing a Value.", root)
                return

        monster_list = []
        if os.path.exists(add_monster_flag):
            with open(add_monster_flag, "r") as f:
                content = f.read().strip()
                if content:
                    monster_list = json.loads(content)

        for mon in monster_list:
            if mon["name"] == name_val:
                show_error(f"Monster already exists in {bestiary_flag}", root)
                return

        new_monster = Monster(name_val, cr_val)
        new_monster.save_to_file()

        popup.destroy()

        if left_frame and right_frame:
            archive_page(root, left_frame, right_frame)

    def on_cancel():
        result["data"] = None
        popup.destroy()

    name_label = tk.Label(popup, text="Name:")
    name_label.pack()
    name_entry = tk.Entry(popup)
    name_entry.pack()
    name_entry.focus_set()
    cr_label = tk.Label(popup, text="Challenge Rating:")
    cr_label.pack()
    cr_entry = tk.Entry(popup)
    cr_entry.pack()
    submit_btn = tk.Button(popup, text="Submit", command=on_submit)
    submit_btn.pack(pady=10)
    cancel_btn = tk.Button(popup, text="Cancel", command=on_cancel)
    cancel_btn.pack(pady=10)

    popup.grab_set()
    root.wait_window(popup)
    return result["data"]

def delete_monster(root, left_frame=None, right_frame=None):
    global bestiary_flag
    if bestiary_flag == "archive":
        file_path = ARCHIVE_FILE_PATH

    popup = tk.Toplevel(root)
    popup.title(f"Delete Monster from {bestiary_flag}")

    instr_label = tk.Label(popup, text="Please type the name of the monster you wish to delete.\nThis is a permanent action, and they will have to be added again if needed!")
    instr_label.pack(pady=10)

    result = {"data": None}

    def on_submit():
        name_val = name_entry.get()

        monster_list = []
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                content = f.read().strip()
                if content:
                    monster_list = json.loads(content)

        found = False
        for mon in monster_list:
            if mon["name"].lower() == name_val.lower():
                monster_list.remove(mon)
                with open(file_path, "w") as f:
                    json.dump(monster_list, f, indent=4)
                popup.destroy()

                if left_frame and right_frame:
                    archive_page(root, left_frame, right_frame)
                found = True
                break

        if not found:
            show_error(f"{name_val} not found in {bestiary_flag}.", root)
            return

    def on_cancel():
        result["data"] = None
        popup.destroy()

    name_label = tk.Label(popup, text="Name:")
    name_label.pack()
    name_entry = tk.Entry(popup)
    name_entry.pack()
    name_entry.focus_set()
    submit_btn = tk.Button(popup, text="Submit", command=on_submit)
    submit_btn.pack(pady=10)
    cancel_btn = tk.Button(popup, text="Cancel", command=on_cancel)
    cancel_btn.pack(pady=10)