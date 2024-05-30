#!/usr/bin/env python3
"""
Module for user authentication service.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """
    Class defines user model for the users table
    """
    __tablename__ = 'users'

    id: Column = Column(Integer, primary_key=True)
    email: Column = Column(String(250), nullable=False)
    hashed_password: Column = Column(String(250), nullable=False)
    session_id: Column = Column(String(250), nullable=True)
    reset_token: Column = Column(String(250), nullable=True)
