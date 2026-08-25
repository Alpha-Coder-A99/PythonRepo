#identity operators(Ye check karte hain ke kya do variables bilkul ek hi cheez hainentiy opertors)
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)      # True (Dono ek hi memory location hain)
print(x is y)      # False (Value same hai, magar memory alag hai)
print(x == y)      # True (Value barabar hai)