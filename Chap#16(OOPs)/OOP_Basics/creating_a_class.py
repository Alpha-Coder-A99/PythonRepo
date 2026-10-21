#Creating a class in Python
#A class is created with the basic keyword "class" and the name infront of it 
# The name of the class should be in PascalCase. The body of the class is defined by indentation.
class Student:
    name="Alpha"#This is a class variable. It is shared by all instances of this class.it called the body of the class

#Creating Objects/instances of classes
s1=Student()
print(s1.name)
print(s1)


class Car:
    name="BMW"
    model="X5"
    color="Black"
    price=500000

c1=Car()
print(c1.name)
print(c1.model)
print(c1.color)
print(c1.price)

class Laptop:
    name="Dell"
    model="Inspiron"
    color="Silver"
    price=60000
lap1=Laptop()
print(lap1.name)
print(lap1.model)
print(lap1.color)
print(lap1.price)


class Mobile:
    name="Samsung"
    model="Galaxy"
    color="Blue"
    price=30000

m1=Mobile()
print(m1.name)
print(m1.model)
print(m1.color)
print(m1.price)

class Bike:
    name="KTM"
    model="Duke"
    color="Orange"
    price=200000

b1=Bike()
print(b1.name)
print(b1.model)
print(b1.color)
print(b1.price)

class college:
    name="Aspire college"
    location="Mainwali"
    rank=1
    students=1000
    char="Dicipline, modesty and hardwork"

coll1=college()
print(coll1.name)
print(coll1.location)
print(coll1.rank)
print(coll1.students)
print(coll1.char)




#There are two types of thing that can be stored in class
# first one is Attributes: These are the variables that belong to the class. They are used to store data about the object.
# second one is Methods: These are the functions that belong to the class. They are used to define the behavior of the object.