#!/usr/bin/env python3
""" Module for session expiration auth
"""

from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
import os

class SessionExpAuth(SessionAuth):
    """ Session Authentication with Expiration
    """
    def __init__(self):
        """ Initialize SessionExpAuth
        """
        super().__init__()
        self.session_duration = int(os.getenv("SESSION_DURATION", 0))

    def create_session(self, user_id=None):
        """ Create a Session ID with expiration
        """
        session_id = super().create_session(user_id)
        if session_id:
            session_dict = {
                "user_id": user_id,
                "created_at": datetime.now()
            }
            self.user_id_by_session_id[session_id] = session_dict
            return session_id
        return None

    def user_id_for_session_id(self, session_id=None):
        """ Return a User ID based on a Session ID with expiration
        """
        if session_id is None:
            return None

        session_dict = self.user_id_by_session_id.get(session_id)
        if not session_dict:
            return None

        user_id = session_dict.get("user_id")
        created_at = session_dict.get("created_at")
        if not user_id or not created_at:
            return None

        if self.session_duration <= 0:
            return user_id

        expiration_time = created_at + timedelta(seconds=self.session_duration)
        if expiration_time < datetime.now():
            del self.user_id_by_session_id[session_id]
            return None

        return user_id
