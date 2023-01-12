#!/usr/bin/python3

"""importing json"""
import json

"""base class"""


class Base:
    """Implementing the base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """Initializing the base class
        Args:
            id(id): id
        Raises:
            Exception
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


    @staticmethod
    def to_json_string(list_dictionaries):
        """converts dictionary to json string"""
        if len(list_dictionaries) == 0 or list_dictionaries == None:
            return '[]'
        return json.dumps(list_dictionaries)


    @classmethod
    def save_to_file(cls, list_objs):
        """writes json representation of an object to a file"""
        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dic)

        with open(filename, 'w') as f:
            f.write(lists)
