import tkinter as tk

def create_sales_page(root):

    sales_page = tk.Frame(root, bg="white")

    title = tk.Label(
        sales_page,
        text="Sales Management",
        font=("Arial", 22, "bold"),
        bg="white",
        fg="#0B5394"
    )
    title.pack(pady=20)

    return sales_page
    