#!/usr/bin/env python3
"""
Module for user authentication
"""

import bcrypt

def _hash_password(password: str) -> bytes:
    """Method for hashing a password using bcrypt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The salted hash of the password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
