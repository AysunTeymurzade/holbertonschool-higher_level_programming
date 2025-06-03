#!/usr/bin/python3
"""
This module provides a function that writes a string to a text file (UTF8),
creating the file if it does not exist, and overwriting its content if it does.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8), overwriting its content,
    and returns the number of characters written.

    Args:
        filename (str): Name of the file to write to.
        text (str): Text to write.

    Returns:
        int: Number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
