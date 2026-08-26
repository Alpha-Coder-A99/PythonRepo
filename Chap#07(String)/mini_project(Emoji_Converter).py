message = input("Apne jazbaat likho (e.g., I am happy and coding): ")

# Step 2: Words ko alag alag karna (Katana ⚔️ use karke)
words = message.split(" ")

# Step 3: Emoji Map (Dictionary) banana
# Note: Key wo word hai jo user likhega, Value wo emoji hai jo humein chahiye
emojis = {
    "happy": "😊",
    "sad": "😔",
    "coding": "💻",
    "python": "🐍",
    "alpha": "🐺",
    "angry": "😡",
    "independent": "🦅"
}

# Step 4: Logic lagana
output = ""
for word in words:
    # Agar word emoji map min hi toh emoji lagao, warna wahi word rehne do
    output += emojis.get(word, word) + " "

# Step 5: Final reult dikhana
print(f"Alpha Converter: {output}")