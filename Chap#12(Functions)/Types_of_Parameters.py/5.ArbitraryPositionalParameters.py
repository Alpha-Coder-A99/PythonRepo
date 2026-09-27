"""
Arbitrary Positional Parameters (*args) function definition mein use hote hain. -
Yeh function ko yeh power dete hain ke aap usay kitne bhi positional values pass kar sakein,
 bina kisi restriction ke.
"""
def calculate_sum(*args):
    print(args)  # Yeh ek tuple ban jata hai: (1, 2, 3, 4, 5)
    print(sum(args))

# Aap jitne marzi numbers pass kar dein:
calculate_sum(1, 2, 3, 4, 5)


# * lagane se Python samajh jata hai ke user aik se zyada values de sakta hai, 
# aur un sab ko aik hi tuple mein daalna hai.