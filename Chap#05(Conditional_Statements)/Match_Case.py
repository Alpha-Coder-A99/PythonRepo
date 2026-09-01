score=70
match score:
    case "70":
        print("you sucesed best award🥰🥰")
    case "60":
        print("you pass")
    case "50":
        print("you fail😬")

day = input("Aaj kaunsa din hai? ")

match day:
    case "Saturday" | "Sunday":
        print("Cricket match aur coding practice! 🏏🐍")
    case "Monday":
        print("Coding ka naya hafta shuru! 💻")
    case _:
        print("Bas mehnat karte raho! 💪")

light = input("Enter light color: ")

match light:
    case "red":
        print("Stop! 🛑")
    case "yellow":
        print("Ready! 🟡")
    case "green":
        print("Go! 🟢")
    case _: 
        print("Invalid color! 🤔")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: ")) 
operator = input("Enter operator (+, -, *, /): ")

match operator:
    case "+":
        print(f"Result: {num1 + num2}")
    case "-":
        print(f"Result: {num1 - num2}")
    case "*":
        print(f"Result: {num1 * num2}")
    case "/":
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error! Zero se divide nahi ho sakta. 🚫")
    case _:
        print("Ghalat operator dala hai! Sirf +, -, /, * use karein.") 