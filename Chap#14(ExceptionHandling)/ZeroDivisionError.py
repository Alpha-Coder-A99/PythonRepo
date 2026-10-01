num1=int(input("Enter a number: "))
num2=int(input("Enter another number: "))
try:
    print(num1/num2)
except ZeroDivisionError as err:
    print(f"something went wrong: {err}")
