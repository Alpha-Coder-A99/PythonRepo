name=input("Hi ,I am Pyrobot!May I know your name: ")
print("Hi",name,"!")
quistions=["Which is you favourite_food :","Is you like to read :","Are you lerning python :"]
for ques in quistions:
    answer=input(ques).lower()
    if answer=="yes":
        print("OH! thats Great😎")
    elif answer=="no":
        print("Oh! Thats okay😃")
    else:
        print("Okay! so it is "+ answer )