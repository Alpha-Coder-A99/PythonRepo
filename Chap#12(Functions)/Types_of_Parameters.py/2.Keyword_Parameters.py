"""
Function Call ke waqt(Keyword Argument): 
Jab aap function call karte waqt naam se value passkarte hain (jaise greet(name="Ali")).
"""
# Yeh function definition hai. Yahan '*' ke baad jo 'city' hai, woh Keyword Parameter hai.
def user_info(name, *, city):
    print(name, city)

# Jab call karenge, toh 'city' ke liye keyword argument dena lazmi hoga:
user_info("Ali", city="Lahore")  # Sahi hai

# Agar baghair keyword ke doge toh error aayega:
# user_info("Ali", "Lahore")  # Error!