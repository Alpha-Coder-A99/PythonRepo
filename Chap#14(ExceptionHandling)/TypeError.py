a=input("Enter a number: ")
b=input("Enter another number: ") # if you agve any string you ocured type error
try:
    print(a/b)
except TypeError as err:
    #you can write any word instead of err, but it is a good practice to use err
      # you can write any thing instead of Exception,you can write ZeroDivisionError, but it is a good practice to use Exception
    print(f"something went wrong: {err}")