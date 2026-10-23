#A Class Method is a method that is bound to the class itself,
#  rather than to a specific instance (object) of the class.
# A method decorated with @classmethod that receives the class (cls) 
# as its first argument instead of the instance (self),
#  allowing it to access and modify class-level state.
class person :
    name="anonymous"

    def ChangeName(self,name):
        self.__class__.name="Batool"
p1=person()
p1.ChangeName("Batool")
print(p1.name)
print(person.name)
# IN methods way
class person :
    name="anonymous"
    @classmethod
    def ChangeName(cls,name):
        cls.name=name
    
p1=person()
p1.ChangeName("Batool")
print(p1.name)
print(person.name)

#A Class Method is a method that is bound to the class itself,
#  rather than to a specific instance (object) of the class.
class Car:
    wheel=4 # class attribute  

    def __init__(self,color):
        self.color=color #Instance attributes

    def make_sound(self): #Instance method
            return "Gha Gha Gha"