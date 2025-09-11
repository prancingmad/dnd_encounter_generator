import tkinter as tk
import tkinter.simpledialog as simpledialog
from .player import *
from functions.config import *
from .delete_party_member import *
from .add_member import add_member
from .show_error import show_error
from .update_member import update_member

# Delete this later, once all the functions have been made
def placeholder_function(root, left_frame=None, right_frame=None):
    print("Button clicked - function not implemented yet")

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

# Page Functions
PAGE_FUNCTIONS = {
    "Add Member": add_member,
    "Add Monster": placeholder_function,
    "Archive": placeholder_function,
    "Clear Data": placeholder_function,
    "Close Program": close_program,
    "Delete Member": placeholder_function,
    "Delete Monster": placeholder_function,
    "Generate Encounter": placeholder_function,
    "Main Page": main_page,
    "Manage Bestiary": placeholder_function,
    "Manage Party": manage_party_page,
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
    "Add Monster": add_monster,
    "Archive": archive_page,
    "Clear Data": clear_data,
    "Delete Member": delete_member,
    "Delete Monster": delete_monster,
    "Generate Encounter": generate_encounter_page,
    "Manage Bestiary": manage_bestiary_page,
    "Move Monster to Archive": move_to_archive,
    "Move Monster to Random": move_to_random,
    "Move Monster to Required": move_to_required,
    "Random Encounters": random_encounters_page,
    "Required Encounters": required_encounters_page,
    "Update Member": update_member
}
"""