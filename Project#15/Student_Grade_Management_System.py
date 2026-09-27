print("=== Welcome to my Student Grade Management System ===")

# Global dictionary
student_grades = {}

# 1. Adding a new student
def add_Student(name, grade):
    student_grades[name] = grade
    print(f"Added {name} with grade {grade}")

# 2. Updating
def update_Student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name}'s marks are updated to {grade}")
    else:
        print(f"{name} is not found")

# 3. Deleting
def delete_Student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} is deleted successfully...")
    else:
        print(f"{name} is not found...")

# 4. Viewing All
def display_all_student():
    if student_grades:
        print("\n--- Student Records ---")
        # Fix: added 's' to items()
        for name, grade in student_grades.items():
            print(f"Student: {name} | Grade: {grade}")
    else:
        print("Records are empty! Students Not Found...")

# 5. Main Loop
def main():
    while True:
        print("\n--- MENU ---")
        print("1. Add a new student")
        print("2. Update a student")
        print("3. Delete a student")
        print("4. View all Students")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter the name of Student: ")
            grade = int(input("Enter the marks of student: "))
            add_Student(name, grade)

        elif choice == 2:
            name = input("Enter the name of student to update: ")
            grade = int(input("Enter the marks of the student: "))
            update_Student(name, grade)

        elif choice == 3:
            name = input("Enter the name to delete: ")
            delete_Student(name)

        elif choice == 4:
            display_all_student()

        elif choice == 5:
            print("Closing the program... Allah Hafiz!")
            break
        else:
            print("INVALID Choice! Please try again.")

# Important: main function ko call karna
main()
