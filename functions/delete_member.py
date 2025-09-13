import os
import json
import tkinter as tk
from .show_error import show_error
from .config import PARTY_FILE_PATH

def delete_member(root, left_frame=None, right_frame=None):
    popup = tk.Toplevel(root)
    popup.title("Delete Party Member")

    instr_label = tk.Label(popup, text="Please type the name of the character you wish to delete.\nThis is a permanent action, and they will have to be added again if needed!")
    instr_label.pack(pady=10)

    result = {"data": None}

    def on_submit():
        name_val = name_entry.get()

        players_list = []
        if os.path.exists(PARTY_FILE_PATH):
            with open(PARTY_FILE_PATH, "r") as f:
                content = f.read().strip()
                if content:
                    players_list = json.loads(content)

        found = False
        for player in players_list:
            if player["name"].lower() == name_val.lower():
                players_list.remove(player)
                with open(PARTY_FILE_PATH, "w") as f:
                    json.dump(players_list, f, indent=4)
                popup.destroy()

                if left_frame and right_frame:
                    from .gui_functions import manage_party_page
                    manage_party_page(root, left_frame, right_frame)
                found = True
                break

        if not found:
            show_error(f"{name_val} not found in current party.", root)
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