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



    return party_power, party_action