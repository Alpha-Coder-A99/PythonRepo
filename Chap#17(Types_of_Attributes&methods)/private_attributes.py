#private attributes and methods are meant to be used only within the class and are not accessible from outside the class
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self._acc_pass=acc_pass
    def reset_pass(self):
        print(self._acc_pass)

acc1=Account("12345","abcde")

print(acc1._acc_pass)
print(acc1.reset_pass())

#2nd way of private attributes 
class Person:
    __name="anonymous"

    def hello():
        print("Hello Users!")


p1=Person()
# print(p1._name)
# print(p1.hello())