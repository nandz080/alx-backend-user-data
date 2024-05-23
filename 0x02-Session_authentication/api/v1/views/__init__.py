#!/usr/bin/env python3
""" Docstring for the module """
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

# Import views here
from api.v1.views.index import *
from api.v1.views.users import *

# Import User model to load users from file
from models.user import User

User.load_from_file()
