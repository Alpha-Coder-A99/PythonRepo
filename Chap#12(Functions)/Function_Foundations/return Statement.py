"""
return statement function ke andar use hota hai
taake function apna kaam (calculation ya processing) mukammal karne ke baad result
wapas (return) kar sake.
"""
def add(a, b):
    result = a + b
    return result  # Yeh value function se bahar bhej raha hai

# Function ko call kiya aur return ki hui value ko variable mein save kar liya
output = add(5, 3)
print(output)  # Output: 8


"return actual value wapas deta hai taake aap use dubara kisi aur kaam mein use kar sakein."