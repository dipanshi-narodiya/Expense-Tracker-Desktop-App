import sqlite3
import os

# Database path
DB_PATH = os.path.join("database", "expense_tracker.db")


def connect_db():
    """Connect to SQLite database."""
    return sqlite3.connect(DB_PATH)


def create_tables():
    """Create all required tables."""

    conn = connect_db()
    cursor = conn.cursor()

    # ---------------- Users Table ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # ---------------- Income Table ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS income(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        date TEXT,
        source TEXT,
        amount REAL,
        payment_mode TEXT,
        notes TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    # ---------------- Expense Table ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        date TEXT,
        category TEXT,
        description TEXT,
        amount REAL,
        payment_mode TEXT,
        notes TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    # ---------------- Categories ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        category_name TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    # ---------------- Payment Modes ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS payment_modes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        payment_name TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    # ---------------- Budget Table ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS budget(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        month TEXT NOT NULL,
        year INTEGER NOT NULL,
        amount REAL NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()

    print("Database and tables created successfully!")

if __name__ == "__main__":
    create_tables()