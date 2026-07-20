import tkinter as tk
from tkinter import ttk


class AboutWindow:

    def __init__(self):

        self.root = tk.Toplevel()

        self.root.title("About")

        self.root.geometry("500x450")

        self.root.resizable(False, False)

        ttk.Label(
            self.root,
            text="💰 Expense Tracker",
            font=("Arial", 22, "bold")
        ).pack(pady=20)

        ttk.Label(
            self.root,
            text="Version 1.0",
            font=("Arial", 12)
        ).pack()

        ttk.Separator(self.root).pack(fill="x", padx=20, pady=15)

        ttk.Label(
            self.root,
            text="Developed By",
            font=("Arial", 12, "bold")
        ).pack()

        ttk.Label(
            self.root,
            text="Dipanshi Patel",
            font=("Arial", 12)
        ).pack(pady=5)

        ttk.Separator(self.root).pack(fill="x", padx=20, pady=15)

        ttk.Label(
            self.root,
            text="Technologies Used",
            font=("Arial", 12, "bold")
        ).pack()

        technologies = [
            "Python",
            "Tkinter",
            "SQLite",
            "Matplotlib",
            "ReportLab"
        ]

        for tech in technologies:
            ttk.Label(
                self.root,
                text=f"• {tech}"
            ).pack(anchor="center")

        ttk.Separator(self.root).pack(fill="x", padx=20, pady=20)

        ttk.Label(
            self.root,
            text="© 2026 Expense Tracker",
            font=("Arial", 10)
        ).pack()