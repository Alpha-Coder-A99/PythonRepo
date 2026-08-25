"""Bitwise operation
Ye numbers ke saath nahi, balkay unke Bits (0 aur 1) ke saath khelte hain.
 AI aur Data Science mein ye fast calculations ke liye use hote hain.
 & (AND)
| (OR)
^ (XOR)
~ (NOT)
<< (Left Shift)
>> (Right Shift)"""

# Bitwise operators
a = 10 # Binary: 1010
b = 4  # Binary: 0100
print(f"Bitwise AND (10 & 4): {a & b}") # Result: 0
a = 5  # Binary: 0101
b = 3  # Binary: 0011
print(f"Number a: {a} (Binary: {bin(a)})")
print(f"Number b: {b} (Binary: {bin(b)})")
# 1. AND (&): Dono 1 honge toh hi 1 aayega
# 0101 & 0011 = 0001 (Jo ke 1 hai)
print(f"Bitwise AND (a & b): {a & b}") 
# 2. OR (|): Koi ek bhi 1 ho toh 1 aayega
# 0101 | 0011 = 0111 (Jo ke 7 hai)
print(f"Bitwise OR (a | b): {a | b}")
# 3. XOR (^): Dono mukhtalif (different) honge toh hi 1 aayega
# 0101 ^ 0011 = 0110 (Jo ke 6 hai)
print(f"Bitwise XOR (a ^ b): {a ^ b}")
# 4. Left Shift (<<): Zeroes add karke number bara karna
# 5 (0101) ko 1 baar left shift karo toh 10 (1010) ban jata hai
print(f"Left Shift (a << 1): {a << 1}")