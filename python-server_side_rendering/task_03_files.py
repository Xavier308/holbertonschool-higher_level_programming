from flask import Flask, render_template, request, json
import csv

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
        else:
            return render_template('product_display.html', message="Wrong source")
    except FileNotFoundError:
        return render_template('product_display.html', message="File not found")
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

if __name__ == '__main__':
    app.run(debug=True, port=5000)
