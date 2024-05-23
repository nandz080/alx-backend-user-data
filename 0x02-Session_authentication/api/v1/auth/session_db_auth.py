#!/usr/bin/env python3
""" Module for SessionDBAuth
"""

from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime

class SessionDBAuth(SessionExpAuth):
    def create_session(self, user_id=None):
        if user_id is None:
            return None

        session_id = super().create_session(user_id=user_id)
        if session_id is None:
            return None

        new_session = UserSession(user_id=user_id, session_id=session_id)
        new_session.save()

        return session_id

    def user_id_for_session_id(self, session_id=None):
        if session_id is None:
            return None

        user_session = UserSession.search({'session_id': session_id})
        if not user_session:
            return None

        user_session = user_session[0]

        if self.session_duration <= 0:
            return user_session.user_id

        created_at = user_session.created_at
        if created_at is None:
            return None

        expiration_time = created_at + timedelta(seconds=self.session_duration)
        if expiration_time < datetime.now():
            return None

        return user_session.user_id

    def destroy_session(self, request=None):
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_session = UserSession.search({'session_id': session_id})
        if not user_session:
            return False

        user_session = user_session[0]
        user_session.remove()

        return True
