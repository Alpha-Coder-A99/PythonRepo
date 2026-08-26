phone_book = {
    "Mariyam": "03001234567",
    "Sara": "03111234567",
    "Halima": "03221234567"
}
name = input("Enter name: ")
print(phone_book.get(name, "Contact not found"))
phone_book["Areeba"] = "03451234567"
print(phone_book)