# Write a program with local variables score inside a function and global one outside 
score=98
def subject():
    score=95
    print("Function ka nderscore local variable:", score)

subject()
print("Function ka bahir global variable:",score)