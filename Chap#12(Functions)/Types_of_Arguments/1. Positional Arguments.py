"""
Jab aap function call karte waqt arguments ka exact order (position) maintain karte hain,
toh unhein positional arguments kehte hain. Matlab jis tarah parameters define kiye hain,
values bhi usi tarah deni parti hain. Agar order badal do, 
toh output ya meaning change ho jata hai.
"""

#  # Positional Arguments
# def info(name, age):
#     print(name, age)
# info("Areeba", 18)

x=500
y=500
print(y is x) 


def introduce(name, age):
    print(f"Main {name} hoon, aur meri umar {age} saal hai.")

# Yeh Positional Arguments hain (Order matter karta hai)
introduce("Ali", 22)  # Sahi output dega

# Agar order change kar diya toh logic kharab ho jayegi:
introduce(22, "Ali")  # Output: Main 22 hoon, aur meri umar Ali saal hai (Galat!)