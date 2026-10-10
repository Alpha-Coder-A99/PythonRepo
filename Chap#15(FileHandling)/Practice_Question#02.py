# Question#02:
# Write a program to create & read a text from a given file certificate.txt and find whethr it contains the word happy
# f=open("certificate.txt", "x")  # Open the file in exclusive creation mode

with open ("certificate.txt","r") as f:
    content=f.read()
    content=content.lower()  # Convert the content to lowercase for case-insensitive search
    if "happy" in content:
        print("The word 'happy' is present in the file.")
    else:
        print("The word 'happy' is not present in the file.")