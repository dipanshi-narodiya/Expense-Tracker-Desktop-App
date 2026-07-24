# ==========================================
# Expense Tracker - Login Page
# ==========================================

import tkinter as tk
from tkinter import ttk, messagebox

# Import database login function
from utils.authentication import login_user as db_login_user
from utils.theme import *

class LoginWindow:

    def __init__(self):

            self.root = tk.Tk()
            self.root.state("zoomed")
            self.root.title("Expense Tracker")

            self.root.geometry(
                f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"
            )

            self.root.configure(
                bg=BACKGROUND
            )

            self.root.resizable(False, False)

            self.create_widgets()

            self.root.mainloop()

    # ==========================================
    # Create Widgets
    # ==========================================

    def create_widgets(self):

        # -----------------------
        # Left Panel
        # -----------------------

        self.left_frame = tk.Frame(
            self.root,
            bg=PRIMARY,
            width=LEFT_PANEL_WIDTH
        )

        self.left_frame.pack(
            side="left",
            fill="y"
        )

        self.left_frame.pack_propagate(False)

        # -----------------------
        # Right Panel
        # -----------------------

        self.right_frame = tk.Frame(
            self.root,
            bg=BACKGROUND
        )

        self.right_frame.pack(
            side="right",
            fill="both",
            expand=True
        )

        # =======================
        # Left Panel Content
        # =======================

        tk.Label(
            self.left_frame,
            text="💰",
            bg=PRIMARY,
            fg="white",
            font=("Segoe UI Emoji", 55)
        ).pack(pady=(60, 10))

        tk.Label(
            self.left_frame,
            text="Expense\nTracker",
            bg=PRIMARY,
            fg="white",
            font=("Segoe UI", 30, "bold"),
            justify="center"
        ).pack()

        tk.Label(
            self.left_frame,
            text="Track • Manage • Save",
            bg=PRIMARY,
            fg="white",
            font=("Segoe UI", 16)
        ).pack(pady=10)

        tk.Label(
            self.left_frame,
            text="Manage your income,\nexpenses, budget and\nreports easily.",
            bg=PRIMARY,
            fg="white",
            font=("Segoe UI", 12),
            justify="center"
        ).pack(pady=30)

        # Decorative Circle

        canvas = tk.Canvas(
            self.left_frame,
            width=180,
            height=180,
            bg=PRIMARY,
            highlightthickness=0
        )

        canvas.pack(pady=20)

        canvas.create_oval(
            15,
            15,
            165,
            165,
            fill="#3B82F6",
            outline=""
        )

        canvas.create_text(
            90,
            90,
            text="₹",
            font=("Segoe UI", 55, "bold"),
            fill="white"
        )

        tk.Label(
            self.left_frame,
            text="Secure • Fast • Reliable",
            bg=PRIMARY,
            fg="white",
            font=("Segoe UI", 11)
        ).pack(side="bottom", pady=30)

        # =======================
        # Login Card
        # =======================

        self.card = tk.Frame(
            self.right_frame,
            bg="white",
            padx=40,
            pady=35
        )

        self.card.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        tk.Label(
            self.card,
            text="Welcome Back",
            bg="white",
            fg=TEXT,
            font=("Segoe UI", 24, "bold")
        ).pack(pady=(0, 5))

        tk.Label(
            self.card,
            text="Login to continue",
            bg="white",
            fg=SUBTEXT,
            font=("Segoe UI", 11)
        ).pack(pady=(0, 25))

                # ==========================================
        # Username
        # ==========================================

        tk.Label(
            self.card,
            text="Username or Email",
            bg="white",
            fg=TEXT,
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w")

        self.username_var = tk.StringVar()

        self.username_entry = tk.Entry(
            self.card,
            textvariable=self.username_var,
            font=("Segoe UI", 11),
            width=32,
            relief="solid",
            bd=1,
            highlightthickness=1,
            highlightbackground="#D1D5DB",
            highlightcolor=PRIMARY
        )

        self.username_entry.pack(
            ipady=8,
            pady=(5, 18)
        )

        # ==========================================
        # Password
        # ==========================================

        tk.Label(
            self.card,
            text="Password",
            bg="white",
            fg=TEXT,
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w")

        self.password_var = tk.StringVar()

        self.password_entry = tk.Entry(
            self.card,
            textvariable=self.password_var,
            show="*",
            font=("Segoe UI", 11),
            width=32,
            relief="solid",
            bd=1,
            highlightthickness=1,
            highlightbackground="#D1D5DB",
            highlightcolor=PRIMARY
        )

        self.password_entry.pack(
            ipady=8,
            pady=(5, 15)
        )

        # ==========================================
        # Show Password
        # ==========================================

        self.show_password_var = tk.BooleanVar()

        self.show_password = tk.Checkbutton(
            self.card,
            text="Show Password",
            variable=self.show_password_var,
            command=self.toggle_password,
            bg="white",
            activebackground="white",
            fg=TEXT,
            font=("Segoe UI", 10)
        )

        self.show_password.pack(
            anchor="w",
            pady=(0, 20)
        )

        # ==========================================
        # Login Button
        # ==========================================

        self.login_button = tk.Button(
            self.card,
            text="LOGIN",
            bg=PRIMARY,
            fg="white",
            activebackground=PRIMARY_HOVER,
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            font=("Segoe UI", 12, "bold"),
            width=24,
            pady=10,
            command=self.login_user
        )

        self.login_button.pack(
            pady=(0, 20)
        )

        # Hover Effect

        self.login_button.bind(
            "<Enter>",
            lambda e: self.login_button.config(
                bg=PRIMARY_HOVER
            )
        )

        self.login_button.bind(
            "<Leave>",
            lambda e: self.login_button.config(
                bg=PRIMARY
            )
        )

        # ==========================================
        # Register Link
        # ==========================================

        self.register_label = tk.Label(
            self.card,
            text="Create New Account",
            bg="white",
            fg=PRIMARY,
            cursor="hand2",
            font=("Segoe UI", 10, "underline")
        )

        self.register_label.pack()

        self.register_label.bind(
            "<Button-1>",
            self.open_register
        )

        # ==========================================
        # Focus & Enter Key
        # ==========================================

        self.username_entry.focus()

        self.root.bind(
            "<Return>",
            lambda event: self.login_user()
        )

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

        # -------------------------
        # Validation
        # -------------------------

        if username == "" or password == "":

            messagebox.showerror(
                "Login Error",
                "Please enter Username/Email and Password."
            )

            return

        # -------------------------
        # Database Login
        # -------------------------

        try:

            success, result = db_login_user(
                username,
                password
            )

            if success:

                messagebox.showinfo(
                    "Success",
                    f"Welcome {result[1]}!"
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

    def open_register(self, event=None):

        try:

            # Close Login Window
            self.root.destroy()

            # Open Register Window
            from ui.register import RegisterWindow

            RegisterWindow()

        except Exception as e:

            import traceback

            traceback.print_exc()

            messagebox.showerror(
                "Error",
                str(e)
            )


# ==========================================
# Run File
# ==========================================

if __name__ == "__main__":

    LoginWindow()