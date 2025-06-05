#!/usr/bin/python3
"""Defines a Student class with JSON serialization and deserialization."""


class Student:
    """Student class that can be serialized to and from JSON."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): List of attribute names to retrieve.
                If None, retrieve all attributes.

        Returns:
            dict: Dictionary of attributes filtered by attrs or all attributes.
        """
        if attrs is None:
            return self.__dict__.copy()

        filtered = {}
        for attr in attrs:
            if hasattr(self, attr):
                filtered[attr] = getattr(self, attr)
        return filtered

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance from a JSON dictionary.

        Args:
            json (dict): Dictionary containing attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
