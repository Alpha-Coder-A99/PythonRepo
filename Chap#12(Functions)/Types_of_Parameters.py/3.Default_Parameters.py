"""
Default Parameter woh parameter hota hai jise 
aap function definition ke waqt hi ek default (pakki) value de dete hain.
Agar function call karte waqt aap us parameter ki value dena bhool jayein, 
toh Python khud-ba-khud wahi default value use kar leta hai.
"""
# Yahan 'city="Lahore"' ek default parameter hai
def greet(name, city="Lahore"):
    print(f"Hello {name}, you are from {city}.")

# 1. Jab value na dein (Default use hoga):
greet("Ali")  
# Output: Hello Ali, you are from Lahore.

# 2. Jab apni marzi ki value dein (Default override ho jayega):
greet("Sara", "Karachi")  
# Output: Hello Sara, you are from Karachi.
"""
Default parameters hamesha function definition ke akhir mein aate hain. 
Non-default parameters ke baad hi default parameters likhe jate hain.
"""