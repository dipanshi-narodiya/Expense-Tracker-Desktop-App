# ==========================================
# Expense Tracker - Add Income Window
# ==========================================

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from tkcalendar import DateEntry

from utils.helper import save_income


class IncomeWindow:

    def __init__(self, user):

        self.user = user

        self.root = tk.Toplevel()

        self.root.title("Expense Tracker - Add Income")

        self.root.geometry("650x550")

        self.root.resizable(False, False)

        # Make popup modal
        self.root.transient()
        self.root.grab_set()
        self.root.focus_force()

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

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)

        tk.Label(
            header,
            text="💵 Add Income",
            font=("Segoe UI",24,"bold"),
            bg="#2563EB",
            fg="white"
        ).pack(
            pady=18
        )

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
            text="Income Details",
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
        # Date
        # ==========================================

        tk.Label(
            self.card,
            text="📅 Date",
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

        self.date_picker = DateEntry(
            self.card,
            width=30,
            date_pattern="dd-mm-yyyy",
            font=("Segoe UI",11)
        )

        self.date_picker.grid(
            row=1,
            column=1,
            padx=40,
            pady=12,
            sticky="ew"
        )

        # ==========================================
        # Source
        # ==========================================

        tk.Label(
            self.card,
            text="💼 Source",
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

        self.source_var = tk.StringVar()

        self.source_combo = ttk.Combobox(
            self.card,
            textvariable=self.source_var,
            width=32,
            state="readonly",
            font=("Segoe UI",11)
        )

        self.source_combo["values"] = (
            "Salary",
            "Business",
            "Freelancing",
            "Bonus",
            "Gift",
            "Interest",
            "Other"
        )

        self.source_combo.current(0)

        self.source_combo.grid(
            row=2,
            column=1,
            padx=40,
            pady=12,
            sticky="ew"
        )

        # ==========================================
        # Amount
        # ==========================================

        tk.Label(
            self.card,
            text="💰 Amount (₹)",
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
        # Payment Mode
        # ==========================================

        tk.Label(
            self.card,
            text="💳 Payment Mode",
            font=("Segoe UI",11,"bold"),
            bg="white",
            fg="#374151"
        ).grid(
            row=4,
            column=0,
            sticky="w",
            padx=40,
            pady=12
        )

        self.payment_var = tk.StringVar()

        self.payment_combo = ttk.Combobox(
            self.card,
            textvariable=self.payment_var,
            width=32,
            state="readonly",
            font=("Segoe UI",11)
        )

        self.payment_combo["values"] = (
            "Cash",
            "UPI",
            "Credit Card",
            "Debit Card",
            "Net Banking"
        )

        self.payment_combo.current(0)

        self.payment_combo.grid(
            row=4,
            column=1,
            padx=40,
            pady=12,
            sticky="ew"
        )

        # ==========================================
        # Notes
        # ==========================================

        tk.Label(
            self.card,
            text="📝 Notes",
            font=("Segoe UI",11,"bold"),
            bg="white",
            fg="#374151"
        ).grid(
            row=5,
            column=0,
            sticky="nw",
            padx=40,
            pady=12
        )

        self.notes = tk.Text(
            self.card,
            width=35,
            height=6,
            font=("Segoe UI",11),
            relief="solid",
            bd=1,
            wrap="word"
        )

        self.notes.grid(
            row=5,
            column=1,
            padx=40,
            pady=12,
            sticky="ew"
        )

        # ==========================================
        # Save Button
        # ==========================================

        self.save_button = tk.Button(
            self.card,
            text="💾 Save Income",
            bg="#2563EB",
            fg="white",
            activebackground="#1D4ED8",
            activeforeground="white",
            font=("Segoe UI",12,"bold"),
            relief="flat",
            cursor="hand2",
            width=20,
            height=2,
            command=self.save_income
        )

        self.save_button.grid(
            row=6,
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
    # Save Income
    # ==========================================

    def save_income(self):

        # Get Values
        date = self.date_picker.get()
        source = self.source_var.get().strip()
        amount = self.amount_var.get().strip()

        payment_mode = self.payment_var.get().strip()

        notes = self.notes.get("1.0", "end").strip()

        # -----------------------------
        # Validation
        # -----------------------------

        if source == "" or amount == "" or payment_mode == "":
            messagebox.showerror(
                "Error",
                "Please fill all required fields."
            )
            return

        try:

            amount = float(amount)

            if amount <= 0:
                raise ValueError

        except ValueError:

            messagebox.showerror(
                "Invalid Amount",
                "Please enter a valid amount."
            )
            return

        # -----------------------------
        # Save into Database
        # -----------------------------

        save_income(
            self.user[0],
            date,
            source,
            amount,
            payment_mode,
            notes
        )

        messagebox.showinfo(
            "Success",
            "Income saved successfully!"
        )

        # -----------------------------
        # Reset Form
        # -----------------------------

        self.date_picker.set_date(datetime.today())

        self.source_combo.current(0)

        self.amount_var.set("")

        self.payment_combo.current(0)

        self.notes.delete("1.0", "end")

        self.amount_entry.focus()
        # Close Window
        self.root.destroy()


# ==========================================
# Run Only For Testing
# ==========================================

if __name__ == "__main__":

    root = tk.Tk()
    root.withdraw()

    dummy_user = (
        1,
        "Demo User"
    )

    IncomeWindow(dummy_user)

    root.mainloop()
    