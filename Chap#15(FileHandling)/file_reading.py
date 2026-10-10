#1.Read entire file
# with open("Chap#20(File Handling)/mydata.txt","r") as f:
#     data=f.read()
#     print(data)

#2.Read line by line
# with open("Chap#20(File Handling)/New_File.txt","r") as f:
#     line1=f.readline()
#     line2=f.readline()
#     line3=f.readline()
#     line4=f.readline()
#     line5=f.readline()
#     line6=f.readline()
#     line7=f.readline()
#     line8=f.readline()

#     print(f"line1={line1}")
#     print(f"line2={line2}")
#     print(f"line3={line3}")
#     print(f"line4={line4}")
#     print(f"line5={line5}")
#     print(f"line6={line6}")
#     print(f"line7={line7}")
#     print(f"line8={line8}")
    
#Read all lines
with open("Chap#20(File Handling)/New_File.txt","r") as f:
    ReadlinesMethods=f.readlines()
    print(ReadlinesMethods)