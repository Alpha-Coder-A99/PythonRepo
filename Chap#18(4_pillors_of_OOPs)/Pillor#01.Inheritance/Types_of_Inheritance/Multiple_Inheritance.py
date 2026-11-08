"""
Multiple_Inheritance means there wil be 2 parent classes and only one child class
and the child class will be inherit al the atributes and methods of both parent classes
"""
class Animals:
    def __init__(self,name):
        self.name=name

class Humans:
    def __init__(self,id):
        self.id = id

class Robot (Humans,Animals):
    def __init__(self,id,name):
        Humans.__init__(self,id)
        Animals.__init__(self,name)

Robo=Robot(56,"Alpha")
print(Robo.id)


class Father:
    def skills_father(self):
        return "Gardening"

class Mother:
    def skills_mother(self):
        return "Cooking"

class Child(Father, Mother):
    pass

# class A:
#     varA="WElcome to class A"
# class B:
#     varb="WElcome to class B"
# class C(A,B):
#     varc="WElcome to class C"

# s1=C()
# print(s1.varc)
# print(s1.varA)
# print(s1.varb)
class Car:
    @staticmethod
    def start():
        print("Car is starting...")
    @staticmethod
    def stop():
        print("Car is stoping...")

class ToyotaCar():
    def __init__(self,brand):
        self.brand=brand


class Fortuner(ToyotaCar,Car):
    def __init__(self,type):
        self.type=type

car1=Fortuner("disel")
car1.start()
car1.stop()