import sqlite3

connection = sqlite3.connect("marketplace6_2.db")

cursor = connection.cursor()

# creare tabele - tabelul user

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    adress TEXT,
    city TEXT,
    postal_code TEXT,
    country TEXT
    );
    """
)

# tabelul products

# tabelul orders

# tabelul order_items

