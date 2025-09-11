import tkinter as tk
import os

# Pathing
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PARTY_FILE_PATH = os.path.join(BASE_DIR, "information", "party.json")
RANDOM_FILE_PATH = os.path.join(BASE_DIR, "information", "random_encounters.json")
REQUIRED_FILE_PATH = os.path.join(BASE_DIR, "information", "required_encounters.json")
ARCHIVE_FILE_PATH = os.path.join(BASE_DIR, "information", "archive.json")

# Main Page Text
MAIN_PAGE_TEXT = "Hello and welcome to the D&D 5e Encounter Generator! \nPlaceholder"

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
MAIN_PAGE_BUTTON_LABELS = [
    "Manage Party",
    "Manage Bestiary",
    "Generate Encounter",
    "Clear Data",
    "Close Program"
]
MANAGE_PARTY_BUTTON_LABELS = [
    "Add Member",
    "Update Member",
    "Delete Member",
    "Main Page"
]
MANAGE_BESTIARY_BUTTON_LABELS = [
    "Required Encounters",
    "Random Encounters",
    "Archive",
    "Main Page"
]
REQUIRED_ENCOUNTERS_BUTTON_LABELS = [
    "Add Monster",
    "Delete Monster",
    "Move Monster to Random",
    "Move Monster to Archive",
    "Manage Bestiary",
    "Main Page"
]
RANDOM_ENCOUNTERS_BUTTON_LABELS = [
    "Add Monster",
    "Delete Monster",
    "Move Monster to Required",
    "Move Monster to Archive",
    "Manage Bestiary",
    "Main Page"
]
ARCHIVE_BUTTON_LABELS = [
    "Add Monster",
    "Delete Monster",
    "Move Monster to Required",
    "Move Monster to Random",
    "Manage Bestiary",
    "Main Page"
]

# Constants
WINDOW_SIZE = "850x300"
BUTTON_PACK_OPTIONS = {"fill": tk.X, "pady": 5, "expand": True}