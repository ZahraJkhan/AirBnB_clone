#!/usr/bin/python3
"""This module creates a review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ inherits from Basemodel """
    place_id = ""
    user_id = ""
    text = ""
