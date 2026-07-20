import sqlite3
import hashlib
from utils.database import connect_db
import re


def hash_password(password):
    """
    Convert a plain text password into a SHA-256 hash.
    """
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(full_name, username, email, password):
    """
    Register a new user.
    """

    conn = connect_db()
    cursor = conn.cursor()

    try:
        # Convert password into a secure hash
        hashed_password = hash_password(password)

        cursor.execute("""
            INSERT INTO users (full_name, username, email, password)
            VALUES (?, ?, ?, ?)
        """, (full_name, username, email, hashed_password))

        conn.commit()

        return True, "Registration Successful!"

    except sqlite3.IntegrityError:
        return False, "Username or Email already exists."

    except Exception as e:
        return False, str(e)

    finally:
        conn.close()

def validate_password(password):
    """
    Validate password strength.
    """

    # Minimum length
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    # Uppercase letter
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."

    # Lowercase letter
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."

    # Number
    if not re.search(r"\d", password):
        return False, "Password must contain at least one number."

    # Special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character."

    return True, "Password is valid."

def login_user(username_or_email, password):
    """
    Check username/email and password during login.
    """

    conn = connect_db()
    cursor = conn.cursor()

    try:

        # Convert password into hash
        hashed_password = hash_password(password)

        cursor.execute("""
            SELECT *
            FROM users
            WHERE (username = ? OR email = ?)
            AND password = ?
        """, (username_or_email, username_or_email, hashed_password))

        user = cursor.fetchone()

        if user:
            return True, user
        else:
            return False, "Invalid Username, Email or Password."

    finally:
        conn.close()


def username_exists(username):
    """
    Check whether a username already exists.
    """

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id FROM users
        WHERE username = ?
    """, (username,))

    user = cursor.fetchone()

    conn.close()

    return user is not None


def email_exists(email):
    """
    Check whether an email already exists.
    """

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id FROM users
        WHERE email = ?
    """, (email,))

    user = cursor.fetchone()

    conn.close()

    return user is not None


