#Instance/object of a class is created using the class name and
# passing the arguments to the class constructor.
# 1. Class banayi (Sancha)
class Student:
    name = ""  # Khali attribute
    age = 0


# 2. Instances (Objects) banaye
s1 = Student()  # Pehla student object
s2 = Student()  # Doosra student object

# 3. Har object ko apni values di
s1.name = "Ali"
s1.age = 22

s2.name = "Sara"
s2.age = 20

# Access karna:
print(s1.name)  # Output: Ali
print(s2.name)  # Output: Sara

#Student ek Class hai.
# s1 aur s2 do alag-alag Instances (Objects) hain.

class Bag:
    name='Alpha'
    def color(self):
        print("The color of the bag is black")

b1=Bag()
print(b1.name)
result=b1.color()
print(result)

class Student:
    school="Inspire"#class attributes
    name="Kiran"
    def __init__(self,fullname,marks):
        self.fullname=fullname #object attributes
        self.marks=marks
        print("adding new student in  data base...  ")

s1=Student("Mariyam",56)
print(s1.fullname,s1.marks,Student.school)
s2=Student("Batool",78)
print(s2.fullname,s2.marks,Student.school)
