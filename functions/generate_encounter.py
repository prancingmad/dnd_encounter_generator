import os
import json
import tkinter as tk
import random
from .show_error import show_error
from .config import (
    PARTY_FILE_PATH,
    RANDOM_FILE_PATH,
    REQUIRED_FILE_PATH
)

def generate_encounter(root, left_frame=None, right_frame=None):
    from .gui_functions import create_scrollable_frame
    party_list = []
    party_power = 0
    party_action = 0
    if os.path.exists(PARTY_FILE_PATH):
        with open(PARTY_FILE_PATH, "r") as f:
            content = f.read().strip()
            if content:
                party_list = json.loads(content)

    random_list = []
    if os.path.exists(RANDOM_FILE_PATH):
        with open(RANDOM_FILE_PATH, "r") as f:
            content = f.read().strip()
            if content:
                random_list = json.loads(content)

    required_list = []
    if os.path.exists(REQUIRED_FILE_PATH):
        with open(REQUIRED_FILE_PATH, "r") as f:
            content = f.read().strip()
            if content:
                required_list = json.loads(content)

    if not party_list:
        show_error("No characters in Party.", root)
    if not random_list and not required_list:
        show_error("No monsters in Random or Required bestiary", root)

    for plyr in party_list:
        party_power += plyr["combat_value"]
        party_action += plyr["actions"]

    generated_encounter = []
    encounter_actions = 0
    encounter_rating = 0

    for req in required_list:
        tempcount = req["count"]
        while tempcount > 0:
            generated_encounter.append(req)
            tempcount -= 1
            encounter_actions += req["actions"]
            encounter_rating += req["challenge_rating"]

    if random_list:
        failsafe = party_action + 4
        while encounter_rating < party_power and encounter_actions < party_action and failsafe > 0:
            failsafe -= 1
            rand_mon = random.choice(random_list)
            generated_encounter.append(rand_mon)
            encounter_rating += (rand_mon["challenge_rating"] * 0.75)
            encounter_actions += rand_mon["actions"]

    encounter_popup = tk.Toplevel(root)
    encounter_popup.title = "Suggested Encounter"

    scroll_frame = create_scrollable_frame(encounter_popup)
    for mon in generated_encounter:
        mon_text = f"{mon['name']} - Challenge Rating: {mon['challenge_rating']}"
        label = tk.Label(scroll_frame, text=mon_text, anchor="w", justify="left")
        label.pack(fill="x", pady=2)

    button_frame = tk.Frame(encounter_popup)
    button_frame.pack(side="bottom", pady=10)

    okay_btn = tk.Button(button_frame, text="OK", command=encounter_popup.destroy)
    okay_btn.pack(pady=10)

    encounter_popup.grab_set()
    root.wait_window(encounter_popup)

    return