profile={
    "key":"value ",
    "name":"Alpha_Coder_99",
    "Skills":"Python,Ai",
    "Age":"17",
    "Goal":"Ai devolpor"

}
print(profile.keys()) # prints all keys 
print(profile.values())#prints all values
print(profile.items())# prints all items in key:pair format
# print(profile.clear())#All data will be clear, its danguores , so it will be in coment
print(profile.get("Skills"))
profile.update({"Age":"18"}) # updatefunction kuchna kuchreturnkartahn us li uy alg sa printkiajatah
print(profile)
check_skills = profile.setdefault("Skills", "Web Development")
print("Skills (No Change):", check_skills)
profile["skills"]="Garderning"
print(profile)