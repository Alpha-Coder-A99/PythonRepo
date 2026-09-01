# print sum (even sum & odd sum seprately) by using for loop
n=int(input("Enter your number:"))
even_sum=0
odd_sum=0
for i in range (1,n+1):
    if i%2==0:
        even_sum+=i
    else:
        odd_sum+=i

print(f"your even numbers sums are {even_sum} and your odd numbers are {odd_sum}")