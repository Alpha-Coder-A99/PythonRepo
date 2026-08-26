"""
Create a dictionary of 3 students with their marks in 3 subjects, "
then calculate total marks for each student.
"""
Students = {
    "Std1": {"name": "Fatima", "marks": {"Math": 98, "physics": 97, "Computer": 95}},
    "Std2": {"name": "Mariyam", "marks": {"Math": 96, "physics": 99, "Computer": 90}},
    "Std3": {"name": "Halima", "marks": {"Math": 98, "physics": 99, "Computer": 99}}
}


for student_id, student_info in Students.items():
    name = student_info["name"]
    marks_dict = student_info["marks"]
    total = sum(marks_dict.values())
    print(f"{name}'s total marks are: {total}")