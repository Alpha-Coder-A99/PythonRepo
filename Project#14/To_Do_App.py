def task_manager():
    # 1. Empty list banayein (naam 'tasks' rakha hai)
    tasks = [] 
    
    print("=== WELCOME TO TASK MANAGER APP ===")
    
    # 2. Shuruati tasks add karein
    total_task = int(input("Enter how many tasks you want to add: "))
    
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name) # append ke baad () zaroori hain

    # 3. Main Loop (Operations ke liye)
    while True:
        print("\n--- OPERATIONS ---")
        print("1. Add | 2. Update | 3. Delete | 4. View | 5. Exit")
        
        operation = int(input("Choose your operation: "))
        
        # --- ADD (Operation 1) ---
        if operation == 1:
            add_task = input("Enter your task to add: ")
            tasks.append(add_task) # Yahan (add_task) missing tha
            print(f"Task '{add_task}' has been successfully added...")

        # --- UPDATE (Operation 2) ---
        elif operation == 2:
            update = input("Enter the task name you want to update: ")
            if update in tasks:
                update_val = input("Enter new task: ")
                ind = tasks.index(update) # Syntax: index(value) hota hai, [] nahi
                tasks[ind] = update_val
                print(f"Task updated to: {update_val}")
            else:
                print("Task not found!")

        # --- DELETE (Operation 3) ---
        elif operation == 3:
            del_val = input("Enter the task which you want to delete: ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task '{del_val}' deleted successfully!")
            else:
                print("Task not found!")

        # --- VIEW (Operation 4) ---
        elif operation == 4:
            print(f"Today's tasks are: {tasks}")

        # --- EXIT (Operation 5) ---
        elif operation == 5:
            print("Closing the program.... Bye Areeba!Thanks for using our app")
            break
        
        else:
            print("INVALID Input")

# Function call 
task_manager()