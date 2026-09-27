#Create a function that takes a string and return the count vowels and constant seperately
def countvowelconsto(userInput):
    vowels = "aeiouAEIOU"
    count_vowels = 0
    count_consonant = 0

    for eachChar in userInput:
        if eachChar.isalpha(): # Pehle check karo ke alphabet hai ya nahi
            if eachChar in vowels:
                count_vowels += 1
            else: # Agar alphabet hai lekin vowel nahi, to pakka consonant hai!
                count_consonant +=1
        # Jo alphabet nahi (space/numbers), wo skip ho jayenge

    return count_vowels, count_consonant

v, c = countvowelconsto("Apple 123")
print(f"Vowels: {v}, Consonants: {c}") 
# Output: Vowels: 2 (A, e), Consonants: 3 (p, p, l)