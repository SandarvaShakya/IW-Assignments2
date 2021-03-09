"""
18. Find a package in the Python standard library for dealing with JSON.
    Import the library module and inspect the attributes of the module.
    Use the help function to learn more about how to use the module.
    Serialize a dictionary mapping 'name' to your name and 'age' to your
    age, to a JSON string. Deserialize the JSON back into Python.
"""

import json

some_dict = {
    "name": "Sandarva",
    "age": 19
}

serialize = json.dumps(some_dict, indent=4)

print("Serialized Json: ")
print(serialize)

deserialize = json.loads(serialize)
print("Deserialized back to Python: ")
print(deserialize)
