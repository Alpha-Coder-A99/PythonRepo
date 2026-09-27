# Create a function full_name(first_name,last_name)that return full name joint with space
def full_name(first_name,last_name):
    # return first_name + " " +last_name
    return first_name + "_" +last_name

print(full_name("Alpha","Coder"))
# Ye purana aur simple tareeqa hai, lekin zyada variables hon to thora "Messy" ho jata hai.
#2nd way
# Ye Modern Python ka sab se behtareen tareeqa hai. 
# Is mein galti ke chances kam hote hain aur ye parhne mein asaan hai.
def fully_name(first_name,last_name):
    # return f"{first_name_{last_name}"
    return f"{first_name} {last_name}"

print(fully_name("Alpha","Coder"))