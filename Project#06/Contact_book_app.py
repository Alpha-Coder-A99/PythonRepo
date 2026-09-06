"""
THis is my contact book app which perform difrent function
->first of all we can create contact
->we can view contacts
->we can update contacts
->WE can Delete contacts
->WE can Search any contact
->WE can Count contacts
->WE can exit

"""

user = input("What is your name? ")
contacts = {}

while True:
    print(f"\n=== {user}'s Contact Book 📱📕 ===")
    print("1. Create Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count Contact")
    print("7. Exit")
    
    choice = int(input("Enter your choice (1-7): "))

    # Choice 1: Create
    if choice == 1:
        name = input("Enter the name: ")
        if name in contacts:
            print(f"Contact {name} already exists!")
        else:
            age = input("Enter age: ")
            email = input("Enter email: ")
            mobile = input("Enter mobile number: ")
            # Storing with correct dictionary keys
            contacts[name] = {"age": age, "email": email, "mobile": mobile}
            print(f"Contact {name} created successfully!")

    # Choice 2: View
    elif choice == 2:
        view_name = input("Enter name to view: ")
        if view_name in contacts:
            person = contacts[view_name]
            # Fixed the single quotes inside double quotes!
            print(f"Name: {view_name}, Age: {person['age']}, Mobile: {person['mobile']}")
        else:
            print("CONTACT NOT FOUND")

    # Choice 3: Update
    elif choice == 3:
        update_name = input("Enter the name for update: ")
        if update_name in contacts:
            contacts[update_name]["age"] = input("Enter new age: ")
            contacts[update_name]["email"] = input("Enter new email: ")
            contacts[update_name]["mobile"] = input("Enter new mobile: ")
            print("Contact Updated!")
        else:
            print("CONTACT NOT FOUND")

    # Choice 4: Delete
    elif choice == 4:
        del_name = input("Enter name to delete: ")
        if del_name in contacts:
            del contacts[del_name]
            print(f"{del_name} deleted successfully!")
        else:
            print("CONTACT NOT FOUND")

    # Choice 5: Search
    elif choice == 5:
        search_name = input("Enter name to search: ").lower()
        found = False
        # Using .items() to get both Name and Info
        for name, info in contacts.items():
            if search_name in name.lower():
                print(f"Found -> Name: {name}, Mobile: {info['mobile']}")
                found = True
        if not found:
            print("No matching contact found.")

    # Choice 6: Count
    elif choice == 6:
        print(f"Total contacts: {len(contacts)}")

    # Choice 7: Exit
    elif choice == 7:
        print(f"Goodbye {user}! 🥰, Take care7")
        break

    else:
        print("Invalid Input! Please try again.")