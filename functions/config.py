import tkinter as tk
import os

# Pathing
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PARTY_FILE_PATH = os.path.join(BASE_DIR, "information", "party.json")
RANDOM_FILE_PATH = os.path.join(BASE_DIR, "information", "random_encounters.json")
REQUIRED_FILE_PATH = os.path.join(BASE_DIR, "information", "required_encounters.json")
ARCHIVE_FILE_PATH = os.path.join(BASE_DIR, "information", "archive.json")

# Configure base class modifiers
ARTI_MOD = 1
BARB_MOD = 1
BARD_MOD = 1
CLER_MOD = 1
DRUI_MOD = 1
FIGH_MOD = 1
MONK_MOD = 1
PALA_MOD = 1
RANG_MOD = 1
ROGU_MOD = 1
SORC_MOD = 1
WARL_MOD = 1
WIZA_MOD = 1

# Specific Mods
SURGE_MOD = 0.25
EXTRA_ATTACK_MOD = 0.25
RECKLESS_MOD = 0.25
SMITE_MOD = 0.25
STUN_STRIKE_MOD = 0.25

# Button Labels
MAIN_PAGE_BUTTON_LABELS = {
    "Manage Party": manage_party_page,
    "Manage Bestiary": manage_bestiary_page,
    "Generate Encounter": generate_encounter_page,
    "Clear Data": clear_data,
    "Close Program": close_program
}
MANAGE_PARTY_BUTTON_LABELS = {
    "Add Member": add_member,
    "Update Member": update_member,
    "Delete Member": delete_member,
    "Back": main_page
}
MANAGE_BESTIARY_BUTTON_LABELS = {
    "Required Encounters": required_encounters_page,
    "Random Encounters": random_encounters_page,
    "Archive": archive_page,
    "Back": main_page
}
REQUIRED_ENCOUNTERS_BUTTON_LABELS = {
    "Add Monster": add_monster,
    "Delete Monster": delete_monster,
    "Move Monster to Random": move_to_random,
    "Move Monster to Archive": move_to_archive,
    "Back": manage_bestiary_page
}
RANDOM_ENCOUNTERS_BUTTON_LABELS = [
    "Add Monster",
    "Delete Monster",
    "Move Monster to Required",
    "Move Monster to Archive",
    "Back"
]
ARCHIVE_BUTTON_LABELS = [
    "Add Monster",
    "Delete Monster",
    "Move Monster to Required",
    "Move Monster to Random",
    "Back"
]

# Constants
WINDOW_SIZE = "400x300"
BUTTON_PACK_OPTIONS = {"fill": tk.X, "pady": 5, "expand": True}