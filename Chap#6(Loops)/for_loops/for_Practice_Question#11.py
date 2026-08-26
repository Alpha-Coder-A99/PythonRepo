#Check if a number is a perfect(sum of the factors=the number itself)
num=int(input("Enter a number:"))
s=0
for i in range (1,num):
    if num%i==0:
        s+=i

if s==num:
    print("perfect number")
else:
    print("Not a perfect number")
