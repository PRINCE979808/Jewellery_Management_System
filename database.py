import sqlite3

DB_NAME = "jewellery.db"


def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Customers Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers(
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            mobile TEXT,
            address TEXT,
            email TEXT,
            aadhaar TEXT
        )
    """)

    # Product Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            category TEXT,
            metal TEXT,
            purity TEXT,
            hsn_code TEXT,
            purchase_price REAL,
            selling_price REAL,
            making_charge REAL,
            wastage REAL,
            stock_weight REAL,
            stock_qty INTEGER,
            description TEXT
        )
    """)

    # Sales Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales(
            sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT,
            mobile TEXT,
            bill_no TEXT,
            total_amount REAL,
            paid_amount REAL,
            balance REAL,
            sale_date TEXT
        )
    """)

    # Purchase Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS purchase(
            purchase_id INTEGER PRIMARY KEY AUTOINCREMENT,
            supplier_name TEXT,
            bill_no TEXT,
            total_amount REAL,
            purchase_date TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_customer(name, mobile, address, email, aadhaar):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO customers
        (customer_name, mobile, address, email, aadhaar)
        VALUES (?, ?, ?, ?, ?)
    """, (name, mobile, address, email, aadhaar))

    conn.commit()
    conn.close()


def save_product(product_name, category, metal, weight, selling_price):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO products
        (product_name, category, metal, stock_weight, selling_price)
        VALUES (?, ?, ?, ?, ?)
    """, (
        product_name,
        category,
        metal,
        weight,
        selling_price
    ))

    conn.commit()
    conn.close()


def get_all_products():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            product_id,
            product_name,
            category,
            metal,
            stock_weight,
            selling_price
        FROM products
    """)

    data = cursor.fetchall()

    conn.close()

    return data


def delete_product(product_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM products WHERE product_id=?",
        (product_id,)
    )

    conn.commit()
    conn.close()


def update_product(product_id, product_name, category, metal, weight, selling_price):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE products
        SET
            product_name=?,
            category=?,
            metal=?,
            stock_weight=?,
            selling_price=?
        WHERE product_id=?
    """, (
        product_name,
        category,
        metal,
        weight,
        selling_price,
        product_id
    ))


    conn.commit()
    conn.close()
# ================= Purchase =================

def save_purchase(supplier_name, bill_no, total_amount, purchase_date):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO purchase
        (supplier_name, bill_no, total_amount, purchase_date)
        VALUES (?, ?, ?, ?)
    """, (
        supplier_name,
        bill_no,
        total_amount,
        purchase_date
    ))

    conn.commit()
    conn.close()


def get_all_purchase():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            purchase_id,
            supplier_name,
            bill_no,
            total_amount,
            purchase_date
        FROM purchase
    """)

    data = cursor.fetchall()

    conn.close()

    return data


def delete_purchase(purchase_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM purchase WHERE purchase_id=?",
        (purchase_id,)
    )

    conn.commit()
    conn.close()


def update_purchase(purchase_id, supplier_name, bill_no, total_amount, purchase_date):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE purchase
        SET
            supplier_name=?,
            bill_no=?,
            total_amount=?,
            purchase_date=?
        WHERE purchase_id=?
    """, (
        supplier_name,
        bill_no,
        total_amount,
        purchase_date,
        purchase_id
    ))

def update_sales_table():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    new_columns = [
        ("product_name", "TEXT"),
        ("weight", "REAL"),
        ("quantity", "INTEGER"),
        ("rate", "REAL"),
        ("making_charge", "REAL"),
        ("wastage", "REAL"),
        ("gst", "REAL"),
        ("discount", "REAL")
    ]

    cursor.execute("PRAGMA table_info(sales)")
    existing_columns = [col[1] for col in cursor.fetchall()]

    for column_name, column_type in new_columns:
        if column_name not in existing_columns:
            cursor.execute(
                f"ALTER TABLE sales ADD COLUMN {column_name} {column_type}"
            )

def save_sale(
    customer_name,
    mobile,
    bill_no,
    product_name,
    weight,
    quantity,
    rate,
    making_charge,
    wastage,
    gst,
    discount,
    total_amount,
    paid_amount,
    balance,
    sale_date
):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO sales(
            customer_name,
            mobile,
            bill_no,
            product_name,
            weight,
            quantity,
            rate,
            making_charge,
            wastage,
            gst,
            discount,
            total_amount,
            paid_amount,
            balance,
            sale_date
        )
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, (
        customer_name,
        mobile,
        bill_no,
        product_name,
        weight,
        quantity,
        rate,
        making_charge,
        wastage,
        gst,
        discount,
        total_amount,
        paid_amount,
        balance,
        sale_date
    ))

    conn.commit()
    conn.close()
    