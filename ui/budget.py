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

        self.root.geometry("900x850")

        self.root.resizable(False, False)

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
            bg="#F59E0B",
            height=70
        )

        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text="🎯 Monthly Budget",
            font=("Segoe UI",24,"bold"),
            bg="#F59E0B",
            fg="white"
        ).pack(pady=18)

        # ==========================================
        # White Card
        # ==========================================

        self.card = tk.Frame(
            container,
            bg="white",
            bd=0,
            highlightbackground="#D1D5DB",
            highlightthickness=1
        )

        self.card.pack(
            pady=30,
            padx=40,
            fill="both",
            expand=True
        )

        # ==========================================
        # Title
        # ==========================================

        tk.Label(
            self.card,
            text="Budget Details",
            font=("Segoe UI",20,"bold"),
            bg="white",
            fg="#111827"
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(25,30)
        )

            # ==========================================
        # Month
        # ==========================================

        tk.Label(
            self.card,
            text="📅 Month",
            font=("Segoe UI",11,"bold"),
            bg="white",
            fg="#374151"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=40,
            pady=12
        )

        self.month_var = tk.StringVar()

        self.month_combo = ttk.Combobox(
            self.card,
            textvariable=self.month_var,
            width=32,
            state="readonly",
            font=("Segoe UI",11)
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

        self.month_combo.set(datetime.now().strftime("%B"))

        self.month_combo.grid(
            row=1,
            column=1,
            padx=40,
            pady=12,
            sticky="ew"
        )

        # ==========================================
        # Year
        # ==========================================

        tk.Label(
            self.card,
            text="📆 Year",
            font=("Segoe UI",11,"bold"),
            bg="white",
            fg="#374151"
        ).grid(
            row=2,
            column=0,
            sticky="w",
            padx=40,
            pady=12
        )

        self.year_var = tk.StringVar()

        self.year_entry = ttk.Entry(
            self.card,
            textvariable=self.year_var,
            font=("Segoe UI",11),
            width=35
        )

        self.year_entry.grid(
            row=2,
            column=1,
            padx=40,
            pady=12,
            sticky="ew"
        )

        self.year_var.set(str(datetime.now().year))

        # ==========================================
        # Budget Amount
        # ==========================================

        tk.Label(
            self.card,
            text="💰 Budget Amount (₹)",
            font=("Segoe UI",11,"bold"),
            bg="white",
            fg="#374151"
        ).grid(
            row=3,
            column=0,
            sticky="w",
            padx=40,
            pady=12
        )

        self.amount_var = tk.StringVar()

        self.amount_entry = ttk.Entry(
            self.card,
            textvariable=self.amount_var,
            font=("Segoe UI",11),
            width=35
        )

        self.amount_entry.grid(
            row=3,
            column=1,
            padx=40,
            pady=12,
            sticky="ew"
        )

        # ==========================================
        # Save Budget Button
        # ==========================================

        self.save_button = tk.Button(
            self.card,
            text="💾 Save Budget",
            bg="#F59E0B",
            fg="white",
            activebackground="#D97706",
            activeforeground="white",
            font=("Segoe UI",12,"bold"),
            relief="flat",
            cursor="hand2",
            width=20,
            height=2,
            command=self.save_budget_data
        )

        self.save_button.grid(
            row=4,
            column=0,
            columnspan=2,
            pady=(30,25)
        )

        # ==========================================
        # Responsive Layout
        # ==========================================

        self.card.columnconfigure(0, weight=1)
        self.card.columnconfigure(1, weight=3)

        self.amount_entry.focus()
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