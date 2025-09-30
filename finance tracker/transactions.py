from database import get_connection

def add_transaction(t_type, category, amount, date, description=""):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO transactions (\"type\", category, amount, date, description) VALUES ('expense', 'food', 100.0, '2025-09-30', 'test')",
        (t_type, category, amount, date, description)
        )
    conn.commit()
    conn.close()

def get_summary():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='income'")
    income = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='expense'")
    expense = cursor.fetchone()[0] or 0
    balance = income - expense
    conn.close()
    return income, expense, balance
  
    