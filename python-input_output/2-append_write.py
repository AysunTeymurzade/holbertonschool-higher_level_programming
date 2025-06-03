#!/usr/bin/python3
"""
This module provides a function that appends a string to a UTF-8 text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns
    the number of characters added.

    Args:
        filename (str): Name of the file.
        text (str): Text to append.

    Returns:
        int: Number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
