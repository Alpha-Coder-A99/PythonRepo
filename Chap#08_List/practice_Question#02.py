#Write a program that takes 3 favourite foodsfrom user
# and store themin a list
# Then print the list and  its length
food1=input("Enter your favourite food 1:")
food2=input("Enter your favourite food 2:")
food3=input("Enter your favourite food 3:")
food4 = input("Enter your 4th favourite food: ")
foods=[food1,food2,food3]
foods.append(food4)
print(foods)
print(len(foods))