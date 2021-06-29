#!/usr/bin/python3
"""
    This is the class to store objects
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Class FileStorage that serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    """------------------------------- METHODS ----------------------------"""
    def all(self):
        """
        Method to return the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Method to sets in __objects the obj with key
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Method to serialize __objects to the JSON file
        """
        save_dict = {}
        for key, value in self.__objects.items():
            save_dict[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as my_file:
            json.dump(save_dict, my_file)

    def reload(self):
        """
            Method to deserealizes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as my_file:
                objects = json.load(my_file)

            for key in objects:
                self.__objects[key] = (classes[objects[key]["__class__"]]
                                       (**objects[key]))

        except FileNotFoundError:
            pass
