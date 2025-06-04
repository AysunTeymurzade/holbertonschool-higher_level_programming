#!/usr/bin/python3
"""Function that returns the dictionary description for JSON serialization of an object."""


def class_to_json(obj):
    """Return the dictionary representation of a simple data structure."""
    return obj.__dict__
