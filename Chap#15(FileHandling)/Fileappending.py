# f=open("hi.txt", "a")
# data=input("Enter what you want to append: ")
# f.write(data)
# f.close()

with open("hi.txt", "a") as f:
    data = input("Enter what you want to append: ")
    f.write(data)