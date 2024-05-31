from flask import Flask, jsonify, request
import json
from collections import OrderedDict

app = Flask(__name__)
# Force depuration
# app.config['DEBUG'] = True

# Initialize the users dictionary with OrderedDict to maintain the order.
users = {
    "jane": OrderedDict([
        ('username', 'jane'), 
        ('name', 'Jane'), 
        ('age', 28), 
        ('city', 'Los Angeles')
    ]),
    "john": OrderedDict([
        ('username', 'john'), 
        ('name', 'John'), 
        ('age', 30), 
        ('city', 'New York')
    ])
}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"message": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    user_data = request.get_json()
    username = user_data.get('username')
    if username in users:
        return jsonify({"message": "User already exists"}), 409

    # Using OrderedDict to ensure the data is serialized in the precise order.
    ordered_user_data = OrderedDict([
        ('username', user_data.get('username')),
        ('name', user_data.get('name')),
        ('age', user_data.get('age')),
        ('city', user_data.get('city'))
    ])

    users[username] = ordered_user_data
    response = json.dumps({"message": "User added", "user": ordered_user_data}, ensure_ascii=False)
    return Response(response, mimetype='application/json')


if __name__ == "__main__":
    app.run(debug=False)
