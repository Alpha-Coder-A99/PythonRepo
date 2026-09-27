#personalChatAsistent_Aibuddy app

import datetime
import time
present_hour=datetime.datetime.now().hour
name=input("Enter your name:")
if 5<=present_hour<=11:
    print(f"Good morning🌄{name}")
elif 11<=present_hour<=17:
    print(f"Good Afternoon{name}")
elif 17<=present_hour<= 20:
    print(f"Good evening🌲{name}")
else:
    print(f"Good Night😴")



print(f"Assalam-o-Aliakum!{name} welcome to ChatBot🥰🤗,I am you Ai_buddy ")
print("You can ask me basics quistions ,Type'bye' to exit from Chat")

#Chatbot memory Creation
resposes={
    "wa-aliakum assalam":f"WELcome🥰🤗{name} How can i help you",
    "how are you":"I am very fine☺😎😏😉Thankyou 🥰 How about you",
    "i am fine":"Thats great 😎🥰",
    "who are you":"I am a friendly Ai chat bot created by Alpha_Coder_99",
    "motivate me":"Keep Going😎!Every bug of Life &Coding makes you better 💪, Are you happy",
    "happy":"Great to hear  That🥰",
    "what is functions": "A function in python is a block of reuseable code  that performs a speacific tasks",
    "bye":f"Okay bye {name}! I enjed your Company 🤗, Thanks to talking me🥰, Come again "
}

#Method/Function to get response of ChatBot
def getresponseofBot(user_Question):
    user_Question=user_Question.lower()
    for each_key in resposes:
        if each_key in user_Question:
            return resposes[each_key]
    return"Sorry! I don't Understand your quistion,I am not well trained yet😌but i will try to improve my self💪I am still in learning mode"


#Take your Input 
while True:
    User_Input=input("Please ask your Question")
    reply=getresponseofBot(User_Input)
    print("Bot response:",reply)


    if "bye" in User_Input.lower():
        break