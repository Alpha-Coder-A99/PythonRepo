#Print how many lines are present in report.txt
with open ("report.txt","r")as file:
    lines=file.readlines()
    print("Number of lines in report.txt:",len(lines))
