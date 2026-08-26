#  Guessing Game - Alpha Edition 🐺
secret_number=18
attempts=0
win=False
print("---Welcome to Alpha Guessing Game--- ")
while win==False:
    guess=int(input("Guess one number from 1 to 20"))
    attempts+=1
    if guess==secret_number:
        print(f"Congratualation Areeba! 🎉 you won in {attempts} attempts!")
    elif guess < secret_number:
        print("Guess up from this number")
    else:
        print("Guess low from this number.")
print("Game Over")