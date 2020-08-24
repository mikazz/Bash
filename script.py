from time import sleep
from time import localtime


class User(object):
    def __new__(cls, name, age):
        """
            Constructor
            is called when the class is ready to instantiate itself.
            is always a static method of the class, even if no static
            method decorator is added.
        """
        print("Creating Instance")
        return object.__new__(cls)
        
    def __init__(self, name, age):
        """Initializator"""
        self.name = name
        self.age = age

class Foo(object):
    def __new__(cls, *args, **kwargs):
        print("Creating Instance")
        return super(Foo, cls).__new__(cls)

    def __init__(self, a, b):
        self.a = a
        self.b = b
 
    def bar(self):
        pass

foo = Foo(2, 3)


