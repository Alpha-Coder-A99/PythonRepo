# 1. Simple Assignment (=)
x = 10
print(f"Shuruati value: {x}")

# 2. Add and Assign (+=)
x += 5  # Iska matlab hai: x = x + 5
print(f"5 jama karne ke baad: {x}")

# 3. Subtract and Assign (-=)
x -= 3  # Iska matlab hai: x = x - 3.,-->> x-=3
print(f"3 nikalne ke baad: {x}")

# 4. Multiply and Assign (*=)
x *= 2  # Iska matlab hai: x = x * 2
print(f"2 se multiply ke baad: {x}")

# 5. Divide and Assign (/=)
x /= 4  # Iska matlab hai: x = x / 4
print(f"4 se divide ke baad: {x}")

# 6. Modulus and Assign (%=)
x = 10
x %= 3  # 10 ko 3 se divide karo aur bacha hua (remainder) x mein daal do
print(f"10 % 3 ka result: {x}")

# 7. Exponent (Power) and Assign (**=)
x = 2
x **= 3 # 2 ki power 3 (2*2*2)
print(f"2 ki power 3: {x}")

# 9. Floor Division and Assign (//=)
x = 10  
x //= 3  # 10 ko 3 se divide karo aur poora number (floor) x mein daal do
print(f"10 // 3 ka result: {x}")
# 10. Remainder and Assign (%=)
x = 10
x %= 3  # 10 ko 3 se divide karo aur bacha hua (remainder) x mein daal do
print(f"10 % 3 ka result: {x}")

# 11. Bitwise AND and Assign (&=)
x = 5  # Binary: 0101
x &= 3  # Binary: 0011, Result: 0001 (1)
print(f"5 & 3 ka result: {x}")  

#12. Bitwise OR and Assign (|=)
x = 5  # Binary: 0101       
x |= 3  # Binary: 0011, Result: 0111 (7)    
print(f"5 | 3 ka result: {x}")

#13^. Bitwise XOR and Assign (^=)
x = 5  # Binary: 0101
x ^= 3  # Binary: 0011, Result: 0110 (6)
print(f"5 ^ 3 ka result: {x}")

# 14. Bitwise Left Shift and Assign (<<=)
x = 5  # Binary: 0101
x <<= 1  # Left shift by 1, Result: 1010 (10)
print(f"5 << 1 ka result: {x}")

# 15. Bitwise Right Shift and Assign (>>=)
x = 10  # Binary: 1010
x >>= 1  # Right shift by 1, Result: 0101 (5)
print(f"10 >> 1 ka result: {x}")

# 16. Bitwise | and Assign (|=)
x = 5  # Binary: 0101
x |= 3  # Binary: 0011, Result: 0111 (7)
print(f"5 | 3 ka result: {x}")