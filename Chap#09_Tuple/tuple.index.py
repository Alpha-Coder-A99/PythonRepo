# Ye method aapko batata hai ke koi specific value tuple mein kis position (index) par mojood hai.
# my Tuple

skills = ("Python", "Freelancing", "AI", "Cooking")

# AI ka index maloom karte hain
position = skills.index("AI")

print(position) 


# Imp point
"""Pehli Occurrence: Agar koi item tuple mein do baar ho,
 to .index() sirf pehli baar wali position batayega."""
nums = (10, 20, 30, 20, 40)
print(nums.index(20)) # Output: 1 (Agla wala 20 ignore ho jayega)

#Error case:
#  Agar aap aisi cheez dhoondein jo tuple me hai hi nahi, to Python ValueError dega.

skills.index("Java") # ->>> Error! ya eror de ga