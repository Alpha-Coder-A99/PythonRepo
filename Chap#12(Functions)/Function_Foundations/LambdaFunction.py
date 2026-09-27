"""
Lambda ek small anonymous function hota hai 
jo usually simple one-expression operations ke liye use hota hai.
"""
# lambda arguments: expression
lambda x:x*x
"""
lambda: Keyword hai.
arguments: Jitne marzi parameters de sakte hain.
expression: Ek single calculation ya code jo automatically return ho jata hai 
(yahan return keyword likhne ki zaroorat nahi hoti)."""


square = lambda x: x * x
print(square(5))


add=lambda a,b:a+b
print(add(4,7))

# lambda
""" Aam taur par hum function def keyword se banate hain
 lekin Lambda function aik hi line mein khatam ho jata hai."""
# def addition(x):
#     return x + 6

# addition()
addition=lambda x,y:x+y 
result=addition(5,9)
print(result)

#Lambda Functions
# Short one-line functions
square = lambda x: x*x
print(square(5))
