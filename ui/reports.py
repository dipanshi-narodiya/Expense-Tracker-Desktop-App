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

        # self.root.geometry("1350x850")
        self.root.state("zoomed")
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

        # Make card expand properly
        container.rowconfigure(1, weight=1)
        container.columnconfigure(0, weight=1)

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
            text="📊 Reports & Transactions",
            font=("Segoe UI",24,"bold"),
            bg="#2563EB",
            fg="white"
        ).pack(pady=18)

        # ==========================================
        # Main Card
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

        # Card Layout
        for i in range(6):
            self.card.columnconfigure(i, weight=1)

        # Make Income & Expense sections expand
        self.card.rowconfigure(2, weight=1)
        self.card.rowconfigure(3, weight=1)
        # ==========================================
        # Title
        # ==========================================

        tk.Label(
            self.card,
            text="Income & Expense Reports",
            font=("Segoe UI",20,"bold"),
            bg="white",
            fg="#111827"
        ).grid(
            row=0,
            column=0,
            columnspan=6,
            pady=(20,25)
        )

        # ==========================================
        # Toolbar
        # ==========================================

        toolbar = tk.Frame(
            self.card,
            bg="white"
        )

        toolbar.grid(
            row=1,
            column=0,
            columnspan=6,
            sticky="ew",
            padx=20,
            pady=(0,25)
        )

        toolbar.columnconfigure(1, weight=1)

        # Search Label

        tk.Label(
            toolbar,
            text="🔍 Search",
            font=("Segoe UI",11,"bold"),
            bg="white",
            fg="#374151"
        ).grid(
            row=0,
            column=0,
            padx=(0,10)
        )

        # Search Entry

        self.search_var = tk.StringVar()

        self.search_var.trace_add(
            "write",
            lambda *args: self.search_data()
        )

        search_entry = ttk.Entry(
            toolbar,
            textvariable=self.search_var,
            font=("Segoe UI",11),
            width=35
        )

        search_entry.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=5
        )

        # Search Button

        tk.Button(
            toolbar,
            text="Search",
            bg="#2563EB",
            fg="white",
            activebackground="#1D4ED8",
            activeforeground="white",
            font=("Segoe UI",10,"bold"),
            relief="flat",
            cursor="hand2",
            width=10,
            command=self.search_data
        ).grid(
            row=0,
            column=2,
            padx=5
        )

        # Show All Button

        tk.Button(
            toolbar,
            text="Show All",
            bg="#22C55E",
            fg="white",
            activebackground="#16A34A",
            activeforeground="white",
            font=("Segoe UI",10,"bold"),
            relief="flat",
            cursor="hand2",
            width=10,
            command=self.show_all
        ).grid(
            row=0,
            column=3,
            padx=5
        )

        # Export Excel Button

        tk.Button(
            toolbar,
            text="Excel",
            bg="#F59E0B",
            fg="white",
            activebackground="#D97706",
            activeforeground="white",
            font=("Segoe UI",10,"bold"),
            relief="flat",
            cursor="hand2",
            width=10,
            command=lambda: export_to_excel(self.user[0])
        ).grid(
            row=0,
            column=4,
            padx=5
        )

        # Export PDF Button

        tk.Button(
            toolbar,
            text="PDF",
            bg="#EF4444",
            fg="white",
            activebackground="#DC2626",
            activeforeground="white",
            font=("Segoe UI",10,"bold"),
            relief="flat",
            cursor="hand2",
            width=10,
            command=lambda: export_to_pdf(self.user)
        ).grid(
            row=0,
            column=5,
            padx=5
        )

        # ==========================================
        # Income Records
        # ==========================================

        income_frame = tk.LabelFrame(
            self.card,
            text=" 💰 Income Records ",
            bg="white",
            fg="#111827",
            font=("Segoe UI",12,"bold"),
            padx=10,
            pady=10
        )

        income_frame.grid(
            row=2,
            column=0,
            columnspan=6,
            sticky="nsew",
            padx=20,
            pady=(0,20)
        )

        income_frame.rowconfigure(0, weight=1)
        income_frame.columnconfigure(0, weight=1)

        self.income_table = ttk.Treeview(
            income_frame,
            columns=(
                "ID",
                "Date",
                "Source",
                "Amount",
                "Notes"
            ),
            show="headings",
            height=8
        )

        self.income_table.heading("ID", text="ID")
        self.income_table.heading("Date", text="Date")
        self.income_table.heading("Source", text="Source")
        self.income_table.heading("Amount", text="Amount")
        self.income_table.heading("Notes", text="Notes")

        self.income_table.column("ID", width=0, stretch=False)
        self.income_table.column("Date", width=120, anchor="center")
        self.income_table.column("Source", width=180, anchor="center")
        self.income_table.column("Amount", width=120, anchor="center")
        self.income_table.column("Notes", width=400)

        income_scroll_y = ttk.Scrollbar(
            income_frame,
            orient="vertical",
            command=self.income_table.yview
        )

        income_scroll_x = ttk.Scrollbar(
            income_frame,
            orient="horizontal",
            command=self.income_table.xview
        )

        self.income_table.configure(
            yscrollcommand=income_scroll_y.set,
            xscrollcommand=income_scroll_x.set
        )

        self.income_table.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        income_scroll_y.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        income_scroll_x.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        self.income_table.bind(
            "<Double-1>",
            lambda event: self.edit_income()
        )

        self.income_table.tag_configure(
            "even",
            background="#FFFFFF"
        )

        self.income_table.tag_configure(
            "odd",
            background="#F8FAFC"
        )

        # ==========================================
        # Expense Records
        # ==========================================

        expense_frame = tk.LabelFrame(
            self.card,
            text=" 💸 Expense Records ",
            bg="white",
            fg="#111827",
            font=("Segoe UI",12,"bold"),
            padx=10,
            pady=10
        )

        expense_frame.grid(
            row=3,
            column=0,
            columnspan=6,
            sticky="nsew",
            padx=20,
            pady=(0,20)
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
            show="headings",
            height=8
        )

        self.expense_table.heading("ID", text="ID")
        self.expense_table.heading("Date", text="Date")
        self.expense_table.heading("Category", text="Category")
        self.expense_table.heading("Description", text="Description")
        self.expense_table.heading("Amount", text="Amount")

        self.expense_table.column("ID", width=0, stretch=False)
        self.expense_table.column("Date", width=120, anchor="center")
        self.expense_table.column("Category", width=170, anchor="center")
        self.expense_table.column("Description", width=420)
        self.expense_table.column("Amount", width=120, anchor="center")

        expense_scroll_y = ttk.Scrollbar(
            expense_frame,
            orient="vertical",
            command=self.expense_table.yview
        )

        expense_scroll_x = ttk.Scrollbar(
            expense_frame,
            orient="horizontal",
            command=self.expense_table.xview
        )

        self.expense_table.configure(
            yscrollcommand=expense_scroll_y.set,
            xscrollcommand=expense_scroll_x.set
        )

        self.expense_table.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        expense_scroll_y.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        expense_scroll_x.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        self.expense_table.bind(
            "<Double-1>",
            self.edit_expense
        )

        self.expense_table.tag_configure(
            "even",
            background="#FFFFFF"
        )

        self.expense_table.tag_configure(
            "odd",
            background="#F8FAFC"
        )

        # ==========================================
        # Action Buttons
        # ==========================================

        action_frame = tk.Frame(
            self.card,
            bg="white"
        )

        action_frame.grid(
            row=4,
            column=0,
            columnspan=6,
            pady=(10,20)
        )

        tk.Button(
            action_frame,
            text="🗑 Delete Income",
            bg="#EF4444",
            fg="white",
            width=16,
            font=("Segoe UI",10,"bold"),
            relief="flat",
            cursor="hand2",
            command=self.delete_income
        ).grid(row=0,column=0,padx=8)

        tk.Button(
            action_frame,
            text="✏ Edit Income",
            bg="#F59E0B",
            fg="white",
            width=16,
            font=("Segoe UI",10,"bold"),
            relief="flat",
            cursor="hand2",
            command=self.edit_income
        ).grid(row=0,column=1,padx=8)

        tk.Button(
            action_frame,
            text="🗑 Delete Expense",
            bg="#EF4444",
            fg="white",
            width=16,
            font=("Segoe UI",10,"bold"),
            relief="flat",
            cursor="hand2",
            command=self.delete_expense
        ).grid(row=0,column=2,padx=8)

        tk.Button(
            action_frame,
            text="✏ Edit Expense",
            bg="#F59E0B",
            fg="white",
            width=16,
            font=("Segoe UI",10,"bold"),
            relief="flat",
            cursor="hand2",
            command=self.edit_expense
        ).grid(row=0,column=3,padx=8)

        # ==========================================
        # Status Bar
        # ==========================================

        self.status = tk.Label(
            self.card,
            text="Ready",
            bg="#F3F4F6",
            fg="#374151",
            font=("Segoe UI",10),
            anchor="w",
            padx=10,
            pady=8
        )

        self.status.grid(
            row=5,
            column=0,
            columnspan=6,
            sticky="ew",
            padx=20,
            pady=(10,15)
        )

        # ==========================================
        # Responsive Layout
        # ==========================================

        self.card.columnconfigure(0, weight=1)

        # ==========================================
        # Load Initial Data
        # ==========================================

        self.load_data()

        self.status.config(
            text="✅ Records Loaded Successfully"
        )
    # ==========================================
    # Load Data
    # ==========================================

    def load_data(self):

        user_id = self.user[0]

        # ==========================================
        # Clear Income Table
        # ==========================================

        for row in self.income_table.get_children():
            self.income_table.delete(row)

        # ==========================================
        # Clear Expense Table
        # ==========================================

        for row in self.expense_table.get_children():
            self.expense_table.delete(row)

        # ==========================================
        # Load Income Records
        # ==========================================

        incomes = get_income_records(user_id)

        for i, row in enumerate(incomes):

            tag = "even" if i % 2 == 0 else "odd"

            self.income_table.insert(
                "",
                "end",
                values=row,
                tags=(tag,)
            )

        # ==========================================
        # Load Expense Records
        # ==========================================

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
        # Update Status
        # ==========================================

        if hasattr(self, "status"):
            self.status.config(
                text="✅ Records Loaded Successfully"
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