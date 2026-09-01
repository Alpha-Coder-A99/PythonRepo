# Write a program that inputs your fav_food name and pints:
# The middle 3 characters
# The last 2 characters
fav_foods=input("Enter your favourite food:")
mid=(len(fav_foods))//2
output1=fav_foods[mid-1:mid +2]
print(output1)
output2=fav_foods[-2:]
print(output2)