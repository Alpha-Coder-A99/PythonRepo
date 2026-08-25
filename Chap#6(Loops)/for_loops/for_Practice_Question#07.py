#Print  sum of first natural number
s=0
num=int (input("Enter a number till where you want to sum:"))
for i in range(1,num+1):
    s+=i

print(s)