#when one class is derived/inherit some features from another class 
# then it is called inheritance
class Parent :
    def __init__(self,char):
        self.char=char
        # self.cast=cast
        # self.mission=mission

class Child(Parent) :
    pass

p1=Parent("Intelligance")
print(p1.char)
c1=Child()
print(c1.char)