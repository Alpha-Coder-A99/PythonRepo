"""
WORKFLOW OF PROJECT
1-Input from user(Rock🤘💎 ,Paper📜 ,Scissor✂ )
2-Computer chioce(Computer chosse randomly not conditionally)
3-Result print

Cases:
A-Rock
Rock-Rock=tie
Rock-Paper=Paper win
Rock-Scissor=Rock win

B-Paper
Paper-Paper=tie
Paper-rock=paper win
Paper-Scissor=Scissor win

C-Scissor
Scissor-Scissor=tie
Scissor-paper=Scissor win
Scissor-Rock=Rock win

"""
import random

# Humne list (Data Structure) use ki computer choice ke liye
items = ["Rock", "Paper", "Scissor"]

user_name = input("Enter your name: ")
print(f"Welcome {user_name}! Let's play 🕹️")

while True:
    print("\n" + "="*30)
    # .strip() use kiya taake agar user galti se space de de to error na aaye
    # .capitalize() se 'rock' likho ya 'ROCK', wo 'Rock' ban jaye ga
    user_move = input("Enter your move (Rock 💎, Paper 📜, Scissor ✂️) or 'Exit' to stop: ").strip().capitalize()

    if user_move == "Exit":
        print(f"Thanks for playing, {user_name}! Goodbye 👋🥰")
        break

    # Check if input is valid
    if user_move not in items:
        print("🚫 Invalid Move! Please type Rock, Paper, or Scissor.")
        continue

    computer_move = random.choice(items)

    print(f"\n{user_name} chose: {user_move} 👧")
    print(f"Computer chose: {computer_move} 💻")
    print("-" * 20)

    if user_move == computer_move:
        print(f"Both chose {user_move}: It's a Tie! 🤝")

    elif user_move == "Rock":
        if computer_move == "Paper":
            print("Paper covers Rock! 📜 > 💎 | Computer Wins 💻🏆")
        else:
            print("Rock smashes Scissor! 💎 > ✂️ | You Win 👧🏆🥇")

    elif user_move == "Paper":
        if computer_move == "Rock":
            print("Paper covers Rock! 📜 > 💎 | You Win 👧🏆🥇")
        else:
            print("Scissor cuts Paper! ✂️ > 📜 | Computer Wins 💻🏆")

    elif user_move == "Scissor":
        if computer_move == "Rock":
            print("Rock smashes Scissor! 💎 > ✂️ | Computer Wins 💻🏆")
        else:
            print("Scissor cuts Paper! ✂️ > 📜 | You Win 👧🏆🥇")