# Question#01.Write code to create and open a file named mydata.txt in read mode.

# file = open("mydata.txt", "x")

with open("mydata.txt", "r") as file:
    content=file.read()
    print(f"your file data is:\n{content}")
    file.close()

  

