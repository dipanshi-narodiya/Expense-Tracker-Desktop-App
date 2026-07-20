import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime

from utils.helper import update_expense


class EditExpenseWindow:

    def __init__(self, record, reports_window):

        self.record = record
        self.reports_window = reports_window

        self.root = tk.Toplevel()

        self.root.title("Edit Expense")

        self.root.geometry("650x650")

        self.root.resizable(False, False)

        self.root.transient()
        self.root.grab_set()
        self.root.focus_force()

        self.create_widgets()

        # ==========================================
    # Create Widgets
    # ==========================================

    def create_widgets(self):

        main = ttk.Frame(self.root, padding=30)
        main.pack(fill="both", expand=True)

        ttk.Label(
            main,
            text="✏ Edit Expense",
            font=("Arial",22,"bold")
        ).grid(row=0,column=0,columnspan=2,pady=(0,30))

        # ---------------- Date ----------------

        ttk.Label(
            main,
            text="Date"
        ).grid(row=1,column=0,sticky="w",pady=10)

        self.date_picker = DateEntry(
            main,
            width=37,
            date_pattern="dd-mm-yyyy"
        )

        self.date_picker.grid(row=1,column=1,padx=10)

        # ---------------- Category ----------------

        ttk.Label(
            main,
            text="Category"
        ).grid(row=2,column=0,sticky="w",pady=10)

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

        self.category_combo.grid(
            row=2,
            column=1,
            padx=10
        )

        # ---------------- Description ----------------

        ttk.Label(
            main,
            text="Description"
        ).grid(row=3,column=0,sticky="w",pady=10)

        self.description_var = tk.StringVar()

        ttk.Entry(
            main,
            textvariable=self.description_var,
            width=40
        ).grid(row=3,column=1,padx=10)

        # ---------------- Amount ----------------

        ttk.Label(
            main,
            text="Amount (₹)"
        ).grid(row=4,column=0,sticky="w",pady=10)

        self.amount_var = tk.StringVar()

        ttk.Entry(
            main,
            textvariable=self.amount_var,
            width=40
        ).grid(row=4,column=1,padx=10)

        # ---------------- Payment Mode ----------------

        ttk.Label(
            main,
            text="Payment Mode"
        ).grid(row=5,column=0,sticky="w",pady=10)

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

        self.payment_combo.grid(
            row=5,
            column=1,
            padx=10
        )

        # ---------------- Notes ----------------

        ttk.Label(
            main,
            text="Notes"
        ).grid(row=6,column=0,sticky="nw",pady=10)

        self.notes = tk.Text(
            main,
            width=40,
            height=6
        )

        self.notes.grid(
            row=6,
            column=1,
            padx=10
        )

        # ==========================
        # Save Button
        # ==========================

        tk.Button(
            main,
            text="💾 Save Changes",
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12, "bold"),
            width=20,
            cursor="hand2",
            command=self.update_record
        ).grid(
            row=7,
            column=0,
            columnspan=2,
            pady=25
        )

        # ==========================
        # Load Existing Data
        # ==========================

        record_id = self.record[0]
        date = self.record[1]
        category = self.record[2]
        description = self.record[3]
        amount = self.record[4]

        # These values may not exist if your report table has only 5 columns
        payment_mode = "Cash"
        notes = ""

        if len(self.record) > 5:
            payment_mode = self.record[5]

        if len(self.record) > 6:
            notes = self.record[6]

        self.date_picker.set_date(datetime.strptime(date, "%d-%m-%Y"))

        self.category_var.set(category)
        self.description_var.set(description)
        self.amount_var.set(str(amount))
        self.payment_var.set(payment_mode)

        self.notes.insert("1.0", notes)

    # ==========================================
    # Update Expense
    # ==========================================

    def update_record(self):

        record_id = self.record[0]

        date = self.date_picker.get()
        category = self.category_var.get().strip()
        description = self.description_var.get().strip()
        amount = self.amount_var.get().strip()
        payment_mode = self.payment_var.get().strip()
        notes = self.notes.get("1.0", "end").strip()

        # Validation
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

        # Update Database
        update_expense(
            record_id,
            date,
            category,
            description,
            amount,
            payment_mode,
            notes
        )

        messagebox.showinfo(
            "Success",
            "Expense updated successfully!"
        )

        # Refresh Reports Window
        if self.reports_window:
            self.reports_window.load_data()

        self.root.destroy()

if __name__ == "__main__":

    root = tk.Tk()
    root.withdraw()

    EditExpenseWindow(
        (
            1,
            "14-07-2026",
            "Food",
            "Pizza",
            250,
            "Cash",
            "Dinner"
        ),
        None
    )

    root.mainloop()