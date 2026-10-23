class Student:
    school="Inspire"#class attributes
    name="Kiran"
    def __init__(self,fullname,marks):
        self.fullname=fullname #object attributes
        self.marks=marks
        print("adding new student in  data base...  ")
    def Welcome(self):
        print("Welcome Student",self.name)

    def get_marks(self):
        return self.marks

s1=Student("Raha",56)
s1.Welcome()
print(s1.get_marks())