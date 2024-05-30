#!/usr/bin/env python3
"""
Module for user authentication
"""

from db import DB
from uuid import uuid4
import bcrypt
from user import User
from sqlalchemy.orm.exc import NoResultFound

def _hash_password(password: str) -> bytes:
    """Method for hashing a password using bcrypt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The salted hash of the password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def _generate_uuid() -> str:
    """generate uuid

    Returns:
        str: representation of a new UUID
    """
    return str(uuid4())

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """register a user

        Args:
            email (str): email of user
            password (str): password of user

        Returns:
            User: user registered
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """Validate login credentials.

        Args:
            email (str): The email of the user.
            password (str): The password to validate.

        Returns:
            bool: True if login credentials are valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)
        except NoResultFound:
            return False
