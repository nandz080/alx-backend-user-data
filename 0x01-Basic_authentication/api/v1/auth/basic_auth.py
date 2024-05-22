#!/usr/bin/env python3
"""
Module for Basic Auth
"""

from api.v1.auth.auth import Auth

class BasicAuth(Auth):
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        if authorization_header is None or not isinstance(authorization_header, str):
            return None
        
        if not authorization_header.startswith("Basic "):
            return None
        
        base64_part = authorization_header.split(" ")[1]
        return base64_part
