"Parameter"
# Parameter function definition mein variable hota hai:
def greet(name):   # name = parameter
    print(name)

"Argument"
# Argument function call ke waqt di hui actual value hoti hai:
greet("Areeba")  # "Areeba" = argument
greet("batool")    # "batool" = argument 
greet("Areeba", "batool")  # TypeError: greet() takes 1 positional argument but 2 were given
