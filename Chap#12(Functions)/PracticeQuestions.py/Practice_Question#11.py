#Define a function convert_to_upper(word) that returns the uppercase version of the string
def convert_to_upper(word):
    if word.isupper():
        print("It is already in uppercase!")
    else:
        print("Converting to Upper Case...")
    return word.upper()

print(convert_to_upper("appLe"))