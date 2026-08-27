rent=float(input("Enter your flat rent:"))
food=float(input("Enter the amount of food odered:"))
electricity_spend=float(input("Enter how much your electricity spend:"))
Charge_per_unit=float(input("Enter Charge per unit:"))
person=int(input("Enter the number of number who living in flat:"))

#Calcultion

total_bill=electricity_spend * Charge_per_unit
output=(rent+food+total_bill)// person
print("Every person will pay",output)