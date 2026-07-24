# ==========================================
# Expense Tracker - Dashboard
# ==========================================

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from ui.analytics import AnalyticsWindow

from utils.helper import (
    get_total_income,
    get_total_expense,
    get_balance,
    get_recent_transactions,
    get_budget,
    get_remaining_budget
)

class DashboardWindow:

    def __init__(self, user):

        self.user = user

        self.root = tk.Tk()

        self.root.title("Expense Tracker - Dashboard")
        self.root.configure(bg="#EEF2FF")
        # self.root.geometry("zoomed")
        self.root.state("zoomed")

        # self.root.resizable(False, False)

        self.create_widgets()

        self.root.mainloop()

    # ==========================================
    # Create Widgets
    # ==========================================

    def create_widgets(self):

        # ===============================
        # Root Background
        # ===============================

        self.root.configure(bg="#EEF2FF")

        # ===============================
        # Header
        # ===============================

        header = tk.Frame(
            self.root,
            bg="#2563EB",
            height=90
        )

        header.pack(fill="x")
        header.pack_propagate(False)

        # -------------------------------
        # Left Side
        # -------------------------------

        left_header = tk.Frame(
            header,
            bg="#2563EB"
        )

        left_header.pack(
            side="left",
            padx=30,
            pady=10
        )

        tk.Label(
            left_header,
            text="💰 Expense Tracker",
            font=("Segoe UI",30,"bold"),
            fg="white",
            bg="#2563EB"
        ).pack(anchor="w")

        tk.Label(
            left_header,
            text="Manage your personal finances with ease",
            font=("Segoe UI",11),
            fg="white",
            bg="#2563EB"
        ).pack(anchor="w")

        # -------------------------------
        # Right Side
        # -------------------------------

        right_header = tk.Frame(
            header,
            bg="#2563EB"
        )

        right_header.pack(
            side="right",
            padx=30,
            pady=10
        )

        self.clock_label = tk.Label(
            right_header,
            text="",
            font=("Segoe UI",11),
            fg="white",
            bg="#2563EB"
        )

        self.clock_label.pack(anchor="e")

        tk.Label(
            right_header,
            text=f"👤 Welcome, {self.user[1]}",
            font=("Segoe UI",13,"bold"),
            fg="white",
            bg="#2563EB"
        ).pack(anchor="e", pady=3)

        tk.Button(
            right_header,
            text="Logout",
            bg="#EF4444",
            fg="white",
            activebackground="#DC2626",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            font=("Segoe UI",10,"bold"),
            padx=20,
            command=self.logout
        ).pack(anchor="e", pady=5)

        # ===============================
        # Main Container
        # ===============================

        self.main_container = tk.Frame(
            self.root,
            bg="#EEF2FF"
        )

        self.main_container.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=20
        )

        # ===============================
        # Summary Cards Frame
        # ===============================

        self.cards_frame = tk.Frame(
            self.main_container,
            bg="#EEF2FF"
        )

        self.cards_frame.pack(
            fill="x",
            pady=(0,20)
        )

        # ==========================================
        # CARD 1 - BALANCE
        # ==========================================

        self.balance_card = tk.Frame(
            self.cards_frame,
            bg="white",
            bd=0,
            highlightbackground="#E5E7EB",
            highlightthickness=1
        )

        self.balance_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=8
        )

        tk.Label(
            self.balance_card,
            text="💚 Balance",
            font=("Segoe UI",14,"bold"),
            fg="#16A34A",
            bg="white"
        ).pack(anchor="w", padx=20, pady=(18,5))

        self.balance_label = tk.Label(
            self.balance_card,
            text="₹ 0.00",
            font=("Segoe UI",28,"bold"),
            fg="#111827",
            bg="white"
        )

        self.balance_label.pack(anchor="w", padx=20)

        tk.Label(
            self.balance_card,
            text="Current Balance",
            font=("Segoe UI",10),
            fg="#6B7280",
            bg="white"
        ).pack(anchor="w", padx=20, pady=(0,18))


        # ==========================================
        # CARD 2 - INCOME
        # ==========================================

        self.income_card = tk.Frame(
            self.cards_frame,
            bg="white",
            bd=0,
            highlightbackground="#E5E7EB",
            highlightthickness=1
        )

        self.income_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=8
        )

        tk.Label(
            self.income_card,
            text="💵 Income",
            font=("Segoe UI",14,"bold"),
            fg="#2563EB",
            bg="white"
        ).pack(anchor="w", padx=20, pady=(18,5))

        self.income_label = tk.Label(
            self.income_card,
            text="₹ 0.00",
            font=("Segoe UI",28,"bold"),
            fg="#111827",
            bg="white"
        )

        self.income_label.pack(anchor="w", padx=20)

        tk.Label(
            self.income_card,
            text="Total Income",
            font=("Segoe UI",10),
            fg="#6B7280",
            bg="white"
        ).pack(anchor="w", padx=20, pady=(0,18))


        # ==========================================
        # CARD 3 - EXPENSE
        # ==========================================

        self.expense_card = tk.Frame(
            self.cards_frame,
            bg="white",
            bd=0,
            highlightbackground="#E5E7EB",
            highlightthickness=1
        )

        self.expense_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=8
        )

        tk.Label(
            self.expense_card,
            text="💸 Expense",
            font=("Segoe UI",14,"bold"),
            fg="#EF4444",
            bg="white"
        ).pack(anchor="w", padx=20, pady=(18,5))

        self.expense_label = tk.Label(
            self.expense_card,
            text="₹ 0.00",
            font=("Segoe UI",28,"bold"),
            fg="#111827",
            bg="white"
        )

        self.expense_label.pack(anchor="w", padx=20)

        tk.Label(
            self.expense_card,
            text="Total Expense",
            font=("Segoe UI",10),
            fg="#6B7280",
            bg="white"
        ).pack(anchor="w", padx=20, pady=(0,18))


        # ==========================================
        # CARD 4 - BUDGET
        # ==========================================

        self.budget_card = tk.Frame(
            self.cards_frame,
            bg="white",
            bd=0,
            highlightbackground="#E5E7EB",
            highlightthickness=1
        )

        self.budget_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=8
        )

        tk.Label(
            self.budget_card,
            text="🎯 Budget",
            font=("Segoe UI",14,"bold"),
            fg="#F59E0B",
            bg="white"
        ).pack(anchor="w", padx=20, pady=(18,5))

        self.budget_label = tk.Label(
            self.budget_card,
            text="₹ 0.00",
            font=("Segoe UI",28,"bold"),
            fg="#111827",
            bg="white"
        )

        self.budget_label.pack(anchor="w", padx=20)

        tk.Label(
            self.budget_card,
            text="Monthly Budget",
            font=("Segoe UI",10),
            fg="#6B7280",
            bg="white"
        ).pack(anchor="w", padx=20, pady=(0,18))


        # ==========================================
        # CARD 5 - REMAINING
        # ==========================================

        self.remaining_card = tk.Frame(
            self.cards_frame,
            bg="white",
            bd=0,
            highlightbackground="#E5E7EB",
            highlightthickness=1
        )

        self.remaining_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=8
        )

        tk.Label(
            self.remaining_card,
            text="🟣 Remaining",
            font=("Segoe UI",14,"bold"),
            fg="#8B5CF6",
            bg="white"
        ).pack(anchor="w", padx=20, pady=(18,5))

        self.remaining_label = tk.Label(
            self.remaining_card,
            text="₹ 0.00",
            font=("Segoe UI",28,"bold"),
            fg="#111827",
            bg="white"
        )

        self.remaining_label.pack(anchor="w", padx=20)

        tk.Label(
            self.remaining_card,
            text="Budget Left",
            font=("Segoe UI",10),
            fg="#6B7280",
            bg="white"
        ).pack(anchor="w", padx=20, pady=(0,18))

        # ==========================================
        # Quick Actions
        # ==========================================

        self.button_frame = tk.Frame(
            self.main_container,
            bg="#EEF2FF"
        )

        self.button_frame.pack(
            fill="x",
            pady=(10,20)
        )

        # Row 1
        row1 = tk.Frame(
            self.button_frame,
            bg="#EEF2FF"
        )

        row1.pack()

        # Income Button

        tk.Button(
            row1,
            text="➕  Income",
            bg="#22C55E",
            fg="white",
            activebackground="#16A34A",
            activeforeground="white",
            relief="flat",
            font=("Segoe UI",11,"bold"),
            cursor="hand2",
            width=16,
            height=2,
            command=self.open_income
        ).pack(
            side="left",
            padx=8,
            pady=8
        )

        # Expense

        tk.Button(
            row1,
            text="➖  Expense",
            bg="#EF4444",
            fg="white",
            activebackground="#DC2626",
            activeforeground="white",
            relief="flat",
            font=("Segoe UI",11,"bold"),
            cursor="hand2",
            width=16,
            height=2,
            command=self.open_expense
        ).pack(
            side="left",
            padx=8,
            pady=8
        )

        # Reports

        tk.Button(
            row1,
            text="📄 Reports",
            bg="#2563EB",
            fg="white",
            activebackground="#1D4ED8",
            activeforeground="white",
            relief="flat",
            font=("Segoe UI",11,"bold"),
            cursor="hand2",
            width=16,
            height=2,
            command=self.open_reports
        ).pack(
            side="left",
            padx=8,
            pady=8
        )

        # Analytics

        tk.Button(
            row1,
            text="📊 Analytics",
            bg="#8B5CF6",
            fg="white",
            activebackground="#7C3AED",
            activeforeground="white",
            relief="flat",
            font=("Segoe UI",11,"bold"),
            cursor="hand2",
            width=16,
            height=2,
            command=self.open_analytics
        ).pack(
            side="left",
            padx=8,
            pady=8
        )

        # Budget

        tk.Button(
            row1,
            text="🎯 Budget",
            bg="#F59E0B",
            fg="white",
            activebackground="#D97706",
            activeforeground="white",
            relief="flat",
            font=("Segoe UI",11,"bold"),
            cursor="hand2",
            width=16,
            height=2,
            command=self.open_budget
        ).pack(
            side="left",
            padx=8,
            pady=8
        )

        # Row 2

        row2 = tk.Frame(
            self.button_frame,
            bg="#EEF2FF"
        )

        row2.pack()

        tk.Button(
            row2,
            text="⚙ Settings",
            bg="#64748B",
            fg="white",
            activebackground="#475569",
            activeforeground="white",
            relief="flat",
            font=("Segoe UI",11,"bold"),
            cursor="hand2",
            width=16,
            height=2,
            command=self.open_settings
        ).pack(
            side="left",
            padx=8,
            pady=8
        )

        tk.Button(
            row2,
            text="🚪 Logout",
            bg="#374151",
            fg="white",
            activebackground="#1F2937",
            activeforeground="white",
            relief="flat",
            font=("Segoe UI",11,"bold"),
            cursor="hand2",
            width=16,
            height=2,
            command=self.logout
        ).pack(
            side="left",
            padx=8,
            pady=8
        )

        # ==========================================
        # Recent Transactions Section
        # ==========================================

        transaction_container = tk.Frame(
            self.main_container,
            bg="#EEF2FF"
        )

        transaction_container.pack(
            fill="both",
            expand=True
        )

        # --------------------------
        # Title
        # --------------------------

        tk.Label(
            transaction_container,
            text="📋 Recent Transactions",
            bg="#EEF2FF",
            fg="#111827",
            font=("Segoe UI",18,"bold")
        ).pack(
            anchor="w",
            pady=(10,10)
        )

        # --------------------------
        # Table Frame
        # --------------------------

        table_frame = tk.Frame(
            transaction_container,
            bg="white",
            bd=0,
            highlightbackground="#E5E7EB",
            highlightthickness=1
        )

        table_frame.pack(
            fill="both",
            expand=True
        )

        # --------------------------
        # Scrollbar
        # --------------------------

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical"
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        # --------------------------
        # Treeview
        # --------------------------

        self.transaction_table = ttk.Treeview(
            table_frame,
            columns=(
                "Date",
                "Type",
                "Category",
                "Amount"
            ),
            show="headings",
            yscrollcommand=scrollbar.set,
            height=12
        )

        scrollbar.config(
            command=self.transaction_table.yview
        )

        self.transaction_table.heading(
            "Date",
            text="Date"
        )

        self.transaction_table.heading(
            "Type",
            text="Type"
        )

        self.transaction_table.heading(
            "Category",
            text="Category"
        )

        self.transaction_table.heading(
            "Amount",
            text="Amount"
        )

        self.transaction_table.column(
            "Date",
            width=140,
            anchor="center"
        )

        self.transaction_table.column(
            "Type",
            width=120,
            anchor="center"
        )

        self.transaction_table.column(
            "Category",
            width=220,
            anchor="center"
        )

        self.transaction_table.column(
            "Amount",
            width=150,
            anchor="center"
        )

        self.transaction_table.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # Load Existing Data

        self.load_summary()

        self.load_recent_transactions()

        # ==========================================
        # Alternate Row Colors
        # ==========================================

        self.transaction_table.tag_configure(
            "oddrow",
            background="#FFFFFF"
        )

        self.transaction_table.tag_configure(
            "evenrow",
            background="#F8FAFC"
        )

        # ==========================================
        # Hover Effect Function
        # ==========================================

        def on_enter(button, color):
            button.config(bg=color)

        def on_leave(button, color):
            button.config(bg=color)

        # ==========================================
        # Apply Hover Effects
        # ==========================================

        buttons = []

        for widget in self.button_frame.winfo_children():

            if isinstance(widget, tk.Frame):

                for btn in widget.winfo_children():

                    if isinstance(btn, tk.Button):

                        buttons.append(btn)

        hover_colors = {
            "#22C55E": "#16A34A",
            "#EF4444": "#DC2626",
            "#2563EB": "#1D4ED8",
            "#8B5CF6": "#7C3AED",
            "#F59E0B": "#D97706",
            "#64748B": "#475569",
            "#374151": "#1F2937"
        }

        for btn in buttons:

            normal = btn.cget("bg")

            hover = hover_colors.get(
                normal,
                normal
            )

            btn.bind(
                "<Enter>",
                lambda e, b=btn, c=hover: b.config(bg=c)
            )

            btn.bind(
                "<Leave>",
                lambda e, b=btn, c=normal: b.config(bg=c)
            )

        # ==========================================
        # Initial Refresh
        # ==========================================

        self.load_summary()

        self.load_recent_transactions()

        self.update_clock()
    # ==========================================
    # Live Clock
    # ==========================================

    def update_clock(self):

        current = datetime.now().strftime("%d %B %Y   %I:%M:%S %p")

        self.clock_label.config(text=current)

        self.root.after(1000, self.update_clock)


    # ==========================================
    # Load Summary
    # ==========================================

    def load_summary(self):

        if not self.user:
            return

        user_id = self.user[0]

        income = get_total_income(user_id)
        expense = get_total_expense(user_id)
        balance = get_balance(user_id)

        budget = get_budget(user_id)
        remaining = get_remaining_budget(user_id)

        self.balance_label.config(
            text=f"₹ {balance:,.2f}"
        )

        self.income_label.config(
            text=f"₹ {income:,.2f}"
        )

        self.expense_label.config(
            text=f"₹ {expense:,.2f}"
        )
        self.budget_label.config(
            text=f"₹ {budget:,.2f}"
        )

        self.remaining_label.config(
            text=f"₹ {remaining:,.2f}"
        )

        # ==========================
        # Budget Warning
        # ==========================

        # if budget > 0:

        #     if remaining < 0:

        #         messagebox.showwarning(
        #             "Budget Exceeded",
        #             f"You have exceeded your monthly budget by ₹ {abs(remaining):,.2f}"
        #         )    

    # ==========================================
    # Load Recent Transactions
    # ==========================================

    def load_recent_transactions(self):

        if not self.user:
            return

        for item in self.transaction_table.get_children():
            self.transaction_table.delete(item)

        rows = get_recent_transactions(self.user[0])

        for row in rows:

            date, category, amount, trans_type = row

            self.transaction_table.insert(
                "",
                "end",
                values=(
                    date,
                    trans_type,
                    category,
                    f"₹ {amount:,.2f}"
                )
            )


    # ==========================================
    # Open Income Window
    # ==========================================
    def open_income(self):

        print("Income button clicked")

        from ui.income import IncomeWindow

        IncomeWindow(self.user)

        self.load_summary()

        self.load_recent_transactions()


    # ==========================================
    # Open Expense Window
    # ==========================================

    def open_expense(self):

        print("Expense button clicked")

        from ui.expense import ExpenseWindow

        ExpenseWindow(self.user)

    

        self.load_summary()
        self.load_recent_transactions()


    # ==========================================
    # Open Reports
    # ==========================================

    def open_reports(self):

        from ui.reports import ReportsWindow

        ReportsWindow(self.user)

    # ==========================================
    # Open Analytics
    # ==========================================

    def open_analytics(self):

        AnalyticsWindow(self.user)
    # ==========================================
    # Open Budget Window
    # ==========================================

    def open_budget(self):

        from ui.budget import BudgetWindow

        BudgetWindow(self.user)

        self.load_summary()
    # ==========================================
    # Logout
    # ==========================================
    def logout(self):

        self.root.destroy()

        from ui.login import LoginWindow

        LoginWindow()

    def open_settings(self):

        from ui.settings import SettingsWindow

        SettingsWindow(self.user)

# ==========================================
# Run Dashboard
# ==========================================

if __name__ == "__main__":

    DashboardWindow((1, "Demo User"))
