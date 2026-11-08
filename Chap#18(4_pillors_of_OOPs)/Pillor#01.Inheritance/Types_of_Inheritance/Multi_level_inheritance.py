"""
This is the basics case where we have:
Grandparent class -> Parent class ->Child class
The attributes and methods are passed on through all the classes
"""
class Grandparent:
    def old_story(self):
        return "Legacy story"

class Parent(Grandparent):
    def work(self):
        return "Office work"

class Child(Parent):
    pass
class Car:
    @staticmethod
    def start():
        print("Car is starting...")
    @staticmethod
    def stop():
        print("Car is stoping...")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type=type

car1=Fortuner("disel")
car1.start()