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
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        if path[-1] != '/':
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                if path.startswith(excluded_path[:-1]):
                    return False
            elif path == excluded_path or path == excluded_path + '/':
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
