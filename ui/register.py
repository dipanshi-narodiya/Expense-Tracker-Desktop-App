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
            height=80
        )

        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text="💰 Expense Tracker",
            bg="#2563EB",
            fg="white",
            font=("Segoe UI", 24, "bold")
        ).pack(pady=18)

        # ==========================================
        # Main Card
        # ==========================================

        self.card = tk.Frame(
            container,
            bg="white",
            highlightbackground="#D1D5DB",
            highlightthickness=1
        )

        self.card.pack(
            padx=70,
            pady=30,
            fill="both",
            expand=True
        )

        # ==========================================
        # Title
        # ==========================================

        tk.Label(
            self.card,
            text="Create New Account",
            bg="white",
            fg="#111827",
            font=("Segoe UI", 20, "bold")
        ).pack(pady=(25, 5))

        tk.Label(
            self.card,
            text="Fill in the details below",
            bg="white",
            fg="#6B7280",
            font=("Segoe UI", 11)
        ).pack(pady=(0, 25))

        # ==========================================
        # Form Frame
        # ==========================================

        form = tk.Frame(
            self.card,
            bg="white"
        )

        form.pack(
            padx=40,
            fill="x"
        )

        form.columnconfigure(0, weight=1)

        # ==========================================
        # Full Name
        # ==========================================

        tk.Label(
            form,
            text="👤 Full Name",
            bg="white",
            fg="#374151",
            font=("Segoe UI",11,"bold")
        ).grid(row=0,column=0,sticky="w",pady=(0,5))

        self.full_name_var = tk.StringVar()

        self.full_name_entry = tk.Entry(
            form,
            textvariable=self.full_name_var,
            font=("Segoe UI",11),
            relief="solid",
            bd=1
        )

        self.full_name_entry.grid(
            row=1,
            column=0,
            sticky="ew",
            ipady=6,
            pady=(0,15)
        )

        # ==========================================
        # Username
        # ==========================================

        tk.Label(
            form,
            text="👤 Username",
            bg="white",
            fg="#374151",
            font=("Segoe UI",11,"bold")
        ).grid(row=2,column=0,sticky="w",pady=(0,5))

        self.username_var = tk.StringVar()

        self.username_entry = tk.Entry(
            form,
            textvariable=self.username_var,
            font=("Segoe UI",11),
            relief="solid",
            bd=1
        )

        self.username_entry.grid(
            row=3,
            column=0,
            sticky="ew",
            ipady=6,
            pady=(0,15)
        )

        # ==========================================
        # Email
        # ==========================================

        tk.Label(
            form,
            text="📧 Email",
            bg="white",
            fg="#374151",
            font=("Segoe UI",11,"bold")
        ).grid(row=4,column=0,sticky="w",pady=(0,5))

        self.email_var = tk.StringVar()

        self.email_entry = tk.Entry(
            form,
            textvariable=self.email_var,
            font=("Segoe UI",11),
            relief="solid",
            bd=1
        )

        self.email_entry.grid(
            row=5,
            column=0,
            sticky="ew",
            ipady=6,
            pady=(0,15)
        )

        # ==========================================
        # Password
        # ==========================================

        tk.Label(
            form,
            text="🔒 Password",
            bg="white",
            fg="#374151",
            font=("Segoe UI",11,"bold")
        ).grid(row=6,column=0,sticky="w",pady=(0,5))

        self.password_var = tk.StringVar()

        self.password_entry = tk.Entry(
            form,
            textvariable=self.password_var,
            show="*",
            font=("Segoe UI",11),
            relief="solid",
            bd=1
        )

        self.password_entry.grid(
            row=7,
            column=0,
            sticky="ew",
            ipady=6,
            pady=(0,15)
        )

        # ==========================================
        # Confirm Password
        # ==========================================

        tk.Label(
            form,
            text="🔒 Confirm Password",
            bg="white",
            fg="#374151",
            font=("Segoe UI",11,"bold")
        ).grid(row=8,column=0,sticky="w",pady=(0,5))

        self.confirm_password_var = tk.StringVar()

        self.confirm_password_entry = tk.Entry(
            form,
            textvariable=self.confirm_password_var,
            show="*",
            font=("Segoe UI",11),
            relief="solid",
            bd=1
        )

        self.confirm_password_entry.grid(
            row=9,
            column=0,
            sticky="ew",
            ipady=6,
            pady=(0,15)
        )

        # ==========================================
        # Show Password
        # ==========================================

        self.show_password_var = tk.BooleanVar()

        self.show_password_checkbox = tk.Checkbutton(
            form,
            text="Show Password",
            variable=self.show_password_var,
            command=self.toggle_password,
            bg="white",
            activebackground="white",
            font=("Segoe UI",10)
        )

        self.show_password_checkbox.grid(
            row=10,
            column=0,
            sticky="w",
            pady=(0,20)
        )

        # ==========================================
        # Register Button
        # ==========================================

        self.register_button = tk.Button(
            self.card,
            text="📝 Register Account",
            bg="#2563EB",
            fg="white",
            activebackground="#1D4ED8",
            activeforeground="white",
            font=("Segoe UI",12,"bold"),
            relief="flat",
            cursor="hand2",
            width=22,
            height=2,
            command=self.register_user
        )

        self.register_button.pack(pady=(10,20))

        # ==========================================
        # Login Link
        # ==========================================

        login_frame = tk.Frame(
            self.card,
            bg="white"
        )

        login_frame.pack(pady=(0,25))

        tk.Label(
            login_frame,
            text="Already have an account?",
            bg="white",
            fg="#6B7280",
            font=("Segoe UI",10)
        ).pack(side="left")

        self.login_label = tk.Label(
            login_frame,
            text=" Login",
            bg="white",
            fg="#2563EB",
            cursor="hand2",
            font=("Segoe UI",10,"bold","underline")
        )

        self.login_label.pack(side="left")

        self.login_label.bind(
            "<Button-1>",
            self.open_login
        )

        # ==========================================
        # Focus
        # ==========================================

        self.full_name_entry.focus_set()


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