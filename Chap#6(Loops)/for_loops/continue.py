# continue	⏭️ SKIP	Sirf current round ko chhor kar aglay par jata hai.
for egg in range(1, 11):
    if egg == 5: # Samjho 5th anda kharab hai
        print(f"Oye! Anda {egg} toh kharab hai! 🤢 Skip karo.")
        continue
    print(f"Anda {egg} bilkul fresh hai! ✅")
#Write a program that prints 1 to 10 but skip the number 7 by use continue statement 
for i in range (1,11):
    if i==7:
        continue
    print(i)