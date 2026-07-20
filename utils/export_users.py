import pandas as pd
from tkinter import filedialog, messagebox
from utils.admin_helper import get_all_users


def export_users_excel():

    users = get_all_users()

    if len(users) == 0:
        messagebox.showwarning(
            "No Data",
            "No users found."
        )
        return

    df = pd.DataFrame(
        users,
        columns=[
            "ID",
            "Full Name",
            "Username",
            "Email",
            "Created At"
        ]
    )

    filename = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[
            ("Excel File", "*.xlsx")
        ],
        initialfile="users.xlsx"
    )

    if filename == "":
        return

    df.to_excel(filename, index=False)

    messagebox.showinfo(
        "Success",
        "Users exported successfully."
    )