"""
Keyword Arguments (jinhein named arguments bhi kehte hain) woh arguments hote hain 
jo function call karte waqt parameter ke naam (name) ke sath pass kiye jate hain.
Iska sabse bara faida yeh hai ke aapko order (position) yaad rakhne ki zaroorat nahi parti.
"""

def greet(msg, name):
    print(f"{msg}, {name}")

greet(name="Ali", msg="Hi") # Yahan humne keyword arguments diye (order matter nahi karta)

"""
Keyword Argument function call karte waqt confusion khatam karne ke liye hota hai taake pata ho 
kaunsi value kis parameter ko ja rahi hai.
"""