import tkinter as tk
from tkinter import messagebox
from database import save_customer


def create_customer_page(root):

    customer_page = tk.Frame(root, bg="white")

    title = tk.Label(
        customer_page,
        text="Customer Management",
        font=("Arial", 22, "bold"),
        bg="white",
        fg="#0B5394"
    )
    title.pack(pady=20)

    form_frame = tk.Frame(customer_page, bg="white")
    form_frame.pack(pady=20)

    # Customer Name
    tk.Label(form_frame, text="Customer Name",
             font=("Arial", 12, "bold"),
             bg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")

    name_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    # Mobile
    tk.Label(form_frame, text="Mobile Number",
             font=("Arial", 12, "bold"),
             bg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")

    mobile_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
    mobile_entry.grid(row=1, column=1, padx=10, pady=10)

    # Address
    tk.Label(form_frame, text="Address",
             font=("Arial", 12, "bold"),
             bg="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")

    address_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
    address_entry.grid(row=2, column=1, padx=10, pady=10)

    # Email
    tk.Label(form_frame, text="Email",
             font=("Arial", 12, "bold"),
             bg="white").grid(row=3, column=0, padx=10, pady=10, sticky="w")

    email_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
    email_entry.grid(row=3, column=1, padx=10, pady=10)

    # Aadhaar
    tk.Label(form_frame, text="Aadhaar Number",
             font=("Arial", 12, "bold"),
             bg="white").grid(row=4, column=0, padx=10, pady=10, sticky="w")

    aadhaar_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
    aadhaar_entry.grid(row=4, column=1, padx=10, pady=10)

    # Save Function
    def save_data():
        save_customer(
            name_entry.get(),
            mobile_entry.get(),
            address_entry.get(),
            email_entry.get(),
            aadhaar_entry.get()
        )

        messagebox.showinfo("Success", "Customer Saved Successfully")

        # Clear Entries
        name_entry.delete(0, tk.END)
        mobile_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        aadhaar_entry.delete(0, tk.END)

    # Save Button
    tk.Button(
        customer_page,
        text="Save Customer",
        bg="#0B5394",
        fg="white",
        font=("Arial", 12, "bold"),
        width=20,
        command=save_data
    ).pack(pady=20)

    return customer_page
    