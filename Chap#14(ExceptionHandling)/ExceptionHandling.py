"""
Python Exception Handling allows a program to gracefully handle unexpected events
(like invalid input or missing files) without crashing. Instead of terminating abruptly,
 Python lets you detect the problem, respond to it, and continue execution when possible.

❌ Errors (unfixable)
SyntaxError — wrong syntax
IndentationError — bad spacing
TabError — mixing tabs/spaces

✅ Exceptions (handleable!)
ZeroDivisionError
TypeError
ValueError
FileNotFoundError
IndexError
NameError
ImportError
Key Error
SyntaxError"""


a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
try:
    print(a/b)
except Exception as err:
    #you can write any word instead of err, but it is a good practice to use err
      # you can write any thing instead of Exception,you can write ZeroDivisionError, but it is a good practice to use Exception
    print(f"something went wrong: {err}")
else:
    print("Division was successful")
finally:
    print("If there are errors or not no matter i will run")

name=input("Enter your name: ")
print(f"Hello{name}! ")  

"""
Python Exception Handling allows a program to gracefully handle unexpected events
(like invalid input or missing files) without crashing. Instead of terminating abruptly
, Python lets you detect the problem, respond to it, and continue execution when possible.
"""
try:
    number=int(input("Enter the number to divide:"))
    print(1/number)
# except ZeroDivisionError:
#     print("You canot divide number with 0 buddy😜 ")
# except ValueError:
#     print("Enter only integer please🥺")
except Exception:
    print("Some thing went wrong")


try:
    # Agar user ne 'hazar' likh diya numbers ke bajaye:
    rent = float(input("Flat ka rent likhein (sirf numbers): "))
    print(f"Aapka rent hai: {rent}")
    
except ValueError:
    # Python crash hone ke bajaye yeh message dikhaye ga:
    print("❌ Ghalati! Meharbani kar ke sirf numbers (123) enter karein, text nahi.")

try:
    # Agar user ne 'hazar' likh diya numbers ke bajaye:
    rent = float(input("Flat ka rent likhein (sirf numbers): "))
    print(f"Aapka rent hai: {rent}")
    
except ValueError:
    # Python crash hone ke bajaye yeh message dikhaye ga:
    print("❌ Ghalati! Meharbani kar ke sirf numbers (123) enter karein, text nahi.")