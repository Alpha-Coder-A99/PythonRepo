marks = [97, 85, 77, 64, 55, 35] # Maine ek failing score (35) add kiya hai check karne ke liye

# Pehle Grade dene wala function banate hain (Map ke liye)
def get_grade(score):
    if score >= 90:
        return f"{score}: A+"
    elif score >= 80:
        return f"{score}: A"
    elif score >= 70:
        return f"{score}: B"
    elif score >= 60:
        return f"{score}: C"
    elif score >= 50:
        return f"{score}: D"
    else:
        return f"{score}: Fail"

# Ab failing marks filter karne wala function (Filter ke liye)
def is_failing(score):
    return score < 50  # फर्ज़ करें 50 से कम वाला फेल है

# --- EXECUTION ---

# 1. Map use karke sab ke grades nikalein
grades = list(map(get_grade, marks))

# 2. Filter use karke sirf fail hone wale marks nikalien
failing_scores = list(filter(is_failing, marks))

print("Exam Scores:", marks)
print("All Grades:", grades)
print("Failing Scores Only:", failing_scores)