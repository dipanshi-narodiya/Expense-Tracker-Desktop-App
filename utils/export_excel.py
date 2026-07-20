from openpyxl import Workbook
from tkinter import filedialog, messagebox

from utils.helper import (
    get_income_records,
    get_expense_records
)


def export_to_excel(user_id):

    wb = Workbook()

    # ==========================
    # Income Sheet
    # ==========================

    income_sheet = wb.active
    income_sheet.title = "Income"

    income_sheet.append([
        "ID",
        "Date",
        "Source",
        "Amount"
    ])

    incomes = get_income_records(user_id)

    for row in incomes:
        income_sheet.append(row)

    # ==========================
    # Expense Sheet
    # ==========================

    expense_sheet = wb.create_sheet("Expenses")

    expense_sheet.append([
        "ID",
        "Date",
        "Category",
        "Description",
        "Amount"
    ])

    expenses = get_expense_records(user_id)

    for row in expenses:
        expense_sheet.append(row)

    # ==========================
    # Save File
    # ==========================

    file_path = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[
            ("Excel File", "*.xlsx")
        ],
        initialfile="Expense_Report.xlsx"
    )

    if file_path:

        wb.save(file_path)

        messagebox.showinfo(
            "Success",
            "Excel exported successfully!"
        )