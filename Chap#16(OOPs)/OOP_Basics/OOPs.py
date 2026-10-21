#To map with real world scenarios , we started using objects in code THis is called object oriented programming

# object oriented programming

"""
🔹 OOP kya hota hai?

OOP ek programming style hai jisme hum real world cheezon ko code mein model karte hain.

👉 Real life example:

Insaan = object
Car = object
Mobile = object

Har object ke paas:

properties (attributes) → jaise car ka color, speed
actions (methods) → jaise car chalana, brake lagana"""

# 🔹 Python mein OOP ka base kya hai?

# Sab kuch start hota hai class se:

class Student:
    name = "Areeba"

# Yahan:

# Student = class
# name = attribute
# 🔹 Object kaise banta hai?
s1 = Student()
print(s1.name)

# 👉 s1 ek object hai jo class se bana hai
# 🔹 Thoda aur real banate hain (important 👀)
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Alpha_Coder")
print(s1.name)

# 👉 Yahan:
# __init__ = constructor (jab object banta hai tab run hota hai)
# self = object ko refer karta hai
# 🔹 Simple words mein summary:
# Class = blueprint
# Object = real thing
# __init__ = setup function
# self = current object
