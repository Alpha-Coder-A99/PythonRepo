# Yeh dono tab use hote hain jab aapko pata na ho ke function ko kitne arguments pass kiye jayenge.
"""
Jab aap chahte hain ke function mein kitne bhi named (keyword) arguments pass kiye ja sakein, 
toh **kwargs use hota hai. Yeh saari key-value pairs ko ek dictionary mein pack kar deta hai.
"""
"**kwargs"

9
def print_user_info(**kwargs):
    print(kwargs)

# Yahan humne 'city' extra pass kiya hai jo function mein define nahi hai
print_user_info(name="Ali", age=22, city="Lahore")