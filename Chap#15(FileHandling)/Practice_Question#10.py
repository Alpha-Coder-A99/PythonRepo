#Write your name and age in file named "Intro.txt"
with open ("report.txt","a") as f:
    name=input("Enter your name: ")
    age=float(input("Enter your age:"))
    f.write(f"My name is {name}, My Age is {age}")
       