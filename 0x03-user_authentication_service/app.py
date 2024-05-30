#!/usr/bin/env python3
"""
Module for basic Flask app
"""

from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth
import logging

app = Flask(__name__)
AUTH = Auth()

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/', methods=['GET'])
def index():
    """GET route that returns a JSON payload"""
    return jsonify({"message": "Bienvenue"})

@app.route('/users', methods=['POST'])
def register_user():
    """Register a new user"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

@app.route('/sessions', methods=['POST'])
def login():
    """POST /sessions route to log in a user"""
    email = request.form.get('email')
    password = request.form.get('password')

    logging.debug(f"Attempting to log in user: {email}")
    
    if not AUTH.valid_login(email, password):
        logging.debug("Invalid login credentials")
        abort(401)
    
    session_id = AUTH.create_session(email)
    response = make_response(jsonify({"email": email, "message": "logged in"}))
    response.set_cookie("session_id", session_id)
    
    logging.debug(f"User {email} logged in successfully with session_id {session_id}")
    return response

@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """Logout user by deleting the session"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        logging.debug(f"User {user.email} logged out successfully")
        return redirect('/')
    else:
        logging.debug("User not found or session invalid")
        abort(403)

@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile() -> str:
    """Get user profile"""
    session_id = request.cookies.get('session_id')
    if session_id is None:
        logging.debug("No session_id cookie found")
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        logging.debug("Invalid session_id or user not found")
        abort(403)

    logging.debug(f"Profile requested for user: {user.email}")
    return jsonify({"email": user.email}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

