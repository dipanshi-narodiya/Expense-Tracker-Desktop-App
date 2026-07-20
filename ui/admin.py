import tkinter as tk
from tkinter import ttk, messagebox
from utils.export_users import export_users_excel
from utils.admin_export_pdf import export_users_pdf

from utils.admin_helper import (
    get_all_users,
    search_users,
    delete_user,
    get_user_summary,
    get_admin_statistics
)


class AdminWindow:

    def __init__(self):

        self.root = tk.Toplevel()

        self.root.title("Admin Panel")

        self.root.geometry("1000x600")

        self.root.state("zoomed")

        self.create_widgets()

    # ==========================================
    # Create Widgets
    # ==========================================

    def create_widgets(self):

        title = tk.Label(
            self.root,
            text="👨‍💼 Admin Panel",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=20)

        stats = get_admin_statistics()

        stats_frame = tk.Frame(self.root)
        stats_frame.pack(fill="x", padx=20, pady=10)

        titles = [
            "👥 Users",
            "💰 Income",
            "💸 Expense",
            "💵 Balance"
        ]

        for i, value in enumerate(stats):

            card = tk.Frame(
                stats_frame,
                bg="#ECEFF1",
                relief="ridge",
                bd=2
            )

            card.pack(
                side="left",
                expand=True,
                fill="x",
                padx=8
            )

            tk.Label(
                card,
                text=titles[i],
                bg="#ECEFF1",
                font=("Arial",12,"bold")
            ).pack(pady=(10,5))

            if i == 0:
                text = str(value)
            else:
                text = f"₹ {value:,.2f}"

            tk.Label(
                card,
                text=text,
                bg="#ECEFF1",
                fg="#1565C0",
                font=("Arial",18,"bold")
            ).pack(pady=(0,10))

        search_frame = tk.Frame(self.root)
        search_frame.pack(pady=10)

        tk.Label(
            search_frame,
            text="Search User:",
            font=("Arial", 12, "bold")
        ).pack(side="left", padx=5)

        self.search_var = tk.StringVar()

        tk.Entry(
            search_frame,
            textvariable=self.search_var,
            width=35,
            font=("Arial", 11)
        ).pack(side="left", padx=5)

        tk.Button(
            search_frame,
            text="Search",
            width=12,
            command=self.search_user
        ).pack(side="left", padx=5)

        tk.Button(
            search_frame,
            text="Delete User",
            bg="#F44336",
            fg="white",
            width=15,
            command=self.delete_selected_user
        ).pack(side="left", padx=5)


        tk.Button(
            search_frame,
            text="View Details",
            bg="#3F51B5",
            fg="white",
            width=15,
            command=self.view_user
        ).pack(side="left", padx=5)

        tk.Button(
            search_frame,
            text="📄 Export Excel",
            bg="#4CAF50",
            fg="white",
            width=15,
            command=export_users_excel
        ).pack(side="left", padx=5)

        tk.Button(
            search_frame,
            text="📄 Export PDF",
            bg="#E53935",
            fg="white",
            width=15,
            font=("Arial", 10, "bold"),
            command=export_users_pdf
        ).pack(side="left", padx=5)
        
        tk.Button(
            search_frame,
            text="Show All",
            width=12,
            command=self.load_users
        ).pack(side="left", padx=5)

        columns = (
            "ID",
            "Name",
            "Username",
            "Email",
            "Created"
        )

        self.user_table = ttk.Treeview(
            self.root,
            columns=columns,
            show="headings"
        )

        for col in columns:
            self.user_table.heading(col, text=col)
            self.user_table.column(col, width=180)

        self.user_table.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.load_users()

    # ==========================================
    # Load Users
    # ==========================================

    def load_users(self):

        for row in self.user_table.get_children():
            self.user_table.delete(row)

        users = get_all_users()

        for user in users:
            self.user_table.insert("", "end", values=user)

    def search_user(self):

        keyword = self.search_var.get().strip()

        users = search_users(keyword)

        for row in self.user_table.get_children():
            self.user_table.delete(row)

        for user in users:
            self.user_table.insert("", "end", values=user)

    def delete_selected_user(self):

        selected = self.user_table.selection()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Please select a user."
            )
            return

        values = self.user_table.item(selected[0])["values"]

        user_id = values[0]

        name = values[1]

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Delete user '{name}'?\n\nThis will also delete all of their income, expenses, budget and related records."
        )

        if not confirm:
            return

        delete_user(user_id)

        messagebox.showinfo(
            "Success",
            "User deleted successfully."
        )

        self.load_users()

    def view_user(self):

        selected = self.user_table.selection()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Please select a user."
            )
            return

        values = self.user_table.item(selected[0])["values"]

        user_id = values[0]

        income, expense, balance = get_user_summary(user_id)

        info = f"""
    Name      : {values[1]}
    Username  : {values[2]}
    Email     : {values[3]}
    Created   : {values[4]}

    ----------------------------

    Total Income  : ₹ {income:,.2f}
    Total Expense : ₹ {expense:,.2f}
    Balance       : ₹ {balance:,.2f}
    """

        messagebox.showinfo(
            "User Details",
            info
        )
