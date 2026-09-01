# break	🛑 STOP	Loop ko foran khatam kar deta hai.
for i in range(1,11):
    if i == 7:
        print("Mil gaya 7! Ab agay nahi jana.")
        break  # Loop yahin khatam!🤞
    print(i)



correct_pass = "python123"

for attempt in range(1, 6):
    guess = input("Password dalo: ")
    if guess == correct_pass:
        print("Access Granted! 🔓")
        break # Baaqi attempts ki zaroorat nahi, loop khatam!
    else:
        print(f"Ghalat! {5 - attempt} chances baaqi hain.")