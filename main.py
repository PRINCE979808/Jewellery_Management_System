import tkinter as tk

from database import create_database, update_sales_table

from ui.header import create_header
from ui.content import create_content
from ui.sidebar import create_sidebar
from ui.dashboard import create_dashboard

# ================= Database =================

# ================= Database =================

create_database()
update_sales_table()

# ================= Main Window =================

root = tk.Tk()

root.title("Jewellery Management System")
root.geometry("1366x768")
root.state("zoomed")
root.configure(bg="#F4F6F8")

# ================= Header =================

create_header(root)

# ================= Content =================

content = create_content(root)

# ================= Sidebar =================

create_sidebar(root, content)

# ================= Dashboard =================

dashboard = create_dashboard(content)
dashboard.pack(fill="both", expand=True)

# ================= Run =================

root.mainloop()
