#!/usr/bin/python3
"""
Module that contains a function to convert a JSON string to a Python object.
"""

import json


def from_json_string(my_str):
    """
    Returns the Python object representation of a JSON string.

    Args:
        my_str (str): The JSON string to deserialize.

    Returns:
        object: Python data structure (e.g., dict, list) from the JSON string.
    """
    return json.loads(my_str)
