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

container = tk.Frame(root)
container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

left_frame = tk.Frame(container, bg="lightgray")
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

right_frame = tk.Frame(container, width=300, bg="lightgray")
right_frame.pack(side=tk.LEFT, fill=tk.Y)
right_frame.pack_propagate(False)

main_page(root, left_frame, right_frame)

root.mainloop()