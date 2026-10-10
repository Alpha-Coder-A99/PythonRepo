#Read only first line of report.txt
with open ("report.txt", "r") as file:
    first_line = file.readline()
    print(first_line)
    Second_line = file.readline()
    print(Second_line)
