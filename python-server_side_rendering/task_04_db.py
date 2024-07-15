from flask import Flask, render_template, request, json
import csv
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r') as file:
        data = json.load(file)
        items_list = data.get('items', [])
    return render_template('items.html', items=items_list)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    try:
        if source == 'json':
            products = read_json(product_id)
        elif source == 'csv':
            products = read_csv(product_id)
        elif source == 'sql':
            products = read_sql(product_id)
        else:
            return render_template('product_display.html', message="Wrong source")
    except FileNotFoundError:
        return render_template('product_display.html', message="File not found")
    except sqlite3.DatabaseError as e:
        return render_template('product_display.html', message=f"Database error: {str(e)}")
    except Exception as e:
        return render_template('product_display.html', message=str(e))

    if not products:
        return render_template('product_display.html', message="Product not found")
    return render_template('product_display.html', products=products)

def read_json(product_id):
    with open('products.json', 'r') as file:
        data = json.load(file)
    if product_id:
        data = [prod for prod in data if prod['id'] == product_id]
    return data

def read_csv(product_id):
    with open('products.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    if product_id:
        data = [prod for prod in data if int(prod['id']) == product_id]
    return data

def read_sql(product_id):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    query = "SELECT * FROM Products"
    if product_id:
        query += f" WHERE id = {product_id}"
    cursor.execute(query)
    data = [{'name': row[1], 'category': row[2], 'price': row[3]} for row in cursor.fetchall()]
    conn.close()
    return data

if __name__ == '__main__':
    app.run(debug=True, port=5000)
