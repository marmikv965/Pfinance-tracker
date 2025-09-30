import sqlite3

def get_connection():
    return sqlite3.connect("finance.db")

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS transactions")
    cursor.execute("""
               CREATE TABLE transactions (
               id INTEGER PRIMARY KEY AUTOINCREMENT ,
               type TEXT ,
               category TEXT ,
               amount REAL ,
               date TEXT ,
               description TEXT
        )
    """)
    conn.commit()
    conn.close()