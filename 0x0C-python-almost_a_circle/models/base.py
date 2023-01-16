#!/usr/bin/python3

"""importing json"""


import json
import csv
import os
import turtle

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
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts dictionary to json string"""
        if list_dictionaries == [] or list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """retruns the list of the JSON string repr json_string"""
        if json_string == [] or json_string is None:
            return []
        return json.loads(json_string)

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

    @classmethod
    def create(cls, **dictionary):
        """returns the instance with all attributes set"""
        if cls.__name__ == 'Rectangle':
            new = cls(10, 10)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """loads from json file"""
        data = ''
        file = '{}.json'.format(cls.__name__)
        try:
            with open(file, 'r', encoding='utf-8') as load:
                data = cls.from_json_string(load.read())
        except FileNotFoundError:
            return []
        finally:
            empty = []
            for item in data:
                empty.append(cls.create(**item))
            return empty

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves to csv file"""
        file = '{}.csv'.format(cls.__name__)
        if os.path.exists(file) is False:
            return []
        if cls.__name__ == 'Rectangle':
            with open(file, 'w', newline='') as out:
                new = csv.writer(out)
                new.writerow(list_objs)
        else:
            with open(file, 'w', newline='') as out:
                new = csv.writer(out)
                new.writerow(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """loads from csv file"""
        file = '{}.csv'.format(cls.__name__)
        if os.path.exists(file) is False:
            return []
        with open(file, newline='') as r:
            read = csv.reader(r, delimiter=' ', quotechar=',')
            arr = []
            for row in read:
                arr.append(row)
            return arr

    def draw(list_rectangles, list_squares):
        """draws all rectangles and squares\
                Based on the arguments given
        Args:
            list_squares(obj): list of squares
            list_rectangles(obj): list of rectangles
        """
        window = turtle.Screen()
        draw = turtle.Turtle()
        draw.color('blue')
        draw.pensize(3)
        mat, other, x, cum = [], [], [], []
        for item in list_squares:
            new = item.to_dictionary()
            mat.append(new)
        for item in mat:
            x.append(item['size'])
        draw.forward(x[1:][0])
        draw.left(90)
        draw.forward(x[1:][0])
        draw.left(90)
        draw.forward(x[1:][0])
        draw.left(90)
        draw.forward(x[1:][0])
        draw.left(90)
        draw.color('green')
        draw.forward(x[1:][1])
        draw.left(90)
        draw.forward(x[1:][1])
        draw.left(90)
        draw.forward(x[1:][1])
        draw.left(90)
        draw.forward(x[1:][1])
        draw.left(90)
        for item in list_rectangles:
            other.append(item.to_dictionary())
        for item in other:
            cum.append(item['width'])
            cum.append(item['height'])
        draw.color('yellow')
        draw.forward(cum[0])
        draw.left(90)
        draw.forward(cum[1])
        draw.left(90)
        draw.forward(cum[0])
        draw.left(90)
        draw.forward(cum[1])
        draw.left(90)
        draw.color('black')
        draw.forward(cum[2])
        draw.left(90)
        draw.forward(cum[3])
        draw.left(90)
        draw.forward(cum[2])
        draw.left(90)
        draw.forward(cum[3])
        draw.left(90)
        draw.color('red')
        draw.forward(cum[4])
        draw.left(90)
        draw.forward(cum[5])
        draw.left(90)
        draw.forward(cum[4])
        draw.left(90)
        draw.forward(cum[5])
        draw.left(90)
