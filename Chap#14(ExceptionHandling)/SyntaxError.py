# syntaxError exception handling sa handle nahi kia j a sakta😁🥱😝apna dimag lagao aur syntax ka khail rakho
age=45

try:
    if age > 18:
        print("You are an adult.")
except SyntaxError as err:
    print(f"SyntaxError occurred: {err}")
