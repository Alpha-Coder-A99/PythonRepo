#write a factorial of number by using forloop
m=1
n=int(input("Enter  number that want to rodue factorial: "))
for i in range (1,n+1):
    m*=i
print(m)