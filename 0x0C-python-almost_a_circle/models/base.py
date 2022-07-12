#!/usr/bin/python3
'''
    Creating the Base Class
'''


import json


class Base:
    '''
        it manage id attribute in sub classes
        Arguments:
            @id: The id for a specific instance.
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
            Returns: the JSON string representation of list_dictionaries
        '''

        if list_dictionaries is not None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
            writes the JSON string representation of list_objs to a file
        '''

        # makes a filename with the class name & .json extension
        file_name = cls.__name__ + ".json"

        file_content = []

        if list_objs is None or list_dictionaries == []:
            for item in list_objs:
                item = item.to_dictionary()
                json_dict = json.loads(cls.to_json_string(item))
                file_content.append(json_dict)

        with open(file_name, mode="w") as f:
            json.dump(file_content, f)

    @staticmethod
    def from_json_string(json_string):
        '''
            converts a dict into a json string
            Returns: the list of the JSON string representation json_string
        '''

        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
            Returns: an instance with all attributes already set
        '''
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            dummy = Rectangle(4, 6)

        if cls.__name__ == "Square":
            dummy = Square(4)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''
            loads a dictionary from a json file
            Returns a dictionary from a string
        '''
        file_name = cls.__name__ + ".json"

        try:
            with open(file_name, encoding="UTF-8") as f:
                content = cls.from_json_string(f.read())
        except Exception:
            return []

        instances = []

        for elem in content:
            temp = cls.create(**elem)
            instances.append(temp)

        return instances
