# Yeh dono tab use hote hain jab aapko pata na ho ke function ko kitne arguments pass kiye jayenge.
"""
Jab aap chahte hain ke function mein kitne bhi positional numbers/values pass kar sakein, 
toh *args use hota hai. Yeh saari values ko ek tuple mein pack kar deta hai.
"""

def add_func(*numbers):
    print(numbers)
    print(sum(numbers))

add_func(1, 2, 3, 4, 5)

# aghr hum numbers ko print karenge toh humein ek tuple milega jismein saari values hongi.

# *args

