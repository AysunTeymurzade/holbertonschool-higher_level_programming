#!/usr/bin/python3
"""
This module contains the function class_to_json that
returns the dictionary description of a class instance
for JSON serialization.
"""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization of obj."""
    return obj.__dict__
