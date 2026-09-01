# range(start,stop,step)
for item in range(2,20,2 ):
    print(item)
# Write a program using for and range() to print all even number  b/w 1 to 30
for item in range(2,31,2):
    print(item)
# Write a program from 1 to 100 by usig for loop
for i in range(1,101):
    print(i)
# Write a program from 100 to 1 by usig for loop
for i in range(100,0,-1):
    print(i)
# print all the numbers 1 and 50 except multiples of 5 by using forloop
for i in range(1,51,1):
    if i%5!=0:
        print(i)
#Alternatve method
for i in range(1, 51):
    if i % 5 == 0:
        continue 
    print(i)

n = 5
factorial = 1

for i in range(1, n + 1):
    factorial *= i  # Iska matlab: factorial = factorial * i

print(f"5 ka factorial (For Loop) hai: {factorial}")