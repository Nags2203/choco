import sqlite3

def setup_database():
    connection = sqlite3.connect('chocolate_shop.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS seasonal_chocolates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            start_date DATE,
            end_date DATE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stock_inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ingredient TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS flavor_suggestions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer TEXT NOT NULL,
            feedback TEXT,
            dietary_restrictions TEXT
        )
    ''')

    connection.commit()
    connection.close()

if __name__ == "__main__":
    setup_database()
