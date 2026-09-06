menu = {
    "Pizza": 700, # Numbrs sa quote nahi lagta lag tha au eror aya koeka python esa int ka bajawa str samjhata hn 😁😜
    "Burger": 200,
    "Salad": 100,
    "Mix_Sabzi": 150,
    "Bread": 30,
    "Coffee": 70,
    "Aloo Paratha": 50,
    "Ice Cream": 100,
}

print("=== Welcome to our Restaurant 🤗🍜😋 ===")
# Menu ko print karne ka Best way
print("Pizza: 700/- \nBurger: 200/- \nSalad: 100/-\nMix_Sabzi: 150/-\nBread: 30/-\nCoffee: 70/-\nAloo Paratha: 50/-\nIce Cream: 100/-")

order_total = 0

# first order
item_1 = input("\nEnter the name of item you want to order == ").title()

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your {item_1} has been added to your order.")
else:
    print(f"Sorry, {item_1} is not available yet.")

# 2nd order
another_item = input("\nDo you want to order another item? (Yes/No) ").title()

if another_item == "Yes":
    item_2 = input("Enter the 2nd name of item you want to order == ").title()
    if item_2 in menu:
        order_total += menu[item_2] # order_total mein price add karni ha
        print(f"{item_2} has been added to your order.")
    else:
        print(f"Sorry, {item_2} is not available yet.")

print(f"\n--- Total amount of order to pay is {order_total} PKR ---")
print("Enjoy your meal! 🍔🥗😋🌸")