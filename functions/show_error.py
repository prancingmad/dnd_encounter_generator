import tkinter as tk

def show_error(msg, root):
    error_popup = tk.Toplevel(root)
    error_popup.title("Error")
    error_popup.resizable(False, False)

    error_label = tk.Label(error_popup, text=msg, padx=10, pady=10)
    error_label.pack(pady=10)

    okay_btn = tk.Button(error_popup, text="OK", command=error_popup.destroy)
    okay_btn.pack(pady=10)

    error_popup.grab_set()
    root.wait_window(error_popup)