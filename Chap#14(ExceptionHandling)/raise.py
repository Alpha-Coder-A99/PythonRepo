"""
Hum khud error (raise) is liye karte hain taake program ko galat data ya ghalti par pehle hi rok dein, 
na ke woh khamoshi se galat kaam karta rahe.
"""
# For Example,
"""
Socho aap aik ATM machine ka code likh rahe ho. Koi insaan apne account se Rs. 5,000 nikalna chahta hai, 
lekin uske account mein hain hi Rs. 1,000.
Agar aap error raise na karo: Machine chup chap transaction aage barha degi aur bank ka system kharab ho jayega."""
balance=1000
withdraw_amount=int(input("Enter the amount you want to withdraw: "))
if balance < withdraw_amount:
    raise ValueError("Aapke paas itne money nahi hain!")
else:
    balance -= withdraw_amount

print(f"Transaction successful! Aapke account mein ab {balance} bache hain.")