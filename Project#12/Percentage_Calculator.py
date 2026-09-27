# obtained_marks = 900
# total_marks = 1200

# # Percentage calculate karne ka formula
# percentage = (obtained_marks / total_marks) * 100

# print(f"Aapki percentage hai: {percentage:.2f}%")

def calculate( obtained_marks, total_marks):
    return (obtained_marks / total_marks) * 100

marks = float(input("Marks: "))
total = float(input("Total: "))

result=calculate(marks, total)
print(f"Aapki percentage hai: {result:.2f}%",)
    

