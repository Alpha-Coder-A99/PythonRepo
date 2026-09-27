"""
Default Arguments woh values hoti hain jo aap function definition mein hi set kar dete hain.
Agar function call karte waqt aap koi value na dein, 
toh Python khud-ba-khud woh default value use kar leta hai.
"""

def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("Ali")         # Output: Hello, Ali! (default use hua)
greet("Sara", "Hi")  # Output: Hi, Sara! (custom value di)


# Default arguments hamesha non-default arguments ke baad aane chahiye.