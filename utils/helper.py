# ==========================================
# Helper Functions
# ==========================================

from utils.database import connect_db
from collections import defaultdict


# ==========================================
# Save Income
# ==========================================

def save_income(
    user_id,
    date,
    source,
    amount,
    payment_mode,
    notes
):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO income
        (user_id, date, source, amount, payment_mode, notes)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        user_id,
        date,
        source,
        amount,
        payment_mode,
        notes
    ))

    conn.commit()
    conn.close()


# ==========================================
# Save Expense
# ==========================================

def save_expense(user_id, date, category, description, amount, payment_mode, notes):
    """
    Save expense into database.
    """

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO expenses
        (user_id, date, category, description, amount, payment_mode, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        user_id,
        date,
        category,
        description,
        amount,
        payment_mode,
        notes
    ))

    conn.commit()
    conn.close()


# ==========================================
# Get Total Income
# ==========================================

def get_total_income(user_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT IFNULL(SUM(amount),0)
        FROM income
        WHERE user_id=?
    """, (user_id,))

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_total_expense(user_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT IFNULL(SUM(amount),0)
        FROM expenses
        WHERE user_id=?
    """, (user_id,))

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_balance(user_id):

    income = get_total_income(user_id)
    expense = get_total_expense(user_id)

    return income - expense

# ==========================================
# Get All Income Records
# ==========================================

def get_income_records(user_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            date,
            source,
            amount,
            notes
        FROM income
        WHERE user_id=?
        ORDER BY id DESC
    """, (user_id,))

    rows = cursor.fetchall()

    conn.close()

    return rows


# ==========================================
# Get All Expense Records
# ==========================================

def get_expense_records(user_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            date,
            category,
            description,
            amount
        FROM expenses
        WHERE user_id=?
        ORDER BY id DESC
    """, (user_id,))

    rows = cursor.fetchall()

    conn.close()

    return rows

def delete_income_record(record_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM income WHERE id=?",
        (record_id,)
    )

    conn.commit()
    conn.close()


def delete_expense_record(record_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM expenses WHERE id=?",
        (record_id,)
    )

    conn.commit()
    conn.close()

def update_income(record_id, date, source, amount, notes):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE income
        SET
            date=?,
            source=?,
            amount=?,
            notes=?
        WHERE id=?
    """, (
        date,
        source,
        amount,
        notes,
        record_id
    ))

    conn.commit()
    conn.close()    

def update_expense(
    record_id,
    date,
    category,
    description,
    amount,
    payment_mode,
    notes
):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE expenses
        SET
            date=?,
            category=?,
            description=?,
            amount=?,
            payment_mode=?,
            notes=?
        WHERE id=?
    """, (
        date,
        category,
        description,
        amount,
        payment_mode,
        notes,
        record_id
    ))

    conn.commit()
    conn.close()

def search_records(user_id, keyword):

    conn = connect_db()
    cursor = conn.cursor()

    keyword = f"%{keyword}%"

    # ---------------- Income Search ----------------

    cursor.execute("""
        SELECT
            id,
            date,
            source,
            amount
        FROM income
        WHERE user_id=?
        AND (
            date LIKE ?
            OR source LIKE ?
            OR notes LIKE ?
            OR CAST(amount AS TEXT) LIKE ?
        )
        ORDER BY id DESC
    """, (
        user_id,
        keyword,
        keyword,
        keyword,
        keyword
    ))

    income_rows = cursor.fetchall()

    # ---------------- Expense Search ----------------

    cursor.execute("""
        SELECT
            id,
            date,
            category,
            description,
            amount
        FROM expenses
        WHERE user_id=?
        AND (
            date LIKE ?
            OR category LIKE ?
            OR description LIKE ?
            OR CAST(amount AS TEXT) LIKE ?
        )
        ORDER BY id DESC
    """, (
        user_id,
        keyword,
        keyword,
        keyword,
        keyword
    ))

    expense_rows = cursor.fetchall()

    conn.close()

    return income_rows, expense_rows

def get_recent_transactions(user_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""

        SELECT
            date,
            source,
            amount,
            'Income'
        FROM income
        WHERE user_id=?

        UNION ALL

        SELECT
            date,
            category,
            amount,
            'Expense'
        FROM expenses
        WHERE user_id=?

        ORDER BY date DESC

        LIMIT 5

    """, (user_id, user_id))

    rows = cursor.fetchall()

    conn.close()

    return rows

def get_expense_by_category(user_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            category,
            SUM(amount)
        FROM expenses
        WHERE user_id=?
        GROUP BY category
    """, (user_id,))

    rows = cursor.fetchall()

    conn.close()

    return rows

