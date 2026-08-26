# print all the factors of number 
num=int(input("Enter number:"))

for item in range(1,num+1):
    if num%item==0:
        print(item)
