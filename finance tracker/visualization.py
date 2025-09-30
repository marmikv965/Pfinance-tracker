import pandas as pd
import matplotlib.pyplot as plt
from database import get_connection

def expense_chart():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM transactions",conn)
    conn.close()

    if df.empty:
        print("No transactions found.")
        return
    
    expenses = df[df['type'] == "expense"]

    if expenses.empty:
        print("No expense record to display.")
        return
    
    expenses = expenses.groupby("category")
    ["amount"].sum()
    expenses.plot(kind="pie", autopct="%. 1f%%") 
    plt.title("Expenses by Category")
    plt.show()