def get_monthly_summary(user_id):

    conn = connect_db()
    cursor = conn.cursor()

    income = defaultdict(float)
    expense = defaultdict(float)

    cursor.execute("""
        SELECT
            substr(date,4,7),
            amount
        FROM income
        WHERE user_id=?
    """,(user_id,))

    for month, amount in cursor.fetchall():
        income[month] += amount

    cursor.execute("""
        SELECT
            substr(date,4,7),
            amount
        FROM expenses
        WHERE user_id=?
    """,(user_id,))

    for month, amount in cursor.fetchall():
        expense[month] += amount

    conn.close()

    months = sorted(set(income.keys()) | set(expense.keys()))

    income_values = [income[m] for m in months]
    expense_values = [expense[m] for m in months]

    return months, income_values, expense_values

# ==========================================
# Save Budget
# ==========================================

def save_budget(user_id, month, year, amount):

    conn = connect_db()
    cursor = conn.cursor()

    # Check if budget already exists
    cursor.execute("""
        SELECT id
        FROM budget
        WHERE user_id=?
        AND month=?
        AND year=?
    """, (
        user_id,
        month,
        year
    ))

    record = cursor.fetchone()

    if record:

        cursor.execute("""
            UPDATE budget
            SET amount=?
            WHERE id=?
        """, (
            amount,
            record[0]
        ))

    else:

        cursor.execute("""
            INSERT INTO budget
            (user_id, month, year, amount)
            VALUES (?, ?, ?, ?)
        """, (
            user_id,
            month,
            year,
            amount
        ))

    conn.commit()
    conn.close()

# ==========================================
# Get Monthly Budget
# ==========================================

from datetime import datetime

def get_budget(user_id):

    conn = connect_db()
    cursor = conn.cursor()

    month = datetime.now().strftime("%B")
    year = datetime.now().year

    cursor.execute("""
        SELECT amount
        FROM budget
        WHERE user_id=?
        AND month=?
        AND year=?
    """, (
        user_id,
        month,
        year
    ))

    row = cursor.fetchone()

    conn.close()

    if row:
        return row[0]

    return 0

# ==========================================
# Remaining Budget
# ==========================================

def get_remaining_budget(user_id):

    budget = get_budget(user_id)

    expense = get_total_expense(user_id)

    return budget - expense

# ==========================================
# AI Financial Insights
# ==========================================

def get_financial_insights(user_id):

    insights = []

    income = get_total_income(user_id)

    expense = get_total_expense(user_id)

    balance = income - expense

    budget = get_budget(user_id)

    # Savings
    if balance > 0:
        insights.append(
            f"✅ Great! You saved ₹{balance:.2f}."
        )
    else:
        insights.append(
            f"⚠ You spent ₹{abs(balance):.2f} more than your income."
        )

    # Budget
    if budget > 0:

        used = (expense / budget) * 100

        insights.append(
            f"📊 Budget Used : {used:.1f}%"
        )

        if used >= 100:
            insights.append(
                "🚨 Budget exceeded!"
            )

        elif used >= 80:
            insights.append(
                "⚠ Budget almost finished."
            )

    # Top Expense Category
    categories = get_expense_by_category(user_id)

    if categories:

        top = max(categories, key=lambda x: x[1])

        insights.append(
            f"🏆 Highest Expense : {top[0]} (₹{top[1]:.2f})"
        )

    return insights

# ==========================================
# Update Profile
# ==========================================

def update_profile(user_id, full_name, email):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
        SET
            full_name=?,
            email=?
        WHERE id=?
    """, (
        full_name,
        email,
        user_id
    ))

    conn.commit()
    conn.close()

# ==========================================
# Change Password
# ==========================================

def change_password(user_id, old_password, new_password):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT password
        FROM users
        WHERE id=?
    """, (user_id,))

    row = cursor.fetchone()

    if not row:
        conn.close()
        return False

    if row[0] != old_password:
        conn.close()
        return False

    cursor.execute("""
        UPDATE users
        SET password=?
        WHERE id=?
    """, (
        new_password,
        user_id
    ))

    conn.commit()
    conn.close()

    return True