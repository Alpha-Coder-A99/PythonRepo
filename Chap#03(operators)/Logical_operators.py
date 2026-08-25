#  Logical Operators  

a = True
b = False

print("Logical Results:")

# 1. AND (Dono ka True hona lazmi hai)
print(f"True AND False: {a and b}")   # Result: False

# 2. OR (Koi ek bhi True ho toh kaam chal jayega)
print(f"True OR False: {a or b}")     # Result: True

# 3. NOT (Ulta kar deta hai - True ko False, False ko True)
print(f"NOT True: {not a}")           # Result: False

# Ek real example:
age = 18
has_license = True

# Kya banda drive kar sakta hai? (Age 18+ AND license hona chahiye)
can_drive = (age >= 18) and has_license
print(f"Kya driving ki ijazat hai? {can_drive}") # Result: True