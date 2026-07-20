from utils.database import connect_db


# ==========================================
# Get All Users
# ==========================================

def get_all_users():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            full_name,
            username,
            email,
            created_at
        FROM users
        ORDER BY id
    """)

    users = cursor.fetchall()

    conn.close()

    return users

# ==========================================
# Search Users
# ==========================================

def search_users(keyword):

    conn = connect_db()
    cursor = conn.cursor()

    keyword = f"%{keyword}%"

    cursor.execute("""
        SELECT
            id,
            full_name,
            username,
            email,
            created_at
        FROM users
        WHERE
            full_name LIKE ?
            OR username LIKE ?
            OR email LIKE ?
        ORDER BY id
    """, (
        keyword,
        keyword,
        keyword
    ))

    users = cursor.fetchall()

    conn.close()

    return users

# ==========================================
# Delete User
# ==========================================

def delete_user(user_id):

    conn = connect_db()
    cursor = conn.cursor()

    # Delete related data first

    cursor.execute(
        "DELETE FROM income WHERE user_id=?",
        (user_id,)
    )

    cursor.execute(
        "DELETE FROM expenses WHERE user_id=?",
        (user_id,)
    )

    cursor.execute(
        "DELETE FROM budget WHERE user_id=?",
        (user_id,)
    )

    cursor.execute(
        "DELETE FROM categories WHERE user_id=?",
        (user_id,)
    )

    cursor.execute(
        "DELETE FROM payment_modes WHERE user_id=?",
        (user_id,)
    )

    # Delete user

    cursor.execute(
        "DELETE FROM users WHERE id=?",
        (user_id,)
    )

    conn.commit()
    conn.close()

# ==========================================
# Get User Summary
# ==========================================

def get_user_summary(user_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            IFNULL(SUM(amount),0)
        FROM income
        WHERE user_id=?
    """, (user_id,))

    income = cursor.fetchone()[0]

    cursor.execute("""
        SELECT
            IFNULL(SUM(amount),0)
        FROM expenses
        WHERE user_id=?
    """, (user_id,))

    expense = cursor.fetchone()[0]

    balance = income - expense

    conn.close()

    return income, expense, balance

# ==========================================
# Admin Statistics
# ==========================================

def get_admin_statistics():

    conn = connect_db()
    cursor = conn.cursor()

    # Total Users
    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]

    # Total Income
    cursor.execute("SELECT IFNULL(SUM(amount),0) FROM income")
    total_income = cursor.fetchone()[0]

    # Total Expense
    cursor.execute("SELECT IFNULL(SUM(amount),0) FROM expenses")
    total_expense = cursor.fetchone()[0]

    conn.close()

    total_balance = total_income - total_expense

    return (
        total_users,
        total_income,
        total_expense,
        total_balance
    )