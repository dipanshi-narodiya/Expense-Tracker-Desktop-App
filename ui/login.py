# ==========================================
# Expense Tracker - Login Page
# ==========================================

import tkinter as tk
from tkinter import ttk, messagebox

# Import database login function
from utils.authentication import login_user as db_login_user


class LoginWindow:

    def __init__(self):

        # Create Main Window
        self.root = tk.Tk()

        self.root.title("Expense Tracker - Login")
        self.root.geometry("700x550")
        self.root.resizable(False, False)

        self.create_widgets()

        self.root.mainloop()

    # ==========================================
    # Create Widgets
    # ==========================================

    def create_widgets(self):

        # Main Frame
        self.main_frame = ttk.Frame(
            self.root,
            padding=20
        )

        self.main_frame.pack(expand=True)

        # Title
        self.title_label = ttk.Label(
            self.main_frame,
            text="💰 Expense Tracker",
            font=("Arial", 22, "bold")
        )

        self.title_label.pack(pady=(10, 5))

        # Subtitle
        self.subtitle_label = ttk.Label(
            self.main_frame,
            text="Welcome Back",
            font=("Arial", 14)
        )

        self.subtitle_label.pack(pady=(0, 25))

        # Username / Email
        self.username_label = ttk.Label(
            self.main_frame,
            text="Username or Email"
        )

        self.username_label.pack(anchor="w")

        self.username_var = tk.StringVar()

        self.username_entry = ttk.Entry(
            self.main_frame,
            textvariable=self.username_var,
            width=40
        )

        self.username_entry.pack(pady=(0, 10))

        # Password
        self.password_label = ttk.Label(
            self.main_frame,
            text="Password"
        )

        self.password_label.pack(anchor="w")

        self.password_var = tk.StringVar()

        self.password_entry = ttk.Entry(
            self.main_frame,
            textvariable=self.password_var,
            width=40,
            show="*"
        )

        self.password_entry.pack(pady=(0, 10))

        self.username_entry.focus()

        # Show Password Checkbox
        self.show_password_var = tk.BooleanVar()

        self.show_password_checkbox = ttk.Checkbutton(
            self.main_frame,
            text="Show Password",
            variable=self.show_password_var,
            command=self.toggle_password
        )

        self.show_password_checkbox.pack(anchor="w", pady=(0, 20))

        # Login Button
        self.login_button = tk.Button(
            self.main_frame,
            text="Login",
            bg="#0078D7",
            fg="white",
            activebackground="#005A9E",
            activeforeground="white",
            font=("Arial", 12, "bold"),
            width=20,
            cursor="hand2",
            command=self.login_user
        )

        self.login_button.pack(pady=15)

        # Allow Enter key to Login
        self.root.bind("<Return>", lambda event: self.login_user())

        # Register Link
        self.register_label = tk.Label(
            self.main_frame,
            text="Don't have an account? Register",
            fg="blue",
            cursor="hand2",
            font=("Arial", 10, "underline")
        )

        self.register_label.pack()

        self.register_label.bind("<Button-1>", self.open_register)

    # ==========================================
    # Show / Hide Password
    # ==========================================

    def toggle_password(self):

        if self.show_password_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    # ==========================================
    # Login User
    # ==========================================

    def login_user(self):

        username = self.username_var.get().strip()
        password = self.password_var.get().strip()

        if username == "" or password == "":
            messagebox.showerror(
                "Error",
                "Please enter Username/Email and Password."
            )
            return

        try:

            success, result = db_login_user(
                username,
                password
            )

            if success:

                messagebox.showinfo(
                    "Success",
                    "Login Successful!"
                )

                # Close Login Window
                self.root.destroy()

                # Open Dashboard
                from ui.dashboard import DashboardWindow

                DashboardWindow(result)

            else:

                messagebox.showerror(
                    "Login Failed",
                    result
                )

        except Exception as e:

            import traceback

            traceback.print_exc()

            messagebox.showerror(
                "Unexpected Error",
                str(e)
            )
    # ==========================================
    # Open Register Window
    # ==========================================

    def open_register(self, event):

        self.root.destroy()

        from ui.register import RegisterWindow

        RegisterWindow()


# ==========================================
# Run File
# ==========================================

if __name__ == "__main__":
    LoginWindow()