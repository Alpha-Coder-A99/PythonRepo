with open ("hi.txt", "w") as f:
    data = input("Enter what you want to write: ")
    f.write(data)


# Create a fil goal.txt  and wrote 3 goals for 2 months
with open ("Chap#20(File Handling)/goal.txt","w") as f:
    goal=f.write("1.cover python baisics to oops \n2.Clear NUMPy ,Panda,tremlitGUI \n3.Webscrapping & Ai automation")
    print(goal)

    