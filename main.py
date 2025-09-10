import tkinter as tk

def on_button_click(label):
    print(f"{label} button clicked")

root = tk.Tk()
root.title("DnD Encounter Generator")
root.geometry("400x300")
root.resizable(True, True)

button_frame = tk.Frame(root)
button_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

main_page_button_labels = [
    "Manage Party",
    "Manage Bestiary",
    "Generate Encounter",
    "Clear Data",
    "Close Program"
]

for label in main_page_button_labels:
    btn = tk.Button(button_frame, text=label, command=lambda l=label: on_button_click(l))
    btn.pack(fill=tk.X, pady=5)

root.mainloop()