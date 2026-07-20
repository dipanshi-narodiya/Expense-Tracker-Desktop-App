import tkinter as tk
from tkinter import ttk, messagebox
from utils.helper import update_income


class EditIncomeWindow:

    def __init__(self, record , reports_window):

        self.record = record
        self.reports_window = reports_window

        self.root = tk.Toplevel()

        self.root.title("Edit Income")
        self.root.geometry("500x550")
        self.root.resizable(False, False)

        self.create_widgets()

    # ==========================================
    # Create Widgets
    # ==========================================

    def create_widgets(self):

        main = ttk.Frame(self.root, padding=20)
        main.pack(fill="both", expand=True)

        ttk.Label(
            main,
            text="✏️ Edit Income",
            font=("Arial", 20, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=(10, 25))

        # -----------------------
        # Date
        # -----------------------

        ttk.Label(main, text="Date").grid(
            row=1,
            column=0,
            sticky="w",
            pady=8
        )

        self.date_var = tk.StringVar(value=self.record[1])

        ttk.Entry(
            main,
            textvariable=self.date_var,
            width=35
        ).grid(row=1, column=1)

        # -----------------------
        # Source
        # -----------------------

        ttk.Label(main, text="Source").grid(
            row=2,
            column=0,
            sticky="w",
            pady=8
        )

        self.source_var = tk.StringVar(value=self.record[2])

        self.source_combo = ttk.Combobox(
            main,
            textvariable=self.source_var,
            width=32,
            state="readonly"
        )

        self.source_combo["values"] = (
            "Salary",
            "Business",
            "Freelancing",
            "Bonus",
            "Gift",
            "Other"
        )

        self.source_combo.grid(row=2, column=1)

        # -----------------------
        # Amount
        # -----------------------

        ttk.Label(main, text="Amount").grid(
            row=3,
            column=0,
            sticky="w",
            pady=8
        )

        self.amount_var = tk.StringVar(value=str(self.record[3]))

        ttk.Entry(
            main,
            textvariable=self.amount_var,
            width=35
        ).grid(row=3, column=1)

        # -----------------------
        # Notes
        # -----------------------

        ttk.Label(main, text="Notes").grid(
            row=4,
            column=0,
            sticky="nw",
            pady=8
        )

        self.notes = tk.Text(
            main,
            width=35,
            height=5
        )

        self.notes.grid(row=4, column=1)

        if len(self.record) > 4:
            self.notes.insert("1.0", self.record[4])

        # -----------------------
        # Update Button
        # -----------------------

        tk.Button(
            main,
            text="Update Income",
            bg="#4CAF50",
            fg="white",
            width=20,
            font=("Arial", 11, "bold"),
            command=self.update_income
        ).grid(
            row=5,
            column=0,
            columnspan=2,
            pady=25
        )

    # ==========================================
    # Update Income
    # ==========================================

    def update_income(self):

        date = self.date_var.get().strip()
        source = self.source_var.get().strip()
        amount = self.amount_var.get().strip()
        notes = self.notes.get("1.0", "end").strip()

        # Validation
        if date == "" or source == "" or amount == "":
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
                "Error",
                "Please enter a valid amount."
            )
            return

        # Update Database
        update_income(
            self.record[0],
            date,
            source,
            amount,
            notes
        )

        messagebox.showinfo(
            "Success",
            "Income updated successfully."
        )

        # Refresh Reports
        self.reports_window.load_data()

        # Close Edit Window
        self.root.destroy()


if __name__ == "__main__":

    root = tk.Tk()
    root.withdraw()

    EditIncomeWindow(
        (1, "2026-07-11", "Salary", 25000, "July Salary")
    )

    root.mainloop()