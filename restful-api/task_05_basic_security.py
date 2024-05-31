from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)
auth = HTTPBasicAuth()
# If necessary change this key (for signing tokens)
app.config['JWT_SECRET_KEY'] = 'mysecretkeydontelanyone'
jwt = JWTManager(app)

# Basic Auth users
users = {
    "user1": generate_password_hash("password1"),
    "admin1": generate_password_hash("adminpass")
}

# JWT Auth users
jwt_users = {
    "user1": "password",
    "admin1": "adminpass"
}


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username], password):
        return username

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    # to obtein JSON directly
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"error": "Username or password not provided"}), 400

    if username not in jwt_users or not jwt_users[username] == password:
        return jsonify({"error": "Bad username or password"}), 401

    # user_role = users.get(username, {}).get('role', 'user') # added rol-user
    access_token = create_access_token(identity=username, additional_claims={"role": user_role})
    return jsonify(access_token=access_token)


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user != 'admin1':
        return jsonify({"error": "Admin Access: Denied"}), 403
    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run(debug=True)
