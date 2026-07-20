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

        # self.root.geometry("zoomed")
        self.root.state("zoomed")

        # self.root.resizable(False, False)

        self.create_widgets()

        self.root.mainloop()

    # ==========================================
    # Create Widgets
    # ==========================================

    def create_widgets(self):

        self.main_frame = ttk.Frame(
            self.root,
            padding=20
        )

        self.main_frame.pack(
            fill="both",
            expand=True
        )

        # ------------------------------
        # Title
        # ------------------------------

        title = ttk.Label(
            self.main_frame,
            text="💰 Expense Tracker",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=(5, 10))

        # ------------------------------
        # Header
        # ------------------------------

        header = ttk.Frame(self.main_frame)

        header.pack(fill="x", pady=(0, 20))

        ttk.Label(
            header,
            text=f"👋 Welcome, {self.user[1]}",
            font=("Arial", 18, "bold")
        ).pack(side="left")

        self.clock_label = ttk.Label(
            header,
            font=("Arial", 12)
        )

        self.clock_label.pack(side="right")

        self.update_clock()

        # ==========================================
        # Summary Cards
        # ==========================================

        self.summary_frame = ttk.Frame(self.main_frame)
        self.summary_frame.pack(pady=20)

        # ------------------------------
        # Balance Card
        # ------------------------------

        balance_frame = tk.Frame(
            self.summary_frame,
            bg="#4CAF50",
            padx=20,
            pady=18,
            relief="ridge",
            bd=2
        )

        balance_frame.grid(row=0, column=0, padx=8)

        tk.Label(
            balance_frame,
            text="💰 Total Balance",
            bg="#4CAF50",
            fg="white",
            font=("Arial", 15, "bold")
        ).pack()

        self.balance_label = tk.Label(
            balance_frame,
            text="₹ 0.00",
            bg="#4CAF50",
            fg="white",
            font=("Arial", 22, "bold")
        )

        self.balance_label.pack(pady=(12, 0))

        # ------------------------------
        # Income Card
        # ------------------------------

        income_frame = tk.Frame(
            self.summary_frame,
            bg="#2196F3",
            padx=20,
            pady=18,
            relief="ridge",
            bd=2
        )

        income_frame.grid(row=0, column=1, padx=15)

        tk.Label(
            income_frame,
            text="📈 Total Income",
            bg="#2196F3",
            fg="white",
            font=("Arial", 15, "bold")
        ).pack()

        self.income_label = tk.Label(
            income_frame,
            text="₹ 0.00",
            bg="#2196F3",
            fg="white",
            font=("Arial", 22, "bold")
        )

        self.income_label.pack(pady=(12, 0))

        # ------------------------------
        # Expense Card
        # ------------------------------

        expense_frame = tk.Frame(
            self.summary_frame,
            bg="#F44336",
            padx=20,
            pady=18,
            relief="ridge",
            bd=2
        )

        expense_frame.grid(row=0, column=2, padx=8)

        tk.Label(
            expense_frame,
            text="📉 Total Expense",
            bg="#F44336",
            fg="white",
            font=("Arial", 15, "bold")
        ).pack()

        self.expense_label = tk.Label(
            expense_frame,
            text="₹ 0.00",
            bg="#F44336",
            fg="white",
            font=("Arial", 22, "bold")
        )

        self.expense_label.pack(pady=(12, 0))


        # ==========================
        # Budget Card
        # ==========================

        budget_frame = tk.Frame(
            self.summary_frame,
            bg="#FF9800",
            padx=20,
            pady=18,
            relief="ridge",
            bd=2
        )

        budget_frame.grid(row=0, column=3, padx=8)

        tk.Label(
            budget_frame,
            text="💰 Monthly Budget",
            bg="#FF9800",
            fg="white",
            font=("Arial",16,"bold")
        ).pack()

        self.budget_label = tk.Label(
            budget_frame,
            text="₹ 0.00",
            bg="#FF9800",
            fg="white",
            font=("Arial",24,"bold")
        )

        self.budget_label.pack(pady=(15,0))


        # ==========================
        # Remaining Budget Card
        # ==========================

        remaining_frame = tk.Frame(
            self.summary_frame,
            bg="#009688",
            padx=20,
            pady=18,
            relief="ridge",
            bd=2
        )

        remaining_frame.grid(row=0, column=4, padx=8)

        tk.Label(
            remaining_frame,
            text="🟢 Remaining Budget",
            bg="#009688",
            fg="white",
            font=("Arial",16,"bold")
        ).pack()

        self.remaining_label = tk.Label(
            remaining_frame,
            text="₹ 0.00",
            bg="#009688",
            fg="white",
            font=("Arial",24,"bold")
        )

        self.remaining_label.pack(pady=(15,0))

        # ==========================================
        # Action Buttons
        # ==========================================

        self.button_frame = ttk.Frame(self.main_frame)

        self.button_frame.pack(pady=(20,30))

        # ------------------------------
        # Add Income
        # ------------------------------

        tk.Button(
            self.button_frame,
            text="➕ Add Income",
            bg="#4CAF50",
            fg="white",
            font=("Arial", 11, "bold"),
            width=14,
            height=2,
            cursor="hand2",
            command=self.open_income
        ).grid(row=0, column=0, padx=10)

        # ------------------------------
        # Add Expense
        # ------------------------------

        tk.Button(
            self.button_frame,
            text="💸 Add Expense",
            bg="#F44336",
            fg="white",
            font=("Arial", 11, "bold"),
            width=14,
            height=2,
            cursor="hand2",
            command=self.open_expense
        ).grid(row=0, column=1, padx=10)

        # ------------------------------
        # Reports
        # ------------------------------

        tk.Button(
            self.button_frame,
            text="📊 Reports",
            bg="#2196F3",
            fg="white",
            font=("Arial", 11, "bold"),
            width=14,
            height=2,
            cursor="hand2",
            command=self.open_reports
        ).grid(row=0, column=2, padx=10)

        # ------------------------------
        # Analytics
        # ------------------------------

        tk.Button(
            self.button_frame,
            text="📊 Analytics",
            bg="#9C27B0",
            fg="white",
            font=("Arial", 11, "bold"),
            width=14,
            height=2,
            cursor="hand2",
            command=self.open_analytics
        ).grid(row=0, column=3, padx=10)

        # ------------------------------
        # Budget
        # ------------------------------

        tk.Button(
            self.button_frame,
            text="💰 Budget",
            bg="#FF9800",
            fg="white",
            font=("Arial", 11, "bold"),
            width=14,
            height=2,
            cursor="hand2",
            command=self.open_budget
        ).grid(row=0, column=4, padx=10)
        
        # ------------------------------
        # Logout
        # ------------------------------

        tk.Button(
            self.button_frame,
            text="🚪 Logout",
            bg="#555555",
            fg="white",
            font=("Arial", 11, "bold"),
            width=14,
            height=2,
            cursor="hand2",
            command=self.logout
        ).grid(row=0, column=5, padx=10)

        tk.Button(
            self.button_frame,
            text="⚙ Settings",
            bg="#607D8B",
            fg="white",
            font=("Arial",11,"bold"),
            width=14,
            height=2,
            command=self.open_settings
        ).grid(row=1, column=2, padx=10, pady=10)

        # ==========================================
        # Recent Transactions
        # ==========================================

        recent_frame = ttk.LabelFrame(
            self.main_frame,
            text="📋 Recent Transactions",
            padding=10
        )

        recent_frame.pack(
            fill="x",
            pady=(20, 0)
        )

        # ------------------------------
        # Transaction Table
        # ------------------------------

        self.transaction_table = ttk.Treeview(
            recent_frame,
            columns=(
                "Date",
                "Type",
                "Category",
                "Amount"
            ),
            show="headings",
            height=6
        )

        self.transaction_table.heading("Date", text="Date")
        self.transaction_table.heading("Type", text="Type")
        self.transaction_table.heading("Category", text="Category / Source")
        self.transaction_table.heading("Amount", text="Amount")

        self.transaction_table.column(
            "Date",
            width=150,
            anchor="center"
        )

        self.transaction_table.column(
            "Type",
            width=120,
            anchor="center"
        )

        self.transaction_table.column(
            "Category",
            width=450
        )

        self.transaction_table.column(
            "Amount",
            width=180,
            anchor="e"
        )

        scrollbar = ttk.Scrollbar(
            recent_frame,
            orient="vertical",
            command=self.transaction_table.yview
        )

        self.transaction_table.configure(
            yscrollcommand=scrollbar.set
        )

        self.transaction_table.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        # Load transactions
        self.load_recent_transactions()
        
        self.load_summary()
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

        if budget > 0:

            if remaining < 0:

                messagebox.showwarning(
                    "Budget Exceeded",
                    f"You have exceeded your monthly budget by ₹ {abs(remaining):,.2f}"
                )    

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