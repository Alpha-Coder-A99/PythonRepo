#There are two types of thing that can be stored in class
# first one is Attributes: These are the variables that belong to the class. They are used to store data about the object.
# second one is Methods: These are the functions that belong to the class. They are used to define the behavior of the object.

class college:
    name="Aspire college"#Attributes
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


class Greeting:
    def hello(self):#Method
        print("Hello, welcome to the world of OOPs")
    def congrataulations(self):
        print("Congratulations, you have successfully learned OOPs")

g1=Greeting()
print(g1.hello())
print(g1.congrataulations())


class Animal:
    species="Dog"#Attributes

    def make_sound(self): #Methods
        print("Woof, woof")

# directly accesing the attributes and class and methods using the class 
print(Animal.species)#Acesing Attributes
print(Animal.make_sound(Animal()))#Accessing Methods
# we have to pass the class name as an argument to the method because
#  it is not bound to any instance of the class.