from gui_functions import *
from functions.config import *
import tkinter as tk


def on_button_click(label):
    print(f"{label} button clicked")

root = tk.Tk()
root.title("DnD Encounter Generator")
root.geometry(WINDOW_SIZE)
root.resizable(True, True)

button_frame = tk.Frame(root)
button_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

for label in MAIN_PAGE_BUTTON_LABELS:
    btn = tk.Button(button_frame, text=label, command=lambda l=label: on_button_click(l))
    btn.pack(**BUTTON_PACK_OPTIONS)

root.mainloop()