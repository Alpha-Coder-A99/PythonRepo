"""
Positional Parameters woh parameters hote hain jo aap function definition ke waqt banate hain.
 Jab aap function call karte hain, toh values ka order (position) bilkul theek hona chahiye,
 kyunke Python pehli value pehle parameter ko aur doosri value doosre parameter ko deta hai.

"""

def student_info(name, age):  # name aur age positional parameters hain
    print(f"Name: {name}, Age: {age}")

# Function Call (Order important hai)
student_info("Ali", 22)  
# Output: Name: Ali, Age: 22 ("Ali" 'name' ko mila, 22 'age' ko)

# Agar order change kar diya:
student_info(22, "Ali")  
# Output: Name: 22, Age: Ali (Logic kharab ho gayi!)