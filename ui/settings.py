import tkinter as tk
from tkinter import ttk, messagebox
from utils.helper import update_profile
from utils.helper import update_profile, change_password


class SettingsWindow:

    def __init__(self, user):

        self.user = user

        self.root = tk.Toplevel()

        self.root.title("Settings")

        self.root.geometry("700x550")

        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):

        ttk.Label(
            self.root,
            text="⚙ Settings",
            font=("Arial", 22, "bold")
        ).pack(pady=20)

        profile = ttk.LabelFrame(
            self.root,
            text="Profile",
            padding=20
        )

        profile.pack(fill="x", padx=20)

        ttk.Label(
            profile,
            text=f"Name : {self.user[1]}",
            font=("Arial",12)
        ).pack(anchor="w", pady=5)

        ttk.Label(
            profile,
            text=f"Username : {self.user[2]}",
            font=("Arial",12)
        ).pack(anchor="w", pady=5)

        ttk.Label(
            profile,
            text=f"Email : {self.user[3]}",
            font=("Arial",12)
        ).pack(anchor="w", pady=5)

        ttk.Button(
            self.root,
            text="✏ Edit Profile",
            command=self.edit_profile
        ).pack(pady=15)

        ttk.Button(
            self.root,
            text="🔒 Change Password",
            command=self.change_password
        ).pack(pady=10)

        ttk.Button(
            self.root,
            text="ℹ About Application",
            command=self.open_about
        ).pack(pady=10)

    def edit_profile(self):

        window = tk.Toplevel(self.root)

        window.title("Edit Profile")

        window.geometry("400x300")

        ttk.Label(window, text="Full Name").pack(pady=5)

        name_var = tk.StringVar(value=self.user[1])

        ttk.Entry(
            window,
            textvariable=name_var,
            width=35
        ).pack()

        ttk.Label(window, text="Email").pack(pady=10)

        email_var = tk.StringVar(value=self.user[3])

        ttk.Entry(
            window,
            textvariable=email_var,
            width=35
        ).pack()

        def save():

            update_profile(
                self.user[0],
                name_var.get(),
                email_var.get()
            )

            messagebox.showinfo(
                "Success",
                "Profile Updated Successfully!"
            )

            window.destroy()

        ttk.Button(
            window,
            text="Save",
            command=save
        ).pack(pady=20)
    
    def change_password(self):

        window = tk.Toplevel(self.root)

        window.title("Change Password")

        window.geometry("400x350")

        # ---------------- Old Password ----------------

        ttk.Label(
            window,
            text="Current Password"
        ).pack(pady=5)

        old_var = tk.StringVar()

        ttk.Entry(
            window,
            textvariable=old_var,
            show="*",
            width=30
        ).pack()

        # ---------------- New Password ----------------

        ttk.Label(
            window,
            text="New Password"
        ).pack(pady=10)

        new_var = tk.StringVar()

        ttk.Entry(
            window,
            textvariable=new_var,
            show="*",
            width=30
        ).pack()

        # ---------------- Confirm Password ----------------

        ttk.Label(
            window,
            text="Confirm Password"
        ).pack(pady=10)

        confirm_var = tk.StringVar()

        ttk.Entry(
            window,
            textvariable=confirm_var,
            show="*",
            width=30
        ).pack()

        # ---------------- Save ----------------

        def save():

            if new_var.get() != confirm_var.get():

                messagebox.showerror(
                    "Error",
                    "Passwords do not match."
                )
                return

            success = change_password(
                self.user[0],
                old_var.get(),
                new_var.get()
            )

            if success:

                messagebox.showinfo(
                    "Success",
                    "Password changed successfully."
                )

                window.destroy()

            else:

                messagebox.showerror(
                    "Error",
                    "Current password is incorrect."
                )

        ttk.Button(
            window,
            text="Save",
            command=save
        ).pack(pady=20)
    
    def open_about(self):

        from ui.about import AboutWindow

        AboutWindow()