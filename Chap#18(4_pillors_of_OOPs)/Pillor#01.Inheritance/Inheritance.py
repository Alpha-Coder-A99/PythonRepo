#when one class is derived/inherit some features (properties & methods)
# from another class then it is called inheritance
"""
Inheritance allows a new class (child) to adopt the attributes and methods of an existing class (parent), 
promoting code reusability.
"""

#Parent class
"Parent class is a class which inhert their propertie to another class.It is also known base class"
#Child class
"Child class is a class which inhert some properties from another class .It is also known as derived class"

#syntax of inheritance
class Parent:
    def __init__(self,char):
        self.char=char
    def details(self):
        print(f"My characteristics are {self.char}")
class Child(Parent):
    pass

obj1=Parent("Intellegence")
obj2=Child("Humour")
print(obj2.char)
obj2.details()
obj1.details()