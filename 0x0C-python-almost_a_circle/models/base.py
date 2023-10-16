#!/usr/bin/python3
""" Base module """
import json


class Base:
    """ This class will be the “base” of all other classes in this project """

    __nb_objects = 0

    def __init__(self, id=None):
        """ construction class """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ this return json to list_dictionary """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ This writes the JSON string represennt of list_objs to a file """

        filename = cls.__name__ + ".json"

        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")

            else:
                obj_dict = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(obj_dict))

    @staticmethod
    def from_json_string(json_string):
        """ returns list of the JSON string representation json_string """

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """

        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                data = file.read()
                data = cls.from_json_string(data)
                return [cls.create(**d) for d in data]
        except FileNotFoundError:
            return []
