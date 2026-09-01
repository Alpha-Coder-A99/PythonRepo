salan_ready = input("Kya salan ban gaya? (yes/no): ")

if salan_ready == "yes": # Pehla Darwaza 🚪
    bhook = int(input("Bhook kitni hai? (1-100): "))
    
    if bhook > 70: # Dusra Darwaza (Nested) 🚪
        print("Mister Chuhender:Jaldi khao, bhot bhook lagi hai! 🥘🐭")
    else:
        print("Mister Chuhender: Thora thair kar khate hain. 😊")
        
else: # Pehla darwaza hi band hai
    print("Mister Chuhender: Chalo abhi coding hi karte hain phir! 🐍")

user_name=input("Enter your name:")
if user_name=="Alpha_Areeba":
    pin=int(input("Enter Alpha pin"))
    if pin==4321:
        print("Login Successful! Welcome Alpha Coder! 💻")
    elif pin != 4321:
        print("Galat pin , ap kuon ho yaha alpha code type karo")
else:
    print("Ap kon houn🧐 , mojha sirf meri Alpha hi open kar sakti hn 😏🥱bye")
    
is_sunny=input("Kya aaj dhoop hai? (yes/no): ")
if is_sunny=="yes":
    have_sunblock = input("Kya sunblock lagaya? (yes/no): ")
    if have_sunblock=="yes":
        print("Bahar jao aur enjoy karo! ☀️")
    else:
        print("Pehle sunblock lagao, skin kharab ho jayegi! 🧴")
else:
    print("aj sunblock skip kar sakto ho but best yahi hn ka thora laga lo")

skills = input("Kya aapko Python aati hai? (yes/no):")
if skills=="yes":
    projects = int(input("Aapne kitne projects banaye hain? "))
    if projects>=5:
        print("Aap freelancing shuru kar sakti hain!💸")
    else:
        print("Thore aur projects banayein, phir kaam milega! 📚")
else:
    print("Pehle learning mukammal karein! 🐍phir projects banae")

is_morning = input("Kya subah ka waqt hai? (yes/no):")
if is_morning=="yes":
     is_raining = input("Kya barish ho rahi hai?(yes/no): ") 
     if is_raining =="yes":
        print("Ghar par yoga karein! 🧘‍♀️")
     else:
        print("Bahar walk ke liye jayein! 🏃‍♀️")
else:
    print("Coding ka waqt hai, focus karein! 💻") 