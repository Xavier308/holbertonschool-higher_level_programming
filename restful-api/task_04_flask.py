# task_04_flask.py
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user storage
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Root endpoint
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# /status endpoint
@app.route('/status')
def status():
    return "OK"

# /data endpoint to get all usernames
@app.route('/data')
def get_usernames():
    return jsonify(list(users.keys()))

# /users/<username> endpoint to get user details
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# /add_user endpoint to add a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    if not username or username in users:
        return jsonify({"error": "Invalid or existing username"}), 400

    users[username] = {
        "username": username,
        "name": data.get('name'),
        "age": data.get('age'),
        "city": data.get('city')
    }
    return jsonify({"message": "User added", "user": users[username]})


if __name__ == "__main__":
    app.run(debug=True)
