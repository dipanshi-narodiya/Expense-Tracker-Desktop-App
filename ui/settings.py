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
            bg="#2563EB",
            height=70
        )

        header.pack(fill="x")

        header.pack_propagate(False)

        tk.Label(
            header,
            text="⚙ Settings",
            font=("Segoe UI",24,"bold"),
            bg="#2563EB",
            fg="white"
        ).pack(
            pady=18
        )

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
            fill="both",
            expand=True,
            padx=40,
            pady=30
        )

        # ==========================================
        # Title
        # ==========================================

        tk.Label(
            self.card,
            text="User Profile",
            font=("Segoe UI",20,"bold"),
            bg="white",
            fg="#111827"
        ).pack(
            pady=(20,25)
        )

        # ==========================================
        # Profile Information
        # ==========================================

        profile_frame = tk.LabelFrame(
            self.card,
            text=" 👤 Profile Information ",
            bg="white",
            fg="#111827",
            font=("Segoe UI",12,"bold"),
            padx=20,
            pady=20
        )

        profile_frame.pack(
            fill="x",
            padx=30,
            pady=(0,30)
        )

        # Name

        tk.Label(
            profile_frame,
            text="👤 Name",
            font=("Segoe UI",11,"bold"),
            bg="white",
            fg="#374151"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=8
        )

        tk.Label(
            profile_frame,
            text=self.user[1],
            font=("Segoe UI",11),
            bg="white",
            fg="#111827"
        ).grid(
            row=0,
            column=1,
            sticky="w",
            padx=30
        )

        # Username

        tk.Label(
            profile_frame,
            text="🆔 Username",
            font=("Segoe UI",11,"bold"),
            bg="white",
            fg="#374151"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            pady=8
        )

        tk.Label(
            profile_frame,
            text=self.user[2],
            font=("Segoe UI",11),
            bg="white",
            fg="#111827"
        ).grid(
            row=1,
            column=1,
            sticky="w",
            padx=30
        )

        # Email

        tk.Label(
            profile_frame,
            text="📧 Email",
            font=("Segoe UI",11,"bold"),
            bg="white",
            fg="#374151"
        ).grid(
            row=2,
            column=0,
            sticky="w",
            pady=8
        )

        tk.Label(
            profile_frame,
            text=self.user[3],
            font=("Segoe UI",11),
            bg="white",
            fg="#111827"
        ).grid(
            row=2,
            column=1,
            sticky="w",
            padx=30
        )

        # ==========================================
        # Action Buttons
        # ==========================================

        button_frame = tk.Frame(
            self.card,
            bg="white"
        )

        button_frame.pack(
            pady=(10,25)
        )

        # ------------------------------------------
        # Edit Profile
        # ------------------------------------------

        tk.Button(
            button_frame,
            text="✏ Edit Profile",
            bg="#2563EB",
            fg="white",
            activebackground="#1D4ED8",
            activeforeground="white",
            font=("Segoe UI",11,"bold"),
            relief="flat",
            cursor="hand2",
            width=22,
            height=2,
            command=self.edit_profile
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=8
        )

        # ------------------------------------------
        # Change Password
        # ------------------------------------------

        tk.Button(
            button_frame,
            text="🔒 Change Password",
            bg="#F59E0B",
            fg="white",
            activebackground="#D97706",
            activeforeground="white",
            font=("Segoe UI",11,"bold"),
            relief="flat",
            cursor="hand2",
            width=22,
            height=2,
            command=self.change_password
        ).grid(
            row=0,
            column=1,
            padx=10,
            pady=8
        )

        # ------------------------------------------
        # About Application
        # ------------------------------------------

        tk.Button(
            button_frame,
            text="ℹ About Application",
            bg="#9333EA",
            fg="white",
            activebackground="#7E22CE",
            activeforeground="white",
            font=("Segoe UI",11,"bold"),
            relief="flat",
            cursor="hand2",
            width=22,
            height=2,
            command=self.open_about
        ).grid(
            row=1,
            column=0,
            columnspan=2,
            pady=15
        )
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