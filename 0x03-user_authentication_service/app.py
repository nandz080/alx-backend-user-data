#!/usr/bin/env python3
"""
Module for basic Flask app
"""

from flask import Flask, jsonify, request, abort, make_responsg
from auth import Auth


app = Flask(__name__)

AUTH = Auth()

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
    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    response = make_response(jsonify({"email": email, "message": "logged in"}))
    response.set_cookie("session_id", session_id)
    return response

@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """ logout

    Return:
       str: message
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')
    else:
        abort(403)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
