from flask import Flask, jsonify, request


app = Flask(__name__)

# In-memory storage for user data
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def data():
    return jsonify(list(users.keys()))  # Returns all usernames

@app.route('/status')
def status():
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    user_data = request.get_json()  # Parse JSON data from the request
    username = user_data.get('username')
    if username and username not in users:
        users[username] = user_data
        return jsonify({"message": "User added", "user": user_data}), 201
    else:
        return jsonify({"error": "Invalid data or user already exists"}), 400


if __name__ == "__main__":
    app.run(debug=True)
