#WAP to print the multiplication table of any number using a while loop
num=int(input("Enter a number:"))
i=1
while i <=10:
    print(f"{num}*{i}=",num*i)
    i+= 1