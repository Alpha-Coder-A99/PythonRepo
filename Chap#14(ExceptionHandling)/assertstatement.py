"""
assert statement Python mein aik debugging tool hai jo yeh check karna ke liye use hota hai 
ke kya aapki koi condition True hai ya nahi.
Agar condition True ho, toh code khamoshi se aage chal padta hai.
Agar condition False ho, toh yeh foran AssertionError throw kar deta hai.
""" 
age = int(input("Enter your age: "))

# Hum check kar rahe hain ke age 18 ya us se zyada honi chahiye
assert age >= 18, "Age 18 se kam hai, access nahi mil sakti!"
print("Access granted, age is 18 or above.")