# filter() ka matlab hai "Channa" (Selection karna).
marks=[97,85,27,34,35]
def failing (score):
    return score<40 

result=filter(failing,marks)
print("Failing score",next(result))

print("Failing score",list(result))