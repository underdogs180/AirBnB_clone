#!/usr/bin/python3
""" holds class User"""
from models.base_model import Base_model

class User(Base_model):
    """User Representation """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
