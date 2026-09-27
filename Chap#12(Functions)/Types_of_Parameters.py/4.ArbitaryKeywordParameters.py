"""
Arbitrary Keyword Parameter (**kwargs) function definition mein use hota hai.
Yeh function ko yeh power deta hai ke aap usay kitne bhi extra named (keyword)
arguments pass kar sakein.
Python un sab extra arguments ko utha kar ek dictionary mein pack kar deta hai.

"""
def user_profile(**kwargs):
    print(kwargs)  # Yeh ek dictionary ban jati hai
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Kitne bhi keyword arguments pass kar dein, error nahi aayega:
user_profile(name="Ali", age=22, city="Lahore", role="AI Engineer")

# **kwargs extra keyword values ko dictionary banata hai.