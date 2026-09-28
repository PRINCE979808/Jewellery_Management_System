import tkinter as tk

def create_content(root):

    content = tk.Frame(
        root,
        bg="white"
    )

    content.pack(
        side="left",
        fill="both",
        expand=True
    )

    return content


def clear_content(content):

    for widget in content.winfo_children():
        widget.destroy()
        


