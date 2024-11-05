from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('chocolate_house.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS seasonal_flavors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flavor_name TEXT NOT NULL,
            available_from DATE NOT NULL,
            available_to DATE NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ingredient_inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ingredient_name TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customer_suggestions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            suggestion TEXT NOT NULL,
            allergy_concerns TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/seasonal_flavors', methods=['GET', 'POST'])
def seasonal_flavors():
    if request.method == 'GET':
        conn = sqlite3.connect('chocolate_house.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM seasonal_flavors')
        flavors = cursor.fetchall()
        conn.close()
        return jsonify(flavors)
    elif request.method == 'POST':
        new_flavor = request.get_json()
        flavor_name = new_flavor['flavor_name']
        available_from = new_flavor['available_from']
        available_to = new_flavor['available_to']
        conn = sqlite3.connect('chocolate_house.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO seasonal_flavors (flavor_name, available_from, available_to)
            VALUES (?, ?, ?)
        ''', (flavor_name, available_from, available_to))
        conn.commit()
        conn.close()
        return jsonify({"status": "success"}), 201

# Similar routes for ingredient_inventory and customer_suggestions...

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
