#!/usr/bin/python3
from flask import Flask, jsonify, request


# Create the Flask application instance
app = Flask(__name__)

# Store users in memory using a dictionary
# The username is the key and the full user object is the value
users = {}


@app.route("/", methods=["GET"])
def home():
    """Return a welcome message for the root endpoint."""
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def get_usernames():
    """Return a list of all usernames stored in memory."""
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def status():
    """Return a simple API status message."""
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return the full user object for the given username."""
    # Check whether the requested user exists
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    # Return the matching user object
    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user from the JSON body of the request."""
    # Try to parse the incoming JSON body
    try:
        data = request.get_json(force=True)
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    # Ensure the parsed body is a dictionary
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    # Extract the username from the request body
    username = data.get("username")

    # Check whether the username field was provided
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Prevent duplicate usernames
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add the new user to the in-memory dictionary
    users[username] = data

    # Return a success message and the created user
    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    # Run the Flask development server
    app.run()
