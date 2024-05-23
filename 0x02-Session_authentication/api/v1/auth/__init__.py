#!/usr/bin/env python3
""" Module for instantiating
"""

from .auth import Auth
from .basic_auth import BasicAuth
from .session_auth import SessionAuth
from .session_exp_auth import SessionExpAuth
from .session_db_auth import SessionDBAuth

__all__ = ['Auth', 'BasicAuth', 'SessionAuth', 'SessionExpAuth', 'SessionDBAuth']
