import sqlite3

conn = sqlite3.connect("transactions.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    description TEXT,
    amount REAL,
    type TEXT
)
""")

conn.commit()
