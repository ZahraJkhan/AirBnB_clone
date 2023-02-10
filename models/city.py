#!/usr/bin/python3
"""This module creates a city class"""

from models.base_model import BaseModel


class City(BaseModel):
    """ inherits from BaseModel"""
    state_id = ""
    name = ""
