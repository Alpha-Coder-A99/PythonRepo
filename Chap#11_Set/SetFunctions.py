foods={"Apple","Samosa","kheer","Cholapatora","Sandwatch","Golgappy"}
print(type(foods))
print(foods)
print(len(foods))
foods.add("dates")
foods.remove("Samosa") # because this is unhealthy😁😜
print(foods)
# union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
print(result)

python_students = {"Fatima", "Sara", "Areeba"}
ai_students = {"Mariyam", "Areeba", "Sara"}
all_students = python_students.union(ai_students)
print(all_students)
A = {1, 2, 3}
B = {3, 4, 5}
C = A.intersection(B)
print(C)
python_students = {"Fatima", "Sara", "Areeba"}
ai_students = {"Sara", "Ayesha", "Areeba"}
common = python_students.intersection(ai_students)
print(common)
#Difrence
A = {10, 20, 30}
B = {20, 30, 40}
C = A.difference(B)
print(C)
python_students = {"Fatima", "Sara", "Areeba"}
ai_students = {"Fatima", "Amina", "Areeba"}

only_python = python_students.difference(ai_students)

print(only_python)