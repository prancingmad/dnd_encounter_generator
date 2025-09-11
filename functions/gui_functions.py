import tkinter as tk
from functions.config import *
from .add_party_member import *
from .delete_party_member import *

# Delete this later, once all the functions have been made
def placeholder_function(root):
    print("Button clicked - function not implemented yet")

# Page Functions
PAGE_FUNCTIONS = {
    "Add Member": placeholder_function,
    "Add Monster": placeholder_function,
    "Archive": placeholder_function,
    "Clear Data": placeholder_function,
    "Close Program": placeholder_function,
    "Delete Member": placeholder_function,
    "Delete Monster": placeholder_function,
    "Generate Encounter": placeholder_function,
    "Main Page": placeholder_function,
    "Manage Bestiary": placeholder_function,
    "Manage Party": placeholder_function,
    "Move Monster to Archive": placeholder_function,
    "Move Monster to Random": placeholder_function,
    "Move Monster to Required": placeholder_function,
    "Random Encounters": placeholder_function,
    "Required Encounters": placeholder_function,
    "Update Member": placeholder_function
}

"""
Each page function will need this to be updated as we make
PAGE_FUNCTIONS = {
    "Add Member": add_member,
    "Add Monster": add_monster,
    "Archive": archive_page,
    "Clear Data": clear_data,
    "Close Program": close_program,
    "Delete Member": delete_member,
    "Delete Monster": delete_monster,
    "Generate Encounter": generate_encounter_page,
    "Main Page": main_page,
    "Manage Bestiary": manage_bestiary_page,
    "Manage Party": manage_party_page,
    "Move Monster to Archive": move_to_archive,
    "Move Monster to Random": move_to_random,
    "Move Monster to Required": move_to_required,
    "Random Encounters": random_encounters_page,
    "Required Encounters": required_encounters_page,
    "Update Member": update_member
}
"""


def on_button_click(label, root):
    func = PAGE_FUNCTIONS.get(label)
    if func:
        func(root)
    else:
        print(f"No function assigned/created for {label}")

def close_program(root):
    root.destroy()

def clear_widgets(root):
    widget_reset = root.winfo_children()
    for w in widget_reset:
        w.destroy()

def main_page(root):
    clear_widgets(root)
    button_frame = tk.Frame(root)
    button_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    for label in MAIN_PAGE_BUTTON_LABELS:
        btn = tk.Button(button_frame, text=label, command=lambda l=label: on_button_click(l, root))
        btn.pack(**BUTTON_PACK_OPTIONS)

def manage_party_page(root):
    clear_widgets(root)
    button_frame = tk.Frame(root)
    button_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    for label in MANAGE_PARTY_BUTTON_LABELS:
        btn = tk.Button(button_frame, text=label, command=lambda l=label: on_button_click(l, root))
        btn.pack(**BUTTON_PACK_OPTIONS)
