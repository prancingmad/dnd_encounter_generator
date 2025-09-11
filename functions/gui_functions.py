import tkinter as tk
from functions.config import *

def on_button_click(label):
    print(f"{label} button clicked")

def clear_widgets(root):
    widget_reset = root.winfo_children()
    for w in widget_reset:
        w.destroy()

def main_page(root):
    clear_widgets(root)
    button_frame = tk.Frame(root)
    button_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    for label in MAIN_PAGE_BUTTON_LABELS:
        btn = tk.Button(button_frame, text=label, command=lambda l=label: on_button_click(l))
        btn.pack(**BUTTON_PACK_OPTIONS)

def manage_party_page(root):
    clear_widgets(root)
    button_frame = tk.Frame(root)
    button_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    for label in MANAGE_PARTY_BUTTON_LABELS:
        btn = tk.Button(button_frame, text=label, command=lambda l=label: on_button_click(l))
        btn.pack(**BUTTON_PACK_OPTIONS)
