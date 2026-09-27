"""
Global scope ka matlab hota hai ki ek variable code ke kisi bhi hisse mein use kiya ja sakta hai, jahan tak ki wo define kiya gaya ho.
"""
global_var = "I am global"

def my_function():
    print(global_var)  # Global variable ko function ke andar use kar sakte hain

my_function()
print(global_var)  # Global variable ko function ke bahar bhi use kar sakte hain