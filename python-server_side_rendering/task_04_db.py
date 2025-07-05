from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# JSON faylından oxuma
def read_json_file():
    try:
        with open('products.json') as file:
            return json.load(file)
    except Exception:
        return None

# CSV faylından oxuma
def read_csv_file():
    try:
        products = []
        with open('products.csv', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["id"] = int(row["id"])
                row["price"] = float(row["price"])
                products.append(row)
        return products
    except Exception:
        return None

# SQLite bazasından oxuma
def read_sqlite_data():
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row  # Dict kimi oxumaq üçün
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        products = [dict(row) for row in rows]
        conn.close()
        return products
    except Exception:
        return None

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    error_message = None
    data = []

    if source == 'json':
        data = read_json_file()
    elif source == 'csv':
        data = read_csv_file()
    elif source == 'sql':
        data = read_sqlite_data()
    else:
        error_message = "Wrong source"
        return render_template("product_display.html", error=error_message, products=[])

    if data is None:
        error_message = "Error reading data"
        return render_template("product_display.html", error=error_message, products=[])

    if product_id is not None:
        filtered = [p for p in data if int(p["id"]) == product_id]
        if filtered:
            data = filtered
        else:
            error_message = "Product not found"
            data = []

    return render_template("product_display.html", products=data, error=error_message)

if __name__ == '__main__':
    app.run(debug=True)