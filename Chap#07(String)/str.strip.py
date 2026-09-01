naam = "  Alpha Coder   "

print("Pehle wala:",naam, "|")
# Output:    Alpha Coder |  

clean_naam = naam.strip()
print("Clean wala:", clean_naam, "|")
# Output: Alpha Coder |
 #.rsstrip
msg = "Alpha Coder    "
print(msg.rstrip()) 
# Output: "Alpha Coder" (Right wali khali jagah khatam!)

#lsstrip
msg = "    Areeba"
print(msg.lstrip()) 
# Output: "Areeba" (Left wali khali jagah khatam!)

website = "www.google.com"
# Sirf shuru ka "www." hatana hai
print(website.lstrip("w.")) # Output: "google.com"
# Sirf aakhir ka ".com" hatana hai
print(website.rstrip(".com")) # Output: "www.google"