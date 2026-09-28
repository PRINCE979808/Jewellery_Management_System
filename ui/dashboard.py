import tkinter as tk

def create_dashboard(parent):

    dashboard = tk.Frame(parent, bg="white")
    dashboard.pack(side="left", fill="both", expand=True)

    title = tk.Label(
        dashboard,
        text="Dashboard",
        font=("Arial", 22, "bold"),
        bg="white",
        fg="#0B5394"
    )
    title.pack(pady=20)

    cards_frame = tk.Frame(
        dashboard,
        bg="white"
    )
    cards_frame.pack(pady=20)

    # ================= Customer Card =================

    customer_card = tk.Frame(
        cards_frame,
        bg="#3498DB",
        width=220,
        height=120
    )
    customer_card.pack(side="left", padx=20)
    customer_card.pack_propagate(False)

    tk.Label(
        customer_card,
        text="Total Customers",
        bg="#3498DB",
        fg="white",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    tk.Label(
        customer_card,
        text="0",
        bg="#3498DB",
        fg="white",
        font=("Arial", 28, "bold")
    ).pack()

    # ================= Product Card =================

    product_card = tk.Frame(
        cards_frame,
        bg="#27AE60",
        width=220,
        height=120
    )
    product_card.pack(side="left", padx=20)
    product_card.pack_propagate(False)

    tk.Label(
        product_card,
        text="Total Products",
        bg="#27AE60",
        fg="white",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    tk.Label(
        product_card,
        text="0",
        bg="#27AE60",
        fg="white",
        font=("Arial", 28, "bold")
    ).pack()

    # ================= Today's Sales Card =================

    sales_card = tk.Frame(
        cards_frame,
        bg="#E67E22",
        width=220,
        height=120
    )
    sales_card.pack(side="left", padx=20)
    sales_card.pack_propagate(False)

    tk.Label(
        sales_card,
        text="Today's Sales",
        bg="#E67E22",
        fg="white",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    tk.Label(
        sales_card,
        text="₹0.00",
        bg="#E67E22",
        fg="white",
        font=("Arial", 28, "bold")
    ).pack()
    # ================= Total Stock Value Card =================

    stock_card = tk.Frame(
        cards_frame,
        bg="#9B59B6",
        width=220,
        height=120
    )

    stock_card.pack(side="left", padx=20)
    stock_card.pack_propagate(False)

    tk.Label(
        stock_card,
        text="Total Stock Value",
        bg="#9B59B6",
        fg="white",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    tk.Label(
        stock_card,
        text="₹0.00",
        bg="#9B59B6",
        fg="white",
        font=("Arial", 28, "bold")
    ).pack()
    
    return dashboard
    