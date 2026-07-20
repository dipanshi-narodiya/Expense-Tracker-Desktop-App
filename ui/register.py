# ==========================================
# Expense Tracker - Register Page
# Part 1
# ==========================================

# Import tkinter library
import tkinter as tk

# Import modern widgets and messagebox
from tkinter import ttk, messagebox

# Import register function from authentication.py
from utils.authentication import register_user as db_register_user
from utils.authentication import validate_password

# from ui.login import LoginWindow
# ==========================================
# Register Window Class
# ==========================================

class RegisterWindow:

    # Constructor (Runs automatically)
    def __init__(self):

        # Create Main Window
        self.root = tk.Tk()

        # Call Functions
        self.create_window()
        self.create_widgets()

        # Keep window running
        self.root.mainloop()

    # ==========================================
    # Window Settings
    # ==========================================

    def create_window(self):

        # Window Title
        self.root.title("Expense Tracker - Register")

        # Window Size
        self.root.geometry("700x650")

        # Disable Resize
        self.root.resizable(False, False)

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

        # ==========================================
        # Title
        # ==========================================

        self.title_label = ttk.Label(
            self.main_frame,
            text="💰 Expense Tracker",
            font=("Arial", 22, "bold")
        )

        self.title_label.pack(pady=(10, 5))

        # ==========================================
        # Subtitle
        # ==========================================

        self.subtitle_label = ttk.Label(
            self.main_frame,
            text="Create New Account",
            font=("Arial", 14)
        )

        self.subtitle_label.pack(pady=(0, 25))

        # ==========================================
        # Full Name
        # ==========================================

        self.full_name_label = ttk.Label(
            self.main_frame,
            text="Full Name"
        )

        self.full_name_label.pack(anchor="w")

        self.full_name_var = tk.StringVar()

        self.full_name_entry = ttk.Entry(
            self.main_frame,
            textvariable=self.full_name_var,
            width=40
        )

        self.full_name_entry.pack(pady=(0, 10))

        # ==========================================
        # Username
        # ==========================================

        self.username_label = ttk.Label(
            self.main_frame,
            text="Username"
        )

        self.username_label.pack(anchor="w")

        self.username_var = tk.StringVar()

        self.username_entry = ttk.Entry(
            self.main_frame,
            textvariable=self.username_var,
            width=40
        )

        self.username_entry.pack(pady=(0, 10))

        # ==========================================
        # Email
        # ==========================================

        self.email_label = ttk.Label(
            self.main_frame,
            text="Email"
        )

        self.email_label.pack(anchor="w")

        self.email_var = tk.StringVar()

        self.email_entry = ttk.Entry(
            self.main_frame,
            textvariable=self.email_var,
            width=40
        )

        self.email_entry.pack(pady=(0, 10))

        # ==========================================
        # Password
        # ==========================================

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

        # ==========================================
        # Confirm Password
        # ==========================================

        self.confirm_password_label = ttk.Label(
            self.main_frame,
            text="Confirm Password"
        )

        self.confirm_password_label.pack(anchor="w")

        self.confirm_password_var = tk.StringVar()

        self.confirm_password_entry = ttk.Entry(
            self.main_frame,
            textvariable=self.confirm_password_var,
            width=40,
            show="*"
        )

        self.confirm_password_entry.pack(pady=(0, 20))
                # ==========================================
        # Show Password Checkbox
        # ==========================================

        # Variable to store checkbox state (True/False)
        self.show_password_var = tk.BooleanVar()

        # Checkbox
        self.show_password_checkbox = ttk.Checkbutton(
            self.main_frame,
            text="Show Password",
            variable=self.show_password_var,
            command=self.toggle_password
        )

        self.show_password_checkbox.pack(anchor="w", pady=(0, 20))


        # ==========================================
        # Register Button
        # ==========================================

        self.register_button = tk.Button(
            self.main_frame,
            text="Register",
            font=("Arial", 12, "bold"),
            bg="#0078D7",
            fg="white",
            activebackground="#005A9E",
            activeforeground="white",
            width=20,
            cursor="hand2",
            command=self.register_user
        )

        self.register_button.pack(pady=10)


        # ==========================================
        # Login Link
        # ==========================================

        self.login_label = tk.Label(
            self.main_frame,
            text="Already have an account? Login",
            fg="blue",
            cursor="hand2",
            font=("Arial", 10, "underline")
        )

        self.login_label.pack(pady=10)

        # Click Event
        self.login_label.bind("<Button-1>", self.open_login)
            # ==========================================
    # Show / Hide Password
    # ==========================================

    def toggle_password(self):

        if self.show_password_var.get():

            # Show password
            self.password_entry.config(show="")
            self.confirm_password_entry.config(show="")

        else:

            # Hide password
            self.password_entry.config(show="*")
            self.confirm_password_entry.config(show="*")


    # ==========================================
    # Open Login Window
    # ==========================================

    def open_login(self, event):

        # Close Register Window
        self.root.destroy()
        from ui.login import LoginWindow
        # Open Login Window
        LoginWindow()
    # ==========================================
    # Register User
    # ==========================================

    def register_user(self):

        # Get values from form
        full_name = self.full_name_var.get().strip()
        username = self.username_var.get().strip()
        email = self.email_var.get().strip()
        password = self.password_var.get()
        confirm_password = self.confirm_password_var.get()

        # Empty field validation
        if not full_name or not username or not email or not password or not confirm_password:
            messagebox.showerror(
                "Error",
                "Please fill all fields."
            )
            return

        # Password validation
        if password != confirm_password:
            messagebox.showerror(
                "Error",
                "Passwords do not match."
            )
            return
        # Validate password strength
        valid, message = validate_password(password)

        if not valid:
            messagebox.showerror(
                "Weak Password",
                message
            )
            return
        # Register user in database
        success, message = db_register_user(
            full_name,
            username,
            email,
            password
        )

        if success:

            messagebox.showinfo(
                "Success",
                message
            )

            # Clear form
            self.full_name_var.set("")
            self.username_var.set("")
            self.email_var.set("")
            self.password_var.set("")
            self.confirm_password_var.set("")

        else:

            messagebox.showerror(
                "Registration Failed",
                message
            )
# ==========================================
# Run File
# ==========================================

if __name__ == "__main__":
    RegisterWindow()