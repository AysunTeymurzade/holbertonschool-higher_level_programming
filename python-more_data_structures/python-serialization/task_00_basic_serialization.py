#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    with open(filename, "w") as write:
        json.dump(data, write)

def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    file = open(filename)   
    data = json.load(file)
    return data