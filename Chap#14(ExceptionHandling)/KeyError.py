# KeyError tab aata hai jab aap kisi dictionary mein aisi key (chabi) ko access karne 
# ki koshish karte hain jo us dictionary ke andar mojood hi na ho.
student = {"name": "Ali", "age": 22}

# 'address' naam ki koi key nahi hai, is liye KeyError aayega:
try:
    print(student["address"])
except KeyError as err:
    print(f"Key not found: {err}")