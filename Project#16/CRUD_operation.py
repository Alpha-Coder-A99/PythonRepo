from pathlib import Path
import os

print("=====Welcome to CRUD operation======")

def CreateFile():
    name = input("Enter the name of the file: ")
    # Variable ka naam chhota 'p' rakha taaki 'Path' class override na ho
    file_path = Path(name) 
    try:
        if not file_path.exists():
            with open(name, 'w') as f:
                data = input("Enter the data you want to write in the file: ")
                f.write(data)
                print("File created successfully!")
        else:
            print("File already exists!")
    except Exception as e:
        print(f"An error occurred: {e}")

def ReadFile():
    name = input("Enter the name of the file to read: ")
    file_path = Path(name)
    try:
        if file_path.exists():
            with open(name, 'r') as f:
                print("\n--- File Content ---")
                print(f.read())
                print("--------------------")
        else:
            print("File does not exist!")
    except Exception as e:
        print(f"An error occurred: {e}")

def UpdateFile():
    name = input("Enter the name of the file to update/append: ")
    file_path = Path(name)
    try:
        if file_path.exists():
            # 'a' mode use kiya hai taaki purana data delete na ho aur naya append ho jaye
            with open(name, 'a') as f:
                data = input("Enter the data you want to append: ")
                f.write("\n" + data) # Nayi line se data add karne ke liye \n lagaya hai
                print("File updated successfully!")
        else:
            print("File does not exist!")
    except Exception as e:
        print(f"An error occurred: {e}")

def DeleteFile():
    name = input("Enter the name of the file to delete: ")
    file_path = Path(name)
    try:
        if file_path.exists():
            os.remove(name)
            print("File deleted successfully!")
        else:
            print("File does not exist!")
    except Exception as e:
        print(f"An error occurred: {e}")


print("\npress 1 if you want to create a new file")
print("press 2 if you want to read a file")
print("press 3 if you want to update/append a file")
print("press 4 if you want to delete a file")

try:
    a = int(input("Enter your choice: "))
    # Har function ke aage () lagaya hai taaki wo execute ho sake
    if a == 1:
        CreateFile()
    elif a == 2:
        ReadFile()
    elif a == 3:
        UpdateFile()
    elif a == 4:
        DeleteFile()
    else:
        print("Invalid choice! Please select between 1 and 4.")
except ValueError:
    print("Please enter a valid number.")
