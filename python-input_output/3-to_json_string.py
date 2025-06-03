#!/usr/bin/python3
"""
Module that contains a function to convert a Python object to a JSON string.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj (any): The Python object to be serialized.

    Returns:
        str: JSON string representation of the object.
    """
    return json.dumps(my_obj)
