print("========WELCOME TO AGE CALCULATOR🚀🎉✨==========")
from datetime import date

today = date.today()
print(f"Today's date is {today.strftime('%B %d, %Y')}")

year=int(input("Enter your birth year (YYYY): "))
month=int(input("Enter your birth month (MM): "))
day=int(input("Enter your birth day (DD): "))

Date_of_birth= date(year, month, day)
age = today.year - Date_of_birth.year - ((today.month, today.day) < (Date_of_birth.month, Date_of_birth.day))
print(f"You are {age} years old! 🎂🎉")

total_Days = (today - Date_of_birth).days 
print(f"You have lived for {total_Days} days! 🌞🌙")
