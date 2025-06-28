from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_data():
    try:
        with open('products.json') as f:
            return json.load(f)
    except Exception as e:
        return []

def read_csv_data():
    try:
        with open('products.csv', newline='') as f:
            reader = csv.DictReader(f)
            return [dict(id=int(row['id']), name=row['name'], category=row['category'], price=float(row['price'])) for row in reader]
    except Exception as e:
        return []

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    error = None
    data = []

    if source == 'json':
        data = read_json_data()
    elif source == 'csv':
        data = read_csv_data()
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error, products=[])

    if product_id:
        try:
            product_id = int(product_id)
            filtered = [product for product in data if product['id'] == product_id]
            if filtered:
                data = filtered
            else:
                error = "Product not found"
                data = []
        except ValueError:
            error = "Invalid product ID"

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)