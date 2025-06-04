#!/usr/bin/python3
"""Defines a class Student with optional attribute filtering for JSON serialization."""


class Student:
    """Class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of the Student instance.
        If attrs is a list of strings, return only those attributes included.
        Otherwise, return all attributes.
        """
        if type(attrs) == list and all(type(attr) == str for attr in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__
