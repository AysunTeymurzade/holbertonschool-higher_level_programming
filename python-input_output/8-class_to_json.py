#!/usr/bin/python3
"""Module that defines a function to retrieve the dictionary
representation of a class instance for JSON serialization.
"""


def class_to_json(obj):
    """Return the dictionary description with simple data structure
    (list, dictionary, string, integer, and boolean) for JSON serialization
    of an object.

    Args:
        obj (object): An instance of a class whose attributes are JSON serializable.

    Returns:
        dict: The dictionary representation of obj's attributes.
    """
    return obj.__dict__
