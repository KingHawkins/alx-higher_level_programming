#!/usr/bin/python3

"""defines a student"""


class Student:
    """Representation of class student"""
    my = ['first_name', 'last_name', 'age']
    def __init__(self, first_name, last_name, age):
        """Initializes the student details"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary rep of student"""
        if attrs != None:
            return ({item: getattr(self, item)
                for item in sorted(attrs) if item in Student.my})
        return{
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
                }

    def reload_from_json(self, json):
        """replaces all attributs of student instance"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except FileNotFoundError:
                pass
