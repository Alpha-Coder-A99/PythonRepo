#Seprate  each digits of a number and print on a new line(trmethod not alloweded)
num=int(input("Enter any number😊:"))
while num > 0:
    print(num %10)
    num//=10