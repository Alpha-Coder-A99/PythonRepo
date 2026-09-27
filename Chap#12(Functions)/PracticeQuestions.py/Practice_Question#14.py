# Create a program using global keyword to modify a varble from inside a function
mood="sad😞/angry😡"
def change_mood():
    global mood # Python ko batana ke hum bahar wale 'mood' ko use kar rahe ha
    mood="happy☺😊"
    print("Function ka ander mood:",mood)
print("Shoru me mood:",mood)

change_mood()
print("Function ka baad mood(global)mood",mood)
