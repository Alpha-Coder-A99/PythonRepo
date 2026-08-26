msg = "Alpha Coder 99"

# 1. 'C' dhoondo kahan hai
print(msg.find("C"))    # Output: 6 (A-0, l-1, p-2, h-3, a-4, space-5, C-6)

# 2. Poora word dhoondo
print(msg.find("Coder")) # Output: 6 (Ye word ka pehla letter batata hai)

# 3. Wo dhoondo jo hai hi nahi
print(msg.find("Toxic")) # Output: -1 (System ne kaha: Toxic logon ki yahan jagah nahi! 😂)