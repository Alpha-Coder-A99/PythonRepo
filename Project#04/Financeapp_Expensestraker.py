# Expense tracker app project

expenses_list = [] # List of expenses in form of dictionaries

print("--- Welcome to Alpha's Expense tracker 🥰 ---")

while True:
    print("\n=== Menu ===")
    print("1. Add expenses 💸")
    print("2. View all expenses 📋")
    print("3. View total expenses 💰")
    print("4. Exit 🚪")

    choice = int(input("Please enter your choice: "))

    if choice == 1:
        date = input("Enter the date of expense: ")
        category = input("Enter the Category (food, gym, books, etc.): ")
        description = input("Enter a bit detail of your expense: ")
        amount = float(input("Enter total amount of your expenses: "))
        
        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        
        expenses_list.append(expense)
        print("\nDone bro! 😉 Expense added successfully 😎")

    elif choice == 2:
        if len(expenses_list) == 0:
            print("No expense added, go and spend money 💵")
        else:
            print("==== This is your list of expenses ====")
            count = 1
            for each_expense in expenses_list:
                # Alag alag variables ko print karna asan ha
                print(f"Expense number {count} --> {each_expense['date']}, {each_expense['category']}, {each_expense['description']}, {each_expense['amount']}")
                count += 1

    elif choice == 3:
        total = 0
        # Sab amounts ko jama (add) karne ke liye for loop
        for each_expense in expenses_list:
            total = total + each_expense["amount"]
        
        print("\n--- Total spending so far: ", total, "💸 ---")

    elif choice == 4:
        print("Thanks for using our system! Stay fit and keep coding! 🥰🤗 and keep using our system😁😜")
        break # Loop se bahar nikalne ke liye

    else:
        print("Invalid Number 🙄, please choose 1, 2, 3 or 4 and try again😏")