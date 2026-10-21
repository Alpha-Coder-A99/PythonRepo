#Use to delete object properties or object itself
# del s1.name
# del s1


class Student:
    def __init__(self,name):
        self.name=name

s1=Student("Mariyam")
print(s1.name)

del s1
# print(s1.name) # Error: name 's1' is not defined , will accured

class Car:
    def __init__(self,brand):
        self.brand=brand

c1=Car("Mercedes")
print(s1.brand)

del c1
print(c1.brand) # Error: name 'c1' is not defined , will accured
     