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

        # ==========================================
        # Root Background
        # ==========================================

        self.root.configure(bg="#EEF2FF")

        # ==========================================
        # Main Container
        # ==========================================

        container = tk.Frame(
            self.root,
            bg="#EEF2FF"
        )

        container.pack(
            fill="both",
            expand=True
        )

        # ==========================================
        # Header
        # ==========================================

        header = tk.Frame(
            container,
            bg="#2563EB",
            height=70
        )

        header.pack(fill="x")

        header.pack_propagate(False)

        tk.Label(
            header,
            text="📊 Analytics Dashboard",
            font=("Segoe UI",24,"bold"),
            bg="#2563EB",
            fg="white"
        ).pack(
            pady=18
        )

        # ==========================================
        # Main White Card
        # ==========================================

        self.card = tk.Frame(
            container,
            bg="white",
            bd=0,
            highlightbackground="#D1D5DB",
            highlightthickness=1
        )

        self.card.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        tk.Label(
            self.card,
            text="Financial Analytics",
            font=("Segoe UI",20,"bold"),
            bg="white",
            fg="#111827"
        ).pack(
            pady=(10,15)
        )

        # ==========================================
        # Summary Cards
        # ==========================================

        summary_frame = tk.Frame(
            self.card,
            bg="white"
        )

        summary_frame.pack(
            fill="x",
            padx=20,
            pady=(0,20)
        )

        cards = [

            ("💰 Income", get_total_income(self.user[0]), "#22C55E"),

            ("💸 Expense", get_total_expense(self.user[0]), "#EF4444"),

            ("💵 Balance", get_balance(self.user[0]), "#2563EB"),

            ("🎯 Budget", get_budget(self.user[0]), "#F59E0B")

        ]

        for index, (title, value, color) in enumerate(cards):

            card = tk.Frame(
                summary_frame,
                bg="white",
                bd=1,
                relief="solid",
                highlightbackground="#D1D5DB",
                highlightthickness=1
            )

            card.pack(
                side="left",
                expand=True,
                fill="both",
                padx=8
            )

            # Colored Top Bar

            tk.Frame(
                card,
                bg=color,
                height=6
            ).pack(fill="x")

            tk.Label(
                card,
                text=title,
                font=("Segoe UI",11,"bold"),
                bg="white",
                fg="#374151"
            ).pack(
                pady=(8,2)
            )

            tk.Label(
                card,
                text=f"₹ {value:,.2f}",
                font=("Segoe UI",16,"bold"),
                bg="white",
                fg=color
            ).pack(
                pady=(0,8)
            )

        # ==========================================
        # Action Buttons
        # ==========================================

        button_frame = tk.Frame(
            self.card,
            bg="white"
        )

        button_frame.pack(
            pady=(5,10)
        )

        # Refresh Button

        tk.Button(
            button_frame,
            text="🔄 Refresh",
            bg="#2563EB",
            fg="white",
            activebackground="#1D4ED8",
            activeforeground="white",
            font=("Segoe UI",11,"bold"),
            relief="flat",
            cursor="hand2",
            width=16,
            command=self.refresh_dashboard
        ).grid(
            row=0,
            column=0,
            padx=10
        )

        # Export Button

        tk.Button(
            button_frame,
            text="📷 Export",
            bg="#22C55E",
            fg="white",
            activebackground="#16A34A",
            activeforeground="white",
            font=("Segoe UI",11,"bold"),
            relief="flat",
            cursor="hand2",
            width=16,
            command=self.export_chart
        ).grid(
            row=0,
            column=1,
            padx=10
        )

        # Top Categories Button

        tk.Button(
            button_frame,
            text="🏆 Top Categories",
            bg="#9333EA",
            fg="white",
            activebackground="#7E22CE",
            activeforeground="white",
            font=("Segoe UI",11,"bold"),
            relief="flat",
            cursor="hand2",
            width=18,
            command=self.show_top_categories
        ).grid(
            row=0,
            column=2,
            padx=10
        )

        # ==========================================
        # Charts Section
        # ==========================================

        charts_container = tk.LabelFrame(
            self.card,
            text=" 📈 Charts & Insights ",
            bg="white",
            fg="#111827",
            font=("Segoe UI",12,"bold"),
            padx=10,
            pady=10,
            height=650
        )

        charts_container.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(5,20)
        )

        charts_container.pack_propagate(False)
        self.charts_frame = tk.Frame(
            charts_container,
            bg="white"
        )

        self.charts_frame.pack(
            fill="both",
            expand=True
        )

        # -----------------------------
        # Top Charts
        # -----------------------------

        top_frame = tk.Frame(
            self.charts_frame,
            bg="white"
        )

        top_frame.pack(
            fill="both",
            expand=True,
            pady=5
        )

        # -----------------------------
        # Bottom Charts
        # -----------------------------

        bottom_frame = tk.Frame(
            self.charts_frame,
            bg="white"
        )

        bottom_frame.pack(
            fill="both",
            expand=True,
            pady=5
        )

        # ==========================================
        # Load Charts
        # ==========================================

        left_chart = tk.Frame(
            top_frame,
            bg="white"
        )

        left_chart.pack(
            side="left",
            fill="both",
            expand=True,
            padx=10
        )

        right_chart = tk.Frame(
            top_frame,
            bg="white"
        )

        right_chart.pack(
            side="left",
            fill="both",
            expand=True,
            padx=10
        )

        self.show_pie_chart(left_chart)
        self.show_bar_chart(right_chart)

        savings_frame = tk.Frame(
            bottom_frame,
            bg="white"
        )

        savings_frame.pack(
            fill="both",
            expand=True
        )

        self.show_savings_chart(savings_frame)

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

        fig = plt.Figure(figsize=(13 , 3.8), dpi=100)

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

        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, parent)

        canvas.draw()

        canvas.get_tk_widget().pack(
            side="left",
            expand=True,
            padx=10,
            pady=10
        )
    # ================================
    # Expense Pie Chart
    # ==========================================

    def show_pie_chart(self, parent):

        data = get_expense_by_category(self.user[0])

        if not data:
            return

        labels = [row[0] for row in data]
        values = [row[1] for row in data]

        fig = plt.Figure(figsize=(8,5.5), dpi=100)

        ax = fig.add_subplot(111)

        ax.pie(
            values,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90,
            textprops={"fontsize":9}
        )

        ax.set_title(
            "Expense By Category",
            fontsize=12,
            pad=20
        )

        ax.axis("equal")

        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, parent)
        canvas.draw()

        canvas.get_tk_widget().pack(
            fill="both",
            expand=True
        )
    
    # ==========================================
    # Monthly Income vs Expense
    # ==========================================

    def show_bar_chart(self, parent):

        months, income, expense = get_monthly_summary(self.user[0])

        if not months:
            return

        fig = plt.Figure(figsize=(7, 4.8), dpi=100)
        ax = fig.add_subplot(111)

        x = range(len(months))

        # Income Bars
        ax.bar(
            [i - 0.2 for i in x],
            income,
            width=0.4,
            label="Income"
        )

        # Expense Bars
        ax.bar(
            [i + 0.2 for i in x],
            expense,
            width=0.4,
            label="Expense"
        )

        # X Axis
        ax.set_xticks(list(x))
        ax.set_xticklabels(
            months,
            rotation=25,
            ha="right",
            fontsize=9
        )

        # Labels
        ax.set_ylabel("Amount (₹)")
        ax.set_xlabel("Month")

        # Title
        ax.set_title(
            "Monthly Income vs Expense",
            fontsize=14,
            fontweight="bold",
            pad=15
        )

        # Grid
        ax.grid(axis="y", linestyle="--", alpha=0.5)

        # Legend
        ax.legend(loc="upper right")

        # Prevent graph from being cut
        fig.subplots_adjust(
            left=0.12,
            right=0.97,
            top=0.90,
            bottom=0.22
        )

        canvas = FigureCanvasTkAgg(fig, parent)
        canvas.draw()

        canvas.get_tk_widget().pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
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