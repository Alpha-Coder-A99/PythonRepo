# Question#04.Open a file called "report.txt" in write mode
# f=open("report.txt","x")  # Open the file in write mode
with open ("report.txt","w") as f:
    data=input("Enter the data to write in the file: ")
    f.write(data)  # Write the data to the file
    f.close()