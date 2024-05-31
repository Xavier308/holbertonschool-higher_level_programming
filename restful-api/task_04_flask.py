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
    if users:
        return jsonify(list(users.keys()))
    else:
        return jsonify([])  # Ensure returning an empty list when no users are added.

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
    if not user_data or 'username' not in user_data:
        return jsonify({"message": "Missing username"}), 400

    username = user_data.get('username')
    if username in users:
        return jsonify({"message": "User already exists"}), 409

    ordered_user_data = OrderedDict([
        ('username', username),
        ('name', user_data.get('name')),
        ('age', user_data.get('age')),
        ('city', user_data.get('city'))
    ])

    users[username] = ordered_user_data
    response = json.dumps({"message": "User added", "user": ordered_user_data}, ensure_ascii=False)
    return Response(response, mimetype='application/json')


if __name__ == "__main__":
    app.run(debug=False)
