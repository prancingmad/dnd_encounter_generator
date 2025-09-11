import json

from functions.gui_functions import *
from functions.config import *
import tkinter as tk

if not os.path.exists("information"):
    os.makedirs("information")
if not os.path.exists(PARTY_FILE_PATH):
    with open(PARTY_FILE_PATH, "w") as f:
        json.dump([], f)
if not os.path.exists(REQUIRED_FILE_PATH):
    with open(REQUIRED_FILE_PATH, "w") as f:
        json.dump([], f)
if not os.path.exists(ARCHIVE_FILE_PATH):
    with open(ARCHIVE_FILE_PATH, "w") as f:
        json.dump([], f)
if not os.path.exists(RANDOM_FILE_PATH):
    with open(RANDOM_FILE_PATH, "w") as f:
        json.dump([], f)

root = tk.Tk()
root.title("DnD Encounter Generator")
root.geometry(WINDOW_SIZE)
root.resizable(True, True)

main_page(root)

root.mainloop()