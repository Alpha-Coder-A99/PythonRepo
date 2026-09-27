# Map se list double kare
numbers = [1, 2, 3, 4, 5, 6]

# Map logic: lambda x: x * 2 (har item ko double karo)
doubled_list = list(map(lambda x: x * 2, numbers))

print(f"Original: {numbers}")
print(f"Doubled:  {doubled_list}")