import tkinter as tk
from tkinter import ttk, filedialog, messagebox

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from utils.helper import (
    get_expense_by_category,
    get_monthly_summary,
    get_total_income,
    get_total_expense,
    get_balance,
    get_budget,
    get_financial_insights
)


class AnalyticsWindow:

    def __init__(self, user):

        self.user = user

        self.root = tk.Toplevel()

        self.root.title("Expense Tracker Analytics")

        self.root.geometry("1400x800")

        self.root.state("zoomed")

        self.create_widgets()

    # ==========================================
    # Create Widgets
    # ==========================================

    def create_widgets(self):

        title = tk.Label(
            self.root,
            text="📊 Expense Tracker Analytics",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=15)

        # -----------------------------
        # Summary Cards
        # -----------------------------

        summary_frame = tk.Frame(self.root)

        summary_frame.pack(fill="x", padx=20)

        cards = [

            ("💰 Income", get_total_income(self.user[0])),

            ("💸 Expense", get_total_expense(self.user[0])),

            ("💵 Balance", get_balance(self.user[0])),

            ("🎯 Budget", get_budget(self.user[0]))

        ]

        for title, value in cards:

            card = tk.Frame(

                summary_frame,

                bg="#F5F5F5",

                relief="ridge",

                bd=2

            )

            card.pack(

                side="left",

                expand=True,

                fill="x",

                padx=8,

                pady=5

            )

            tk.Label(

                card,

                text=title,

                bg="#F5F5F5",

                font=("Arial",12,"bold")

            ).pack(pady=(10,5))

            tk.Label(

                card,

                text=f"₹ {value:,.2f}",

                bg="#F5F5F5",

                fg="#2E7D32",

                font=("Arial",18,"bold")

            ).pack(pady=(0,10))

        # -----------------------------
        # Buttons
        # -----------------------------

        button_frame = tk.Frame(self.root)

        button_frame.pack(pady=15)

        tk.Button(

            button_frame,

            text="🔄 Refresh",

            bg="#2196F3",

            fg="white",

            width=18,

            font=("Arial",11,"bold"),

            command=self.refresh_dashboard

        ).pack(side="left", padx=10)

        tk.Button(

            button_frame,

            text="📷 Export",

            bg="#4CAF50",

            fg="white",

            width=18,

            font=("Arial",11,"bold"),

            command=self.export_chart

        ).pack(side="left", padx=10)

        tk.Button(
            button_frame,
            text="🏆 Top Categories",
            bg="#9C27B0",
            fg="white",
            width=18,
            font=("Arial",11,"bold"),
            command=self.show_top_categories
        ).pack(side="left", padx=10)
        # -----------------------------
        # Charts Frame
        # -----------------------------

        self.charts_frame = tk.Frame(self.root)

        self.charts_frame.pack(

            fill="both",

            expand=True,

            pady=15

        )

        top_frame = tk.Frame(self.charts_frame)
        top_frame.pack()

        bottom_frame = tk.Frame(self.charts_frame)
        bottom_frame.pack()

        self.show_pie_chart(top_frame)

        self.show_bar_chart(top_frame)

        self.show_savings_chart(bottom_frame)

        self.show_insights()
    # ==========================================
    # Monthly Savings Line Chart
    # ==========================================

    def show_savings_chart(self, parent):

        months, income, expense = get_monthly_summary(self.user[0])

        if len(months) == 0:
            return

        savings = []

        for i in range(len(months)):
            savings.append(income[i] - expense[i])

        fig = plt.Figure(figsize=(6, 4), dpi=100)

        ax = fig.add_subplot(111)

        ax.plot(
            months,
            savings,
            marker="o",
            linewidth=3
        )

        ax.set_title("Monthly Savings")

        ax.set_ylabel("Amount (₹)")

        ax.grid(True)

        canvas = FigureCanvasTkAgg(fig, parent)

        canvas.draw()

        canvas.get_tk_widget().pack(
            side="left",
            padx=20,
            pady=20
        )
    # ==========================================
    # Expense Pie Chart
    # ==========================================

    def show_pie_chart(self, parent):

        data = get_expense_by_category(self.user[0])

        if not data:
            return

        labels = [row[0] for row in data]
        values = [row[1] for row in data]

        fig = plt.Figure(figsize=(5,4), dpi=100)

        ax = fig.add_subplot(111)

        ax.pie(
            values,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90,
            shadow=True
        )

        ax.axis("equal")

        ax.set_title("Expense By Category")

        canvas = FigureCanvasTkAgg(fig, parent)

        canvas.draw()

        canvas.get_tk_widget().pack(
            side="left",
            padx=20,
            pady=20
        )    
    
    # ==========================================
    # Monthly Income vs Expense
    # ==========================================

    def show_bar_chart(self, parent):

        months, income, expense = get_monthly_summary(self.user[0])

        if not months:
            return

        fig = plt.Figure(figsize=(6,4), dpi=100)

        ax = fig.add_subplot(111)

        x = range(len(months))

        ax.bar(
            [i-0.2 for i in x],
            income,
            width=0.4,
            label="Income"
        )

        ax.bar(
            [i+0.2 for i in x],
            expense,
            width=0.4,
            label="Expense"
        )

        ax.set_xticks(list(x))

        ax.set_xticklabels(months)

        ax.set_ylabel("Amount (₹)")

        ax.set_title("Monthly Income vs Expense")

        ax.grid(axis="y")

        ax.legend()

        canvas = FigureCanvasTkAgg(fig, parent)

        canvas.draw()

        canvas.get_tk_widget().pack(
            side="left",
            padx=20,
            pady=20
        )

    # ==========================================
    # Refresh Dashboard
    # ==========================================

    def refresh_dashboard(self):

        self.root.destroy()

        AnalyticsWindow(self.user)

    # ==========================================
    # Export Charts
    # ==========================================

    def export_chart(self):

        messagebox.showinfo(
            "Coming Soon",
            "Export feature will be added in the next version."
        )   

    # ==========================================
    # Smart Financial Insights
    # ==========================================

    def show_insights(self):

        frame = tk.LabelFrame(
            self.root,
            text="🤖 Smart Financial Insights",
            font=("Arial", 12, "bold"),
            padx=10,
            pady=10
        )

        frame.pack(
            fill="x",
            padx=20,
            pady=15
        )

        insights = get_financial_insights(self.user[0])

        for text in insights:

            tk.Label(
                frame,
                text=text,
                anchor="w",
                justify="left",
                font=("Arial", 11)
            ).pack(
                anchor="w",
                pady=3
            )

    # ==========================================
    # Top Categories
    # ==========================================

    def show_top_categories(self):

        data = get_expense_by_category(self.user[0])

        if not data:
            messagebox.showinfo(
                "No Data",
                "No expense records found."
            )
            return

        window = tk.Toplevel(self.root)

        window.title("Top Expense Categories")

        window.geometry("500x400")

        ttk.Label(
            window,
            text="🏆 Top Expense Categories",
            font=("Arial",18,"bold")
        ).pack(pady=15)

        tree = ttk.Treeview(
            window,
            columns=("Category","Amount"),
            show="headings"
        )

        tree.heading("Category", text="Category")
        tree.heading("Amount", text="Amount (₹)")

        tree.column("Category", width=220)
        tree.column("Amount", width=150)

        tree.pack(fill="both", expand=True, padx=20, pady=15)

        data.sort(key=lambda x: x[1], reverse=True)

        for row in data:
            tree.insert("", "end", values=row)