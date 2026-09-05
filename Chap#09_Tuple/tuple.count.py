""" .count() Method
Ye method ginta (count karta) hai ke aik specific item tuple mein kitni dafa aaya hai."""

my_targets = ("Python", "AI", "Fitness", "Python", "Deen", "Python")
repeat_count = my_targets.count("Python")
print(repeat_count)


# Error case:
# Agar koi item tuple mein nahi hai, to ye error nahi deta, balkay 0 return karta hai.
# Ye method hamesha aik integer (number) wapis karta hai.