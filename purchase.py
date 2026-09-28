import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from database import (
    save_purchase,
    get_all_purchase,
    delete_purchase,
    update_purchase
)


def create_purchase_page(root):

    purchase_page = tk.Frame(root, bg="white")

    # ================= Title =================

    title = tk.Label(
        purchase_page,
        text="Purchase Management",
        font=("Arial", 22, "bold"),
        bg="white",
        fg="#0B5394"
    )
    title.pack(pady=20)

    # ================= Form =================

    form = tk.Frame(purchase_page, bg="white")
    form.pack(pady=10)

    # ================= Supplier Name =================

    tk.Label(
        form,
        text="Supplier Name",
        font=("Arial", 12, "bold"),
        bg="white"
    ).grid(row=0, column=0, padx=10, pady=10, sticky="w")

    supplier_entry = tk.Entry(
        form,
        width=30,
        font=("Arial", 12)
    )
    supplier_entry.grid(row=0, column=1)

    selected_purchase_id = [None]

    # ================= Bill No =================

    tk.Label(
        form,
        text="Bill No",
        font=("Arial", 12, "bold"),
        bg="white"
    ).grid(row=1, column=0, padx=10, pady=10, sticky="w")

    bill_entry = tk.Entry(
        form,
        width=30,
        font=("Arial", 12)
    )
    bill_entry.grid(row=1, column=1)

    # ================= Total Amount =================

    tk.Label(
        form,
        text="Total Amount",
        font=("Arial", 12, "bold"),
        bg="white"
    ).grid(row=2, column=0, padx=10, pady=10, sticky="w")

    amount_entry = tk.Entry(
        form,
        width=30,
        font=("Arial", 12)
    )
    amount_entry.grid(row=2, column=1)

    # ================= Purchase Date =================

    tk.Label(
        form,
        text="Purchase Date",
        font=("Arial", 12, "bold"),
        bg="white"
    ).grid(row=3, column=0, padx=10, pady=10, sticky="w")

    date_entry = tk.Entry(
        form,
        width=30,
        font=("Arial", 12)
    )
    date_entry.grid(row=3, column=1)

    # ================= Purchase Table =================

    columns = (
        "ID",
        "Supplier Name",
        "Bill No",
        "Total Amount",
        "Purchase Date"
    )

    tree = ttk.Treeview(
        purchase_page,
        columns=columns,
        show="headings",
        height=8
    )

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150, anchor="center")

    # ================= Load Purchase =================

    def load_purchase():

        for row in tree.get_children():
            tree.delete(row)

        purchases = get_all_purchase()

        for purchase in purchases:
            tree.insert("", tk.END, values=purchase)

    # ================= Select Purchase =================

    def select_purchase(event):

        selected = tree.selection()

        if not selected:
            return

        item = tree.item(selected)
        data = item["values"]

        selected_purchase_id[0] = data[0]

        supplier_entry.delete(0, tk.END)
        supplier_entry.insert(0, data[1])

        bill_entry.delete(0, tk.END)
        bill_entry.insert(0, data[2])

        amount_entry.delete(0, tk.END)
        amount_entry.insert(0, data[3])

        date_entry.delete(0, tk.END)
        date_entry.insert(0, data[4])

    tree.bind("<<TreeviewSelect>>", select_purchase)

    # ================= Save / Update =================

    def save_data():

        if supplier_entry.get() == "":
            messagebox.showerror("Error", "Enter Supplier Name")
            return

        if selected_purchase_id[0] is None:

            save_purchase(
                supplier_entry.get(),
                bill_entry.get(),
                amount_entry.get(),
                date_entry.get()
            )

            messagebox.showinfo(
                "Success",
                "Purchase Saved Successfully"
            )

        else:

            update_purchase(
                selected_purchase_id[0],
                supplier_entry.get(),
                bill_entry.get(),
                amount_entry.get(),
                date_entry.get()
            )

            messagebox.showinfo(
                "Success",
                "Purchase Updated Successfully"
            )

            selected_purchase_id[0] = None

        supplier_entry.delete(0, tk.END)
        bill_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)

        load_purchase()

    # ================= Delete Purchase =================

    def delete_selected():

        selected = tree.selection()

        if not selected:
            messagebox.showerror(
                "Error",
                "Please Select Purchase"
            )
            return

        item = tree.item(selected)

        purchase_id = item["values"][0]

        delete_purchase(purchase_id)

        load_purchase()

        messagebox.showinfo(
            "Success",
            "Purchase Deleted Successfully"
        )

    # ================= Buttons =================

    tk.Button(
        purchase_page,
        text="Save Purchase",
        bg="#0B5394",
        fg="white",
        font=("Arial", 12, "bold"),
        width=20,
        command=save_data
    ).pack(pady=10)

    tk.Button(
        purchase_page,
        text="Update Purchase",
        bg="green",
        fg="white",
        font=("Arial", 12, "bold"),
        width=20,
        command=save_data
    ).pack(pady=5)

    tk.Button(
        purchase_page,
        text="Delete Purchase",
        bg="red",
        fg="white",
        font=("Arial", 12, "bold"),
        width=20,
        command=delete_selected
    ).pack(pady=5)

    # ================= Table =================

    tree.pack(fill="both", expand=True, padx=20, pady=20)

    load_purchase()

    return purchase_page
    