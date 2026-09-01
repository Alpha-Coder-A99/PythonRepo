name=input("Welcome🥰 User! What is your name?")
import random 
computer=random.randint(1,100)
tries=0

while True:
    tries+=1
    human=int(input(f"hye{name}!Guess your number between 1 - 100:-"))

    if human==computer:
        print(f"Congratualation!🎉{name}✨ you have win in {tries} tries!🎀")
        break
    elif human > computer:
        print("WRONG Guess! Go lower !")
    
    elif  human < computer:
        print("WRONG Guess! Go Higher !")