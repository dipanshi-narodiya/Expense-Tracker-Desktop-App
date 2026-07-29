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

        self.root.geometry("900x820")

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
            bg="#EF4444",
            height=70
        )

        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text="💸 Add Expense",
            font=("Segoe UI",24,"bold"),
            bg="#EF4444",
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
            text="Expense Details",
            font=("Segoe UI",20,"bold"),
            bg="white",
            fg="#111827"
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(15,20)
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
            pady=8
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
        # Category
        # ==========================================

        tk.Label(
            self.card,
            text="🛒 Category",
            font=("Segoe UI",11,"bold"),
            bg="white",
            fg="#374151"
        ).grid(
            row=2,
            column=0,
            sticky="w",
            padx=40,
            pady=8
        )

        self.category_var = tk.StringVar()

        self.category_combo = ttk.Combobox(
            self.card,
            textvariable=self.category_var,
            width=32,
            state="readonly",
            font=("Segoe UI",11)
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

        self.category_combo.current(0)

        self.category_combo.grid(
            row=2,
            column=1,
            padx=40,
            pady=12,
            sticky="ew"
        )

        # ==========================================
        # Description
        # ==========================================

        tk.Label(
            self.card,
            text="📝 Description",
            font=("Segoe UI",11,"bold"),
            bg="white",
            fg="#374151"
        ).grid(
            row=3,
            column=0,
            sticky="w",
            padx=40,
            pady=8
        )

        self.description_var = tk.StringVar()

        self.description_entry = ttk.Entry(
            self.card,
            textvariable=self.description_var,
            font=("Segoe UI",11),
            width=35
        )

        self.description_entry.grid(
            row=3,
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
            row=4,
            column=0,
            sticky="w",
            padx=40,
            pady=8
        )

        self.amount_var = tk.StringVar()

        self.amount_entry = ttk.Entry(
            self.card,
            textvariable=self.amount_var,
            font=("Segoe UI",11),
            width=35
        )

        self.amount_entry.grid(
            row=4,
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
            row=5,
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
            row=5,
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
            row=6,
            column=0,
            sticky="nw",
            padx=40,
            pady=8
        )

        self.notes = tk.Text(
            self.card,
            width=35,
            height=4,
            font=("Segoe UI",11),
            relief="solid",
            bd=1,
            wrap="word"
        )

        self.notes.grid(
            row=6,
            column=1,
            padx=40,
            pady=12,
            sticky="ew"
        )

        # ==========================================
        # Save Expense Button
        # ==========================================

        self.save_button = tk.Button(
            self.card,
            text="💾 Save Expense",
            bg="#EF4444",
            fg="white",
            activebackground="#DC2626",
            activeforeground="white",
            font=("Segoe UI",12,"bold"),
            relief="flat",
            cursor="hand2",
            width=20,
            height=2,
            command=self.save_expense_data
        )

        self.save_button.grid(
            row=7,
            column=0,
            columnspan=2,
            pady=(15,20)
        )

        # ==========================================
        # Responsive Layout
        # ==========================================

        self.card.columnconfigure(0, weight=1)
        self.card.columnconfigure(1, weight=3)

        self.amount_entry.focus()
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