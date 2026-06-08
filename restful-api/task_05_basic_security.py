#!/usr/bin/python3


from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt,
    jwt_required
)
from werkzeug.security import check_password_hash, generate_password_hash

# Create the Flask application
app = Flask(__name__)

# Configure the secret key used to sign and verify JWT tokens
app.config["JWT_SECRET_KEY"] = "super-secret-key"

# Create the Basic Authentication helper
auth = HTTPBasicAuth()

# Create the JWT manager used to handle token creation and validation
jwt = JWTManager(app)

# Store users in memory
# Each user has:
# - username: unique identifier
# - password: hashed password for secure verification
# - role: permission level used for role-based access control
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verify user credentials for Basic Authentication."""
    # Try to find the user by username
    user = users.get(username)

    # If the user does not exist, authentication fails
    if user is None:
        return None

    # Compare the provided password with the stored hashed password
    if check_password_hash(user["password"], password):
        # Return the username when authentication succeeds
        return username

    # Return None if the password is incorrect
    return None


@auth.error_handler
def basic_auth_error(status):
    """Return a 401 response for Basic Authentication failures."""
    # Always return a consistent unauthorized response
    return jsonify({"error": "Unauthorized"}), 401


@jwt.unauthorized_loader
def handle_missing_token(error):
    """Handle requests with missing JWT tokens."""
    # This runs when no token is provided in a protected route
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token(error):
    """Handle requests with malformed or invalid JWT tokens."""
    # This runs when the provided token cannot be decoded or verified
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token(jwt_header, jwt_payload):
    """Handle requests with expired JWT tokens."""
    # This runs when the token is valid but no longer active
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token(jwt_header, jwt_payload):
    """Handle requests with revoked JWT tokens."""
    # This runs if token revocation is being used and the token is revoked
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_fresh_token(jwt_header, jwt_payload):
    """Handle requests that require a fresh JWT token."""
    # This runs when a route requires a fresh token but a non-fresh one is used
    return jsonify({"error": "Fresh token required"}), 401


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """Return a success message when Basic Authentication succeeds."""
    # If valid username and password are provided, access is granted
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Authenticate a user and return a JWT access token."""
    # Read the request body as JSON
    # silent=True prevents Flask from raising an exception for invalid JSON
    data = request.get_json(silent=True)

    # Ensure the request body is a valid JSON object
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid credentials"}), 401

    # Extract the username and password sent by the client
    username = data.get("username")
    password = data.get("password")

    # Find the user in the in-memory user dictionary
    user = users.get(username)

    # Reject the request if:
    # - the username does not exist
    # - the password does not match the stored hash
    if user is None or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Create a JWT access token
    # identity stores the username
    # additional_claims stores extra data such as the user's role
    access_token = create_access_token(
        identity=username,
        additional_claims={"role": user["role"]}
    )

    # Return the generated token to the client
    return jsonify({"access_token": access_token})


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """Return a success message when JWT Authentication succeeds."""
    # This route can only be accessed with a valid JWT token
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Allow access only to authenticated users with the admin role."""
    # Extract all claims stored inside the current JWT token
    claims = get_jwt()

    # Check the user's role from the token claims
    if claims.get("role") != "admin":
        # Deny access if the authenticated user is not an admin
        return jsonify({"error": "Admin access required"}), 403

    # Return success if the user has the admin role
    return "Admin Access: Granted"


if __name__ == "__main__":
    # Start the Flask development server
    # By default, it runs on http://127.0.0.1:5000
    app.run()
