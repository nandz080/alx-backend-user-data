#!/usr/bin/env python3
"""
Module for authentification systems
"""

from flask import request
from typing import TypeVar, List
User = TypeVar('User')

class Auth:
    """
    Class serves as template for all authentification systems to be implemented
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method that returns False -path and excluded_paths.
        """
        check = path
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != "/":
            check += "/"
        if check in excluded_paths or path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Method that returns None -request
        """
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> User:
        """
        Method that returns None - request
        """
        return None
