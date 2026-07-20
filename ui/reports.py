# ==========================================
# Reports Window
# ==========================================

import tkinter as tk
from tkinter import ttk, messagebox
from utils.export_excel import export_to_excel
from utils.export_pdf import export_to_pdf
from utils.helper import (
    get_income_records,
    get_expense_records,
    delete_income_record,
    delete_expense_record,
    search_records
)


class ReportsWindow:

    def __init__(self, user):

        self.user = user

        self.root = tk.Toplevel()

        self.root.title("Expense Tracker - Reports")

        self.root.geometry("1350x850")

        self.root.minsize(1200,750)

        self.root.resizable(True, True)

        self.create_widgets()

         # THIS LINE MUST EXIST
        self.load_data()

    def search_data(self):

        keyword = self.search_var.get().strip()

        if keyword == "":
            self.load_data()
            return

        income_rows, expense_rows = search_records(
            self.user[0],
            keyword
        )

        # Clear Income Table
        for row in self.income_table.get_children():
            self.income_table.delete(row)

        # Clear Expense Table
        for row in self.expense_table.get_children():
            self.expense_table.delete(row)

        # Insert Income Results
        for row in income_rows:
            self.income_table.insert("", "end", values=row)

        # Insert Expense Results
        for row in expense_rows:
            self.expense_table.insert("", "end", values=row)

    def show_all(self):

        self.search_var.set("")

        self.load_data()
    # ==========================================
    # Create Widgets
    # ==========================================

    def create_widgets(self):

        # ==========================
        # Configure Root
        # ==========================

        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        main = ttk.Frame(self.root, padding=15)
        main.grid(row=0, column=0, sticky="nsew")

        main.rowconfigure(3, weight=1)
        main.rowconfigure(5, weight=1)
        main.columnconfigure(0, weight=1)

        # ==========================
        # Title
        # ==========================

        title = ttk.Label(
            main,
            text="📊 Expense Tracker Reports",
            font=("Arial", 24, "bold")
        )

        title.grid(row=0, column=0, pady=(0,20))

        # ==========================
        # Toolbar
        # ==========================

        toolbar = ttk.Frame(main)
        toolbar.grid(row=1, column=0, sticky="ew", pady=(0,20))

        toolbar.columnconfigure(1, weight=1)

        ttk.Label(
            toolbar,
            text="Search :",
            font=("Arial",11)
        ).grid(row=0,column=0,padx=5)

        self.search_var = tk.StringVar()

        self.search_var.trace_add(
            "write",
            lambda *args: self.search_data()
        )

        ttk.Entry(
            toolbar,
            textvariable=self.search_var,
            width=35
        ).grid(row=0,column=1,padx=5,sticky="ew")

        tk.Button(
            toolbar,
            text="Search",
            bg="#2196F3",
            fg="white",
            width=12,
            command=self.search_data
        ).grid(row=0,column=2,padx=5)

        tk.Button(
            toolbar,
            text="Show All",
            bg="#4CAF50",
            fg="white",
            width=12,
            command=self.show_all
        ).grid(row=0,column=3,padx=5)

        tk.Button(
            toolbar,
            text="Export Excel",
            bg="#FF9800",
            fg="white",
            width=15,
            command=lambda: export_to_excel(self.user[0])
        ).grid(row=0,column=4,padx=5)

        tk.Button(
            toolbar,
            text="📄 Export PDF",
            bg="#E53935",
            fg="white",
            width=15,
            command=lambda: export_to_pdf(self.user)
        ).grid(row=0, column=5, padx=5)
        # ==========================
        # Income Section
        # ==========================

        income_frame = ttk.LabelFrame(
            main,
            text=" Income Records ",
            padding=10
        )

        income_frame.grid(
            row=3,
            column=0,
            sticky="nsew",
            pady=(0,15)
        )

        income_frame.rowconfigure(0,weight=1)
        income_frame.columnconfigure(0,weight=1)

        self.income_table = ttk.Treeview(

            income_frame,

            columns=(
                "ID",
                "Date",
                "Source",
                "Amount",
                "Notes"
            ),

            show="headings"

        )

        self.income_table.heading("ID",text="ID")
        self.income_table.heading("Date",text="Date")
        self.income_table.heading("Source",text="Source")
        self.income_table.heading("Amount",text="Amount")
        self.income_table.heading("Notes",text="Notes")

        self.income_table.column("ID",width=0,stretch=False)
        self.income_table.column("Date",width=120)
        self.income_table.column("Source",width=180)
        self.income_table.column("Amount",width=120)
        self.income_table.column("Notes",width=350)

        income_y = ttk.Scrollbar(
            income_frame,
            orient="vertical",
            command=self.income_table.yview
        )

        income_x = ttk.Scrollbar(
            income_frame,
            orient="horizontal",
            command=self.income_table.xview
        )

        self.income_table.configure(
            yscrollcommand=income_y.set,
            xscrollcommand=income_x.set
        )

        self.income_table.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        income_y.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        income_x.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        self.income_table.bind(
            "<Double-1>",
            lambda event: self.edit_income()
        )

        # ==========================
        # Expense Section
        # ==========================

        expense_frame = ttk.LabelFrame(
            main,
            text=" Expense Records ",
            padding=10
        )

        expense_frame.grid(
            row=5,
            column=0,
            sticky="nsew",
            pady=(0,15)
        )

        expense_frame.rowconfigure(0, weight=1)
        expense_frame.columnconfigure(0, weight=1)

        self.expense_table = ttk.Treeview(

            expense_frame,

            columns=(
                "ID",
                "Date",
                "Category",
                "Description",
                "Amount"
            ),

            show="headings"

        )

        self.expense_table.heading("ID", text="ID")
        self.expense_table.heading("Date", text="Date")
        self.expense_table.heading("Category", text="Category")
        self.expense_table.heading("Description", text="Description")
        self.expense_table.heading("Amount", text="Amount")

        self.expense_table.column("ID", width=0, stretch=False)
        self.expense_table.column("Date", width=120)
        self.expense_table.column("Category", width=180)
        self.expense_table.column("Description", width=350)
        self.expense_table.column("Amount", width=120)

        expense_y = ttk.Scrollbar(
            expense_frame,
            orient="vertical",
            command=self.expense_table.yview
        )

        expense_x = ttk.Scrollbar(
            expense_frame,
            orient="horizontal",
            command=self.expense_table.xview
        )

        self.expense_table.configure(
            yscrollcommand=expense_y.set,
            xscrollcommand=expense_x.set
        )

        self.expense_table.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        expense_y.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        expense_x.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        self.expense_table.bind(
            "<Double-1>",
             self.edit_expense
        )
        # ==========================
        # Action Buttons
        # ==========================

        action_frame = ttk.Frame(main)

        action_frame.grid(
            row=6,
            column=0,
            pady=20
        )

        tk.Button(
            action_frame,
            text="🗑 Delete Income",
            bg="#F44336",
            fg="white",
            width=16,
            font=("Arial",11,"bold"),
            command=self.delete_income
        ).grid(row=0,column=0,padx=8)

        tk.Button(
            action_frame,
            text="✏ Edit Income",
            bg="#FF9800",
            fg="white",
            width=16,
            font=("Arial",11,"bold"),
            command=self.edit_income
        ).grid(row=0,column=1,padx=8)

        tk.Button(
            action_frame,
            text="🗑 Delete Expense",
            bg="#F44336",
            fg="white",
            width=16,
            font=("Arial",11,"bold"),
            command=self.delete_expense
        ).grid(row=0,column=2,padx=8)

        tk.Button(
            action_frame,
            text="✏ Edit Expense",
            bg="#FF9800",
            fg="white",
            width=16,
            font=("Arial",11,"bold"),
            command=self.edit_expense
        ).grid(row=0,column=3,padx=8)

        # ==========================
        # Status Bar
        # ==========================

        self.status = ttk.Label(
            main,
            text="Ready",
            relief="sunken",
            anchor="w",
            padding=5
        )

        self.status.grid(
            row=7,
            column=0,
            sticky="ew"
        )

        self.income_table.tag_configure(
            "even",
            background="#FFFFFF"
        )

        self.income_table.tag_configure(
            "odd",
            background="#F5F5F5"
        )

        self.expense_table.tag_configure(
            "even",
            background="#FFFFFF"
        )

        self.expense_table.tag_configure(
            "odd",
            background="#F5F5F5"
        )
        self.load_data()

        self.status.config(
            text="Records Loaded Successfully"
        )

    # ==========================================
    # Load Data
    # ==========================================

    def load_data(self):

        user_id = self.user[0]

        # Clear old rows
        for row in self.income_table.get_children():
            self.income_table.delete(row)

        for row in self.expense_table.get_children():
            self.expense_table.delete(row)

        # Load Income
        incomes = get_income_records(user_id)

        for i, row in enumerate(incomes):

            tag = "even" if i % 2 == 0 else "odd"

            self.income_table.insert(
                "",
                "end",
                values=row,
                tags=(tag,)
            )

        # Load Expense
        expenses = get_expense_records(user_id)

        for i, row in enumerate(expenses):

            tag = "even" if i % 2 == 0 else "odd"

            self.expense_table.insert(
                "",
                "end",
                values=row,
                tags=(tag,)
            )

    # ==========================================
    # Delete Income
    # ==========================================

    def delete_income(self):

        selected = self.income_table.selection()

        if not selected:
            messagebox.showerror(
                "Error",
                "Please select an income record."
            )
            return

        item = self.income_table.item(selected)

        record_id = item["values"][0]

        # Delete from database
        delete_income_record(record_id)

        # Reload the tables
        self.load_data()

        # Update status bar
        self.status.config(
            text="✅ Income deleted successfully."
        )

        # Show success message
        messagebox.showinfo(
            "Success",
            "Income deleted successfully."
        )
    # ==========================================
    # Delete Expense
    # ==========================================

    def delete_expense(self):

        selected = self.expense_table.selection()

        if not selected:
            messagebox.showerror(
                "Error",
                "Please select an expense record."
            )
            return

        item = self.expense_table.item(selected)

        record_id = item["values"][0]

        # Delete from database
        delete_expense_record(record_id)

        # Reload the tables
        self.load_data()

        # Update status bar
        self.status.config(
            text="✅ Expense deleted successfully."
        )

        # Show success message
        messagebox.showinfo(
            "Success",
            "Expense deleted successfully."
        )
    # ==========================================
    # Edit Expense
    # ==========================================

    def edit_expense(self, event=None):

        selected = self.expense_table.selection()

        if not selected:
            messagebox.showerror(
                "Error",
                "Please select an expense record."
            )
            return

        item = self.expense_table.item(selected)

        record = item["values"]

        print(record)      # Debug

        from ui.edit_expense import EditExpenseWindow

        EditExpenseWindow(record, self)

    def edit_income(self):

        selected = self.income_table.selection()

        if not selected:
            messagebox.showerror(
                "Error",
                "Please select an income record."
            )
            return

        item = self.income_table.item(selected)

        record = item["values"]

        from ui.edit_income import EditIncomeWindow

        EditIncomeWindow(record, self)

    
if __name__ == "__main__":

    root = tk.Tk()
    root.withdraw()

    ReportsWindow((1, "Demo User"))

    root.mainloop()