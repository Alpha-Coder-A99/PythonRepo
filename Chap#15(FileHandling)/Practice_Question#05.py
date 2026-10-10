# Question#05.Open a file called "report.txt" in append mode
with open ("report.txt","a")as f:
    content = input("Enter the content to append to the file: ")
    f.write(content)  # Append the content with a newline character
    f.close()