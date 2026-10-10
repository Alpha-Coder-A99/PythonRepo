try:
    print("File kholne ki koshish ho rahi hai...")
    my_file = open("goal.txt", "r")
    content = my_file.read()
    
except FileNotFoundError:
    print("❌ Masla: 'goal.txt' naam ki koi file mili hi nahi!")
    
else:
    print("✅ File kamyabi se parh li gayi hai!")
    print(content)
    
finally:
    # Yeh har haal mein chalega taake memory free ho sake
    print("🧹 Cleaning up... File handling ka process khatam.")