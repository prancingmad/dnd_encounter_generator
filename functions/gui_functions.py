import tkinter as tk
import json
import os
from .delete_member import delete_member
from .add_member import add_member
from .show_error import show_error
from .update_member import update_member
from .generate_encounter import generate_encounter
from .config import (MAIN_PAGE_TEXT,
                     MAIN_PAGE_BUTTON_LABELS,
                     BUTTON_PACK_OPTIONS,
                     PARTY_FILE_PATH,
                     MANAGE_PARTY_BUTTON_LABELS,
                     BESTIARY_PAGE_TEXT,
                     MANAGE_BESTIARY_BUTTON_LABELS,
                     ARCHIVE_FILE_PATH,
                     ARCHIVE_BUTTON_LABELS,
                     REQUIRED_FILE_PATH,
                     RANDOM_FILE_PATH
                     )


def create_scrollable_frame(parent):
    canvas = tk.Canvas(parent)
    scrollbar = tk.Scrollbar(parent, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    return scrollable_frame

def on_button_click(label, root, left_frame=None, right_frame=None):
    if label == "Add Monster":
        from .bestiary_functions import add_monster
        func = add_monster
    elif label == "Delete Monster":
        from .bestiary_functions import delete_monster
        func = delete_monster
    elif label == "Archive":
        from .bestiary_functions import archive_page
        func = archive_page
    elif label == "Random Encounters":
        from .bestiary_functions import random_encounters_page
        func = random_encounters_page
    elif label == "Required Encounters":
        from .bestiary_functions import required_encounters_page
        func = required_encounters_page
    elif label == "Move Monster to Random":
        from .bestiary_functions import move_monster_to_random
        func = move_monster_to_random
    elif label == "Move Monster to Archive":
        from .bestiary_functions import move_monster_to_archive
        func = move_monster_to_archive
    elif label == "Move Monster to Required":
        from .bestiary_functions import move_monster_to_required
        func = move_monster_to_required
    else:
        func = PAGE_FUNCTIONS.get(label)

    if func:
        if left_frame and right_frame:
            func(root, left_frame, right_frame)
        else:
            func(root)
    else:
        print(f"No function assigned/created for {label}")

def close_program(root, left_frame=None, right_frame=None):
    root.destroy()

def clear_widgets(parent):
    for w in parent.winfo_children():
        w.destroy()

def main_page(root, left_frame, right_frame):
    clear_widgets(left_frame)
    clear_widgets(right_frame)

    placeholder_label = tk.Label(left_frame, text=MAIN_PAGE_TEXT, anchor="nw", justify="left")
    placeholder_label.pack(fill=tk.BOTH, expand=True)

    button_frame = tk.Frame(right_frame)
    button_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    for label in MAIN_PAGE_BUTTON_LABELS:
        btn = tk.Button(button_frame, text=label, command=lambda l=label: on_button_click(l, root, left_frame, right_frame))
        btn.pack(**BUTTON_PACK_OPTIONS)

def manage_party_page(root, left_frame, right_frame):
    clear_widgets(left_frame)
    clear_widgets(right_frame)

    scroll_frame = create_scrollable_frame(left_frame)
    with open(PARTY_FILE_PATH, "r") as f:
        content = f.read().strip()
        if content:
            f.seek(0)
            party_data = json.load(f)

            for member in party_data:
                classes_text = ", ".join([f"{cls['name']} {cls['level']}" for cls in member['classes']])
                member_text = f"{member['name']} - Combat Value: {member['combat_value']}, AC: {member['armor_class']}, Magic Item Count: {member['magic_items']}, Classes: {classes_text}"
                label = tk.Label(scroll_frame, text=member_text, anchor="w", justify="left")
                label.pack(fill="x", pady=2)
        else:
            placeholder_label = tk.Label(left_frame, text="", anchor="nw", justify="left")
            placeholder_label.pack(fill=tk.BOTH, expand=True)


    button_frame = tk.Frame(right_frame)
    button_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    for label in MANAGE_PARTY_BUTTON_LABELS:
        btn = tk.Button(button_frame, text=label, command=lambda l=label: on_button_click(l, root, left_frame, right_frame))
        btn.pack(**BUTTON_PACK_OPTIONS)

def manage_bestiary_page(root, left_frame, right_frame):
    clear_widgets(left_frame)
    clear_widgets(right_frame)

    placeholder_label = tk.Label(left_frame, text=BESTIARY_PAGE_TEXT, anchor="nw", justify="left")
    placeholder_label.pack(fill=tk.BOTH, expand=True)

    button_frame = tk.Frame(right_frame)
    button_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    for label in MANAGE_BESTIARY_BUTTON_LABELS:
        btn = tk.Button(button_frame, text=label,
                        command=lambda l=label: on_button_click(l, root, left_frame, right_frame))
        btn.pack(**BUTTON_PACK_OPTIONS)

def clear_data(root, left_frame, right_frame):
    popup = tk.Toplevel(root)
    popup.title("Clear Data Confirmation")

    instr_label = tk.Label(popup, text="This will delete all player and monster data.\nPlease confirm.")
    instr_label.pack(pady=10)

    result = {"data": None}

    def on_submit():
        empty_list = []
        if os.path.exists(PARTY_FILE_PATH):
            with open(PARTY_FILE_PATH, "w") as f:
                json.dump(empty_list, f, indent=4)
        if os.path.exists(RANDOM_FILE_PATH):
            with open(RANDOM_FILE_PATH, "w") as f:
                json.dump(empty_list, f, indent=4)
        if os.path.exists(REQUIRED_FILE_PATH):
            with open(REQUIRED_FILE_PATH, "w") as f:
                json.dump(empty_list, f, indent=4)
        if os.path.exists(ARCHIVE_FILE_PATH):
            with open(ARCHIVE_FILE_PATH, "w") as f:
                json.dump(empty_list, f, indent=4)
        popup.destroy()

    def on_cancel():
        result["data"] = None
        popup.destroy()

    submit_btn = tk.Button(popup, text="Confirm", command=on_submit)
    submit_btn.pack(pady=10)
    cancel_btn = tk.Button(popup, text="Cancel", command=on_cancel)
    cancel_btn.pack(pady=10)

# Page Functions
PAGE_FUNCTIONS = {
    "Add Member": add_member,
    "Clear Data": clear_data,
    "Close Program": close_program,
    "Delete Member": delete_member,
    "Generate Encounter": generate_encounter,
    "Main Page": main_page,
    "Manage Bestiary": manage_bestiary_page,
    "Manage Party": manage_party_page,
    "Update Member": update_member
}