def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

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

    conn.commit()
    conn.close()