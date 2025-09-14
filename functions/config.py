import tkinter as tk
import os

# Pathing
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PARTY_FILE_PATH = os.path.join(BASE_DIR, "information", "party.json")
RANDOM_FILE_PATH = os.path.join(BASE_DIR, "information", "random_encounters.json")
REQUIRED_FILE_PATH = os.path.join(BASE_DIR, "information", "required_encounters.json")
ARCHIVE_FILE_PATH = os.path.join(BASE_DIR, "information", "archive.json")

# Descriptive Text
MAIN_PAGE_TEXT = 'Hello and welcome to the D&D 5e Encounter Generator! \nUse "Manage Party" to Add, Update, and Delete members of the party.\nTheir power level will be automatically calculated for the generator.\n*Note - Party members are currently limited to the base DnD classes, and doesn\'t currently support homebrew.\nUse Manage Bestiary to Add and Delete monsters for the encounter.\nOnce you have filled the Party, and the Bestiary, click "Generate Encounter" to pop-up with a recommended encounter!\nUse "Clear Data" if you wish to erase all Data - Party and Bestiary.\n\n\n\n\n\n\n\n\nCreated by Prancing Mad\nDungeons & Dragons® and all associated content are © 1974–2025 Wizards of the Coast LLC. All rights reserved.'
BESTIARY_PAGE_TEXT = 'Here\'s the bestiary, where you can manage what monsters you would like to pull.\nThe generator will first pull from "Required Encounters", so that you can guarantee the encounter will have certain creatures.\n"Encounter Count" will allow you to specify how many of each monster you want to appear.\n"Random Encounters" will be what you want to fill the rest of the encounter with, and it will randomly pull from this section.\nArchive is for archived monsters, in case you want to move monsters in and out and use them again later.\nThe generator will not pull from this section at all.\nEach section will let you move monsters to the other section.'

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
WINDOW_SIZE = "1000x350"
BUTTON_PACK_OPTIONS = {"fill": tk.X, "pady": 5, "expand": True}
VALID_CLASSES = ["Artificer", "Barbarian", "Bard", "Cleric", "Druid",
                 "Fighter", "Monk", "Paladin", "Ranger", "Rogue",
                 "Sorcerer", "Warlock", "Wizard"]