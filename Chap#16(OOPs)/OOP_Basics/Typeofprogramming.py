# Types of programming in Python
#1.Imperative programming
#2.Declarative/Functional programming
#3.Object-oriented programming

"1.Imperative programming/procedural programming"

num=int(input("Enter any number:"))
if num%2==0:
    print("even number")
else:
    print("odd number")

"2.Declarative /Functional programming"

def even_odd_check():
    if num%2==0:
        return "even"
    else:
        return "odd"
result=even_odd_check(2)
print(result)

"3.Object-oriented programming"
"In this type of programming we use objects to map with real world scenarios"
"We will explore this in detail in this chapter"

