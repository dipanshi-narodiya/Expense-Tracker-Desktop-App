# ==========================================
# Budget Window
# ==========================================

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

from utils.helper import save_budget


class BudgetWindow:

    def __init__(self, user):

        self.user = user

        self.root = tk.Toplevel()

        self.root.title("Set Monthly Budget")

        self.root.geometry("500x450")

        self.root.resizable(False, False)

        self.create_widgets()

    # ==========================================
    # Create Widgets
    # ==========================================

    def create_widgets(self):

        main = ttk.Frame(
            self.root,
            padding=30
        )

        main.pack(fill="both", expand=True)

        # --------------------------
        # Title
        # --------------------------

        ttk.Label(
            main,
            text="💰 Set Monthly Budget",
            font=("Arial", 22, "bold")
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(0, 30)
        )

        # --------------------------
        # Month
        # --------------------------

        ttk.Label(
            main,
            text="Month",
            font=("Arial", 11)
        ).grid(
            row=1,
            column=0,
            sticky="w",
            pady=10
        )

        self.month_var = tk.StringVar()

        self.month_combo = ttk.Combobox(
            main,
            textvariable=self.month_var,
            width=35,
            state="readonly"
        )

        self.month_combo["values"] = (
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        )

        self.month_combo.grid(
            row=1,
            column=1,
            padx=10
        )

        self.month_combo.set(datetime.now().strftime("%B"))

        # --------------------------
        # Year
        # --------------------------

        ttk.Label(
            main,
            text="Year",
            font=("Arial", 11)
        ).grid(
            row=2,
            column=0,
            sticky="w",
            pady=10
        )

        self.year_var = tk.StringVar()

        ttk.Entry(
            main,
            textvariable=self.year_var,
            width=38
        ).grid(
            row=2,
            column=1,
            padx=10
        )

        self.year_var.set(str(datetime.now().year))

        # --------------------------
        # Budget Amount
        # --------------------------

        ttk.Label(
            main,
            text="Budget (₹)",
            font=("Arial", 11)
        ).grid(
            row=3,
            column=0,
            sticky="w",
            pady=10
        )

        self.amount_var = tk.StringVar()

        ttk.Entry(
            main,
            textvariable=self.amount_var,
            width=38
        ).grid(
            row=3,
            column=1,
            padx=10
        )

        # --------------------------
        # Save Button
        # --------------------------

        tk.Button(
            main,
            text="💾 Save Budget",
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12, "bold"),
            width=20,
            height=2,
            cursor="hand2",
            command=self.save_budget_data
        ).grid(
            row=4,
            column=0,
            columnspan=2,
            pady=30
        )
    
    # ==========================================
    # Save Budget
    # ==========================================

    def save_budget_data(self):

        month = self.month_var.get().strip()
        year = self.year_var.get().strip()
        amount = self.amount_var.get().strip()

        # -------------------------
        # Validation
        # -------------------------

        if month == "" or year == "" or amount == "":
            messagebox.showerror(
                "Error",
                "Please fill all fields."
            )
            return

        try:

            year = int(year)
            amount = float(amount)

            if amount <= 0:
                raise ValueError

        except ValueError:

            messagebox.showerror(
                "Invalid Data",
                "Please enter a valid year and budget amount."
            )
            return

        # -------------------------
        # Save Budget
        # -------------------------

        save_budget(
            self.user[0],
            month,
            year,
            amount
        )

        messagebox.showinfo(
            "Success",
            "Budget saved successfully!"
        )

        self.root.destroy()