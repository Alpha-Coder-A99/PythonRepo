#An instance method works with instance(object) of the clas .
#  this method can accessand modify instance attributes
class Car:
    wheel=4 # class attribute  

    def __init__(self,color):
        self.color=color #Instance attributes

    def make_sound(self): #Instance method
            return "Gha Gha Gha"