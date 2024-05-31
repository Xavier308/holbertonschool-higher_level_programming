from flask import Flask, jsonify, request, Response
import json
from collections import OrderedDict

app = Flask(__name__)

# Initialize with an empty users dictionary.
users = {}

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
        response = json.dumps(user, ensure_ascii=False)
        return Response(response, mimetype='application/json')
    else:
        return jsonify({"message": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    user_data = request.get_json()
    if not user_data or 'username' not in user_data or not user_data['username']:
        return jsonify({"message": "Missing or empty username"}), 400

    if any(field not in user_data or not user_data[field] for field in ['name', 'age', 'city']):
        return jsonify({"message": "Missing required field"}), 400

    username = user_data['username']
    if username in users:
        return jsonify({"message": "User already exists"}), 409

    ordered_user_data = OrderedDict([
        ('username', username),
        ('name', user_data['name']),
        ('age', user_data['age']),
        ('city', user_data['city'])
    ])

    users[username] = ordered_user_data
    response = json.dumps({"message": "User added", "user": ordered_user_data}, ensure_ascii=False)
    return Response(response, mimetype='application/json')


if __name__ == "__main__":
    app.run(debug=False)
