# Function jo list ka sum nikale
def func_sum(my_list):
    total = 0
    for number in my_list:
        total += number  # Har number ko total mein jama karna
    return total

numbers = [1, 2, 3, 4, 5, 6]
print(f"Total Sum: {func_sum(numbers)}") 