import os
import json
import tkinter as tk
import random
from .show_error import show_error
from .config import (
    PARTY_FILE_PATH,
    RANDOM_FILE_PATH,
    REQUIRED_FILE_PATH,
    GENERATED_FILE_PATH
)

def generate_encounter(root):
    party_list = []
    party_power = 0
    party_action = 0
    if os.path.exists(PARTY_FILE_PATH):
        with open(PARTY_FILE_PATH, "r") as f:
            content = f.read().strip()
            if content:
                party_list = json.loads(content)

    random_list = []
    encounter_power = 0
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
            generated_encounter.append(req["name"])
            tempcount -= 1
            encounter_actions += req["actions"]
            encounter_rating += req["challenge_rating"]

    failsafe = 10
    while encounter_rating < party_power and encounter_actions < party_action and failsafe > 0:
        failsafe -= 1
        rand_mon = random.choice(random_list)
        generated_encounter.append(rand_mon["name"])
        encounter_rating += rand_mon["challenge_rating"]
        encounter_actions += rand_mon["actions"]


    return party_power, party_action, encounter_rating, encounter_actions, generated_encounter