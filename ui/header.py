import tkinter as tk

def create_header(root):
    header = tk.Frame(root, bg="#0B5394", height=70)
    header.pack(fill="x")

    title = tk.Label(
        header,
        text="JEWELLERY MANAGEMENT SYSTEM",
        font=("Arial", 24, "bold"),
        bg="#0B5394",
        fg="white"
    )

    title.pack(pady=15)
    