# ==========================================
# Expense Tracker - Add Expense Window
# ==========================================

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from tkcalendar import DateEntry

from utils.helper import save_expense


class ExpenseWindow:

    def __init__(self, user):

        self.user = user

        self.root = tk.Toplevel()

        self.root.title("Expense Tracker - Add Expense")

        self.root.geometry("650x650")

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

        main = ttk.Frame(
            self.root,
            padding=30
        )

        main.pack(fill="both", expand=True)

        # ----------------------------------
        # Title
        # ----------------------------------

        ttk.Label(
            main,
            text="💸 Add Expense",
            font=("Arial", 22, "bold")
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(0, 30)
        )

        # ----------------------------------
        # Date
        # ----------------------------------

        ttk.Label(
            main,
            text="Date",
            font=("Arial", 11)
        ).grid(
            row=1,
            column=0,
            sticky="w",
            pady=10
        )

        self.date_picker = DateEntry(
            main,
            width=37,
            date_pattern="dd-mm-yyyy",
            font=("Arial", 10)
        )

        self.date_picker.grid(
            row=1,
            column=1,
            padx=10
        )

        # ----------------------------------
        # Category
        # ----------------------------------

        ttk.Label(
            main,
            text="Category",
            font=("Arial", 11)
        ).grid(
            row=2,
            column=0,
            sticky="w",
            pady=10
        )

        self.category_var = tk.StringVar()

        self.category_combo = ttk.Combobox(
            main,
            textvariable=self.category_var,
            width=37,
            state="readonly"
        )

        self.category_combo["values"] = (
            "Food",
            "Transport",
            "Shopping",
            "Bills",
            "Entertainment",
            "Medical",
            "Education",
            "Other"
        )

        # Default Category
        self.category_combo.current(0)

        self.category_combo.grid(
            row=2,
            column=1,
            padx=10
        )

                # ----------------------------------
        # Description
        # ----------------------------------

        ttk.Label(
            main,
            text="Description",
            font=("Arial", 11)
        ).grid(
            row=3,
            column=0,
            sticky="w",
            pady=10
        )

        self.description_var = tk.StringVar()

        ttk.Entry(
            main,
            textvariable=self.description_var,
            width=40
        ).grid(
            row=3,
            column=1,
            padx=10
        )

        # ----------------------------------
        # Amount
        # ----------------------------------

        ttk.Label(
            main,
            text="Amount (₹)",
            font=("Arial", 11)
        ).grid(
            row=4,
            column=0,
            sticky="w",
            pady=10
        )

        self.amount_var = tk.StringVar()

        self.amount_entry = ttk.Entry(
            main,
            textvariable=self.amount_var,
            width=40
        )

        self.amount_entry.grid(
            row=4,
            column=1,
            padx=10
        )

        # ----------------------------------
        # Payment Mode
        # ----------------------------------

        ttk.Label(
            main,
            text="Payment Mode",
            font=("Arial", 11)
        ).grid(
            row=5,
            column=0,
            sticky="w",
            pady=10
        )

        self.payment_var = tk.StringVar()

        self.payment_combo = ttk.Combobox(
            main,
            textvariable=self.payment_var,
            width=37,
            state="readonly"
        )

        self.payment_combo["values"] = (
            "Cash",
            "UPI",
            "Credit Card",
            "Debit Card",
            "Net Banking"
        )

        # Default Payment Mode
        self.payment_combo.current(0)

        self.payment_combo.grid(
            row=5,
            column=1,
            padx=10
        )

        # ----------------------------------
        # Notes
        # ----------------------------------

        ttk.Label(
            main,
            text="Notes",
            font=("Arial", 11)
        ).grid(
            row=6,
            column=0,
            sticky="nw",
            pady=10
        )

        self.notes = tk.Text(
            main,
            width=40,
            height=6,
            font=("Arial", 10)
        )

        self.notes.grid(
            row=6,
            column=1,
            padx=10
        )

        # ----------------------------------
        # Save Button
        # ----------------------------------

        tk.Button(
            main,
            text="💾 Save Expense",
            bg="#F44336",
            fg="white",
            activebackground="#D32F2F",
            activeforeground="white",
            font=("Arial", 12, "bold"),
            width=22,
            height=2,
            cursor="hand2",
            command=self.save_expense_data
        ).grid(
            row=7,
            column=0,
            columnspan=2,
            pady=30
        )

            # ==========================================
    # Save Expense
    # ==========================================

    def save_expense_data(self):

        date = self.date_picker.get()
        category = self.category_var.get().strip()
        description = self.description_var.get().strip()
        amount = self.amount_var.get().strip()
        payment_mode = self.payment_var.get().strip()
        notes = self.notes.get("1.0", "end").strip()

        # -----------------------------
        # Validation
        # -----------------------------

        if category == "" or amount == "" or payment_mode == "":
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

        save_expense(
            self.user[0],
            date,
            category,
            description,
            amount,
            payment_mode,
            notes
        )

        messagebox.showinfo(
            "Success",
            "Expense saved successfully!"
        )

        # -----------------------------
        # Reset Form
        # -----------------------------

        self.date_picker.set_date(datetime.today())

        self.category_combo.current(0)

        self.description_var.set("")

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

    ExpenseWindow(dummy_user)

    root.mainloop()