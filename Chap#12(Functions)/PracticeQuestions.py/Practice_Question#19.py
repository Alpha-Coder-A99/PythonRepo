#Check prime number
#Write  a function which checks prime number
def Check_prime(num):
# Step 1: Base Case (1 ya us se chote prime nahi hote)
    if num <= 1:
        return False
    
 # Step 2: Loop chala kar check karna
# Hum 2 se shuru karte hain aur num tak check karte hain
    for i in range(2, num):
        if num % i == 0:
            # Agar kisi bhi 'i' se divide ho gaya, toh ye prime nahi hai
            return False 
            
 # Step 3: Agar poora loop khatam ho gaya aur koi divisor nahi mila
    return True

# Function ko test karte hain
number = 7
if Check_prime(number):
    print(f"{number} ek Prime Number hai! 🚀")
else:
    print(f"{number} Prime nahi hai. ❌")
    