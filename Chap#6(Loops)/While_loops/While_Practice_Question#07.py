"""Write a program that prints the sum of first n natural numbers
 e.g,if n=5 then output dhould be :
1+2+3+4+5=15(Hint:Keep a running tool iside loop)"""
n=int(input("Enter natural number:"))
sum_val=0 
while n>=1:
    sum_val+=n
    n-=1
print("sum:",sum_val)
print("n=", n)