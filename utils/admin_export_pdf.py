from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle
)

from reportlab.lib import colors

from tkinter import (
    filedialog,
    messagebox
)

from utils.admin_helper import get_all_users

def export_users_pdf():

    users = get_all_users()

    if len(users) == 0:
        messagebox.showwarning(
            "No Data",
            "No users found."
        )
        return

    filename = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[
            ("PDF File", "*.pdf")
        ],
        initialfile="Users_Report.pdf"
    )

    if filename == "":
        return

    pdf = SimpleDocTemplate(filename)

    data = [[
        "ID",
        "Name",
        "Username",
        "Email",
        "Created At"
    ]]

    for user in users:
        data.append(list(user))

    table = Table(data)

    table.setStyle(TableStyle([

        ("BACKGROUND", (0,0), (-1,0), colors.darkblue),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),

        ("GRID", (0,0), (-1,-1), 1, colors.black),

        ("BACKGROUND", (0,1), (-1,-1), colors.beige),

        ("ALIGN", (0,0), (-1,-1), "CENTER"),

        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),

        ("BOTTOMPADDING", (0,0), (-1,0), 10),

    ]))

    pdf.build([table])

    messagebox.showinfo(
        "Success",
        "Users PDF exported successfully!"
    )