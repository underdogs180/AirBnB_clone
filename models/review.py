#!/usr/bin/python3
""" holds class Review"""
from models.base_model import Base_model


class Review(Base_model):
    """Representation of Review """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
