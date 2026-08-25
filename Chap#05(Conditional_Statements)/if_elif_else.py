Traffic_light=input("Enter traffic light:")
if Traffic_light=="Red":
    print("you have to stop🚫🛑✋")
elif Traffic_light=="yellow":
    print("Ready to drive🟡💹")
elif Traffic_light=="Green":
    print("you can drive🚘🚘Go!Go!")
else:
    print("you choose 1 in these 3 \nyellow\ngreen\nRed")

month=input("Enter current month :")
if month=="November":
    print("Alpha, aap ka Birthday mahina aa gaya! 🥳")
elif month=="August":
    print("Bas ek mahina baaki hai! 🎁")
else:
    print("Abhi intezar karein, coding seekhte rahein! 🐍")

price=float(input("U laptop ki price kia hn?"))
if price>=150000:
    print("ye toh Pro MacBook hai! 🔥")
elif price>=80000 and price<=120000:
    print("ya ik acha laptop hn") 
else:
    print("Alpha!Thori aur bachat (saving) karni paregi. 💪")

flame=int(input("Enter your flame"))
if flame >=80:
    print(f"your flame🔥 is {flame} which is high, salan jal sakta hn ")
elif flame <=50:
    print("Salan dair se banega, thori aag barhao.")
else:
    print("Perfect! Salan yummy banega.😋😋")

Tempreture=float(input("Enter Tempreture🧪"))
if Tempreture>=30:
    print("It is too hot outside🥵")
elif Tempreture >=15:
    print("It i too cold🥶")
else:
    print("Today is plesaent day,🤩🥰🤗👻")
num=int(input("Enter the number :"))
if num%2==0:
    print(f"{num} is even")
elif num%2!=0:
    print(f"{num} is odd")
else:
    print("Please gave correct output")

marks = int(input("Enter your marks: "))
if marks >= 95:
    print("You got A+ marks 🏆")
elif marks >= 90: 
    print("You got A marks ⭐")
elif marks >= 80:
    print("You got B marks ✅")
elif marks >= 70:
    print("You got C grade 📈")
elif marks >= 65:
    print("You got D grade 😐")
else:
    print("You are fail, try next time with new motivation. Be consistent! 💪")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: ")) 
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result} ")

elif operator == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result} ")

elif operator == "*":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result} ")

elif operator == "/":
    # Division mein zero check karna zaroori hai!
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result} ")
    else:
        print("Error! Zero se divide nahi ho sakta. 🚫")

else:
    print("Invalid Operator! Sirf (+, -, *, /) istemal karein. ⚠️")

num=int(input("Enter a number"))
if num>0:
    print(f"{num} is Positive")
elif num<0:
    print(f"{num} is Negative")
else:
    print("Number is zero")
    