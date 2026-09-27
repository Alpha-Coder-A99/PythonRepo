# Professional Python code ko readable aur maintainable banane ke liye type hints useful hain.
# Yahan 'name: str' aur 'age: int' type hints hain, aur '-> str' return type bata raha hai
def student_info(name: str, age: int) -> str:
    return f"Name: {name}, Age: {age}"

print(student_info("Ali", 22))


"""Yeh optional hote hain, yaani agar aap na dein tab bhi Python code run kar deta hai, 
lekin yeh code ko samajhna aur read karna bohat asan bana dete hain."""