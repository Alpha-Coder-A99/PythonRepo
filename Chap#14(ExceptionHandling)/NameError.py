name="Alpha"
try:
    print(age)
except NameError as err:
    print(f"Variable not defined: {err}")