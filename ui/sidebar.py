import tkinter as tk

from ui.dashboard import create_dashboard
from ui.customer import create_customer_page
from ui.product import create_product_page
from purchase import create_purchase_page
from ui.content import clear_content
from sales import create_sales_page


# ================= sales =================

def show_sales(content):
    clear_content(content)
    sales_page = create_sales_page(content)
    sales_page.pack(fill="both", expand=True)


# ================= Dashboard =================

def show_dashboard(content):
    clear_content(content)
    dashboard = create_dashboard(content)
    dashboard.pack(fill="both", expand=True)


# ================= Customer =================

def show_customer(content):
    clear_content(content)
    customer_page = create_customer_page(content)
    customer_page.pack(fill="both", expand=True)


# ================= Product =================

def show_product(content):
    clear_content(content)
    product_page = create_product_page(content)
    product_page.pack(fill="both", expand=True)


# ================= Purchase =================

def show_purchase(content):
    clear_content(content)
    purchase_page = create_purchase_page(content)
    purchase_page.pack(fill="both", expand=True)


# ================= Sidebar =================

def create_sidebar(root, content):

    sidebar = tk.Frame(
        root,
        bg="#1F2A36",
        width=220
    )

    sidebar.pack(side="left", fill="y")

    tk.Label(
        sidebar,
        text="MENU",
        bg="#1F2A36",
        fg="white",
        font=("Arial", 18, "bold")
    ).pack(pady=20)

    # Dashboard
    tk.Button(
        sidebar,
        text="Dashboard",
        bg="#34495E",
        fg="white",
        font=("Arial", 12),
        width=18,
        command=lambda: show_dashboard(content)
    ).pack(pady=5)

    # Customer
    tk.Button(
        sidebar,
        text="Customer",
        bg="#34495E",
        fg="white",
        font=("Arial", 12),
        width=18,
        command=lambda: show_customer(content)
    ).pack(pady=5)

    # Product
    tk.Button(
        sidebar,
        text="Products",
        bg="#34495E",
        fg="white",
        font=("Arial", 12),
        width=18,
        command=lambda: show_product(content)
    ).pack(pady=5)

    # Purchase
    tk.Button(
        sidebar,
        text="Purchase",
        bg="#34495E",
        fg="white",
        font=("Arial", 12),
        width=18,
        command=lambda: show_purchase(content)
    ).pack(pady=5)

# Sales
    tk.Button(
    sidebar,
    text="Sales",
    bg="#34495E",
    fg="white",
    font=("Arial", 12),
    width=18,
    command=lambda: show_sales(content)
    ).pack(pady=5)

    # Reports
    tk.Button(
        sidebar,
        text="Reports",
        bg="#34495E",
        fg="white",
        font=("Arial", 12),
        width=18
    ).pack(pady=5)

    return sidebar