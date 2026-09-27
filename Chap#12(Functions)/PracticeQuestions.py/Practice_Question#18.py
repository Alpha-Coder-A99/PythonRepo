#Filter se even numbers nikale
numbers=[4,17,19,20,12,17,21,31,45,50]
def filter_even (number):
    return number%2==0 

result=filter(filter_even,numbers)
print("even number:", next(result))
print("even number:", next(result))
print("even number:", next(result))
# print("even number:", list(result))