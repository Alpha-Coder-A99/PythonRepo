grocery_list = []

print("--- Welcome to Smart Kitchen Manager ---")

# 2. Items add karna (.append)
item1 = input("Pehla item batayein: ")
item2 = input("Doosra item batayein: ")
item3 = input("Teesra item batayein: ")

grocery_list.append(item1)
grocery_list.append(item2)
grocery_list.append(item3)

print("\nAapki current list:", grocery_list)

# 3. Aik item nikalna (.pop)
# Farz karein aap ne pehla item kharid liya
bought_item = grocery_list.pop(0) 
print(f"\nTask Done! Aap ne '{bought_item}' kharid liya hai.")

# 4. List ko tartib dena (.sort)
grocery_list.sort()
print("Baqi items (A-Z sorted):", grocery_list)

# 5. Length check karna
print("Ab sirf", len(grocery_list), "items baqi hain.")
# 1. 4th item mangna
item4 = input("Chotha item batayein: ")
grocery_list.append(item4)

# 2. Reverse karna
# Yahan aik line likhein jo list ko ulta (reverse) kar de
# [YOUR CODE HERE]

print("Aapki list (Reverse Order mein):", grocery_list)