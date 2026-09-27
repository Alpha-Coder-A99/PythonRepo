# map() kisi function ko iterable ke har element par apply karta hai.
#Map
#har ik element pa ja ja ka koe function perform karna
marks=[97,85,77,64,55]
def grade(marks):
    if marks>=90:
        return "You got A+ garde"
    elif marks>=80 and marks<90:
        return "you got A garde"
    elif marks>=70 and marks<80:
        return "you got B garde"
    elif marks>=60 and marks <80:
        return "you got C garde"
    elif marks>=50 and marks<60:
        return 'you got D grade'
    else:
        return "you fail , try again"
grades=map(grade,marks)
print("Exam Score", marks)
print("grades",next(grades))
print("grades",next(grades))
print("grades",list(grades))
    