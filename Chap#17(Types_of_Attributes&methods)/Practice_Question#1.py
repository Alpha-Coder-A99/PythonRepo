#Create a Student Class thats takes name&marks of 3 subjects as argumnts in constructor.Then create a method to print the average.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    @staticmethod
    def hello():
        print("hello users")

    def get_average(self):
        total_sum = 0
        for val in self.marks:
            total_sum += val
        
        
# Print loop se bahar hona chahiye taake final result aaye
        average = total_sum / 3
        print(f"Hi! {self.name}, your average score is: {average}")

s1 = Student("Fatima", [34, 89, 78])
s1.get_average()
s1.hello()