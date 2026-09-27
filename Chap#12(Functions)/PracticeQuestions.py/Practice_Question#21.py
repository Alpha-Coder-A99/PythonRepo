# Write a function which checks Even/odd 
def Even_odd_Check(num):
    if num%2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

Even_odd_Check(8)    

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

number = int(input("Enter the number:"))
if is_even(number):
    print(f"{number} AI processing ke liye valid hai!")
    