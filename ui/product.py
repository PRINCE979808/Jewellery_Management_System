import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from database import (
    save_product,
    get_all_products,
    delete_product,
    update_product
)


def create_product_page(root):

    product_page = tk.Frame(root, bg="white")

    title = tk.Label(
        product_page,
        text="Product Management",
        font=("Arial", 22, "bold"),
        bg="white",
        fg="#0B5394"
    )
    title.pack(pady=20)

    form = tk.Frame(product_page, bg="white")
    form.pack(pady=10)

    # ================= Product Name =================

    tk.Label(
        form,
        text="Customer Name",
        font=("Arial", 12, "bold"),
        bg="white"
    ).grid(row=0, column=0, padx=10, pady=10, sticky="w")

    product_name_entry = tk.Entry(form, width=30, font=("Arial", 12))
    product_name_entry.grid(row=0, column=1, padx=10)

    selected_product_id = [None]

    # ================= Category =================

    tk.Label(
        form,
        text="Category",
        font=("Arial", 12, "bold"),
        bg="white"
    ).grid(row=1, column=0, padx=10, pady=10, sticky="w")

    category = tk.StringVar(value="Ring")

    tk.OptionMenu(
        form,
        category,
        "Ring",
        "Chain",
        "Bangle",
        "Necklace",
        "Pendant",
        "Locket",
        "Tops",
        "Nathiya",
        "Tikka",
        "Earrings",
        "Coin"
    ).grid(row=1, column=1, sticky="w")

    # ================= Metal =================

    tk.Label(
        form,
        text="Metal",
        font=("Arial", 12, "bold"),
        bg="white"
    ).grid(row=2, column=0, padx=10, pady=10, sticky="w")

    metal = tk.StringVar(value="Gold")

    tk.OptionMenu(
        form,
        metal,
        "Gold",
        "Silver",
        "Diamond"
    ).grid(row=2, column=1, sticky="w")

    # ================= Weight =================

    tk.Label(
        form,
        text="Weight (Gram)",
        font=("Arial", 12, "bold"),
        bg="white"
    ).grid(row=3, column=0, padx=10, pady=10, sticky="w")

    weight_entry = tk.Entry(form, width=30, font=("Arial", 12))
    weight_entry.grid(row=3, column=1)

    # ================= Selling Price =================

    tk.Label(
        form,
        text="Selling Price",
        font=("Arial", 12, "bold"),
        bg="white"
    ).grid(row=4, column=0, padx=10, pady=10, sticky="w")

    selling_price_entry = tk.Entry(form, width=30, font=("Arial", 12))
    selling_price_entry.grid(row=4, column=1)

    # ================= Table =================

    columns = (
        "ID",
        "Product Name",
        "Category",
        "Metal",
        "Weight",
        "Price"
    )

    tree = ttk.Treeview(
        product_page,
        columns=columns,
        show="headings",
        height=8
    )

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor="center")

    # ================= Load Products =================

    def load_products():

        for row in tree.get_children():
            tree.delete(row)

        products = get_all_products()

        for product in products:
            tree.insert("", tk.END, values=product)

    # ================= Select Product =================

    def select_product(event):

        selected = tree.selection()

        if not selected:
            return

        item = tree.item(selected)
        data = item["values"]

        selected_product_id[0] = data[0]

        product_name_entry.delete(0, tk.END)
        product_name_entry.insert(0, data[1])

        category.set(data[2])

        metal.set(data[3])

        weight_entry.delete(0, tk.END)
        weight_entry.insert(0, data[4])

        selling_price_entry.delete(0, tk.END)
        selling_price_entry.insert(0, data[5])

    tree.bind("<<TreeviewSelect>>", select_product)

    # ================= Save Product =================

    def save_data():

        if product_name_entry.get() == "":
            messagebox.showerror("Error", "Enter Product Name")
            return

        if selected_product_id[0] is None:

            save_product(
                product_name_entry.get(),
                category.get(),
                metal.get(),
                weight_entry.get(),
                selling_price_entry.get()
            )

            messagebox.showinfo("Success", "Product Saved Successfully")

        else:

            update_product(
                selected_product_id[0],
                product_name_entry.get(),
                category.get(),
                metal.get(),
                weight_entry.get(),
                selling_price_entry.get()
            )

            messagebox.showinfo("Success", "Product Updated Successfully")

            selected_product_id[0] = None

        product_name_entry.delete(0, tk.END)
        weight_entry.delete(0, tk.END)
        selling_price_entry.delete(0, tk.END)

        category.set("Ring")
        metal.set("Gold")

        load_products()

    # ================= Delete Product =================

    def delete_selected():

        selected = tree.selection()

        if not selected:
            messagebox.showerror("Error", "Please Select Product")
            return

        item = tree.item(selected)

        product_id = item["values"][0]

        delete_product(product_id)

        load_products()

        messagebox.showinfo("Success", "Product Deleted Successfully")

    # ================= Buttons =================

    tk.Button(
        product_page,
        text="Save Product",
        bg="#0B5394",
        fg="white",
        font=("Arial", 12, "bold"),
        width=20,
        command=save_data
    ).pack(pady=10)

    tk.Button(
        product_page,
        text="Delete Product",
        bg="red",
        fg="white",
        font=("Arial", 12, "bold"),
        width=20,
        command=delete_selected
    ).pack(pady=5)

    tree.pack(fill="both", expand=True, padx=20, pady=20)

    load_products()

    return product_page
    