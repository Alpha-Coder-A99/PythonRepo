"""
Decorator Python mein ek aisa function hota hai 
jo kisi doosre function ki functionality ko modify ya upgrade kar deta hai, 
bina us original function ka code badle.
"""
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper