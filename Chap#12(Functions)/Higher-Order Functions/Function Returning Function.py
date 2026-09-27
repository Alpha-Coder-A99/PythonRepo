# Function doosra function return bhi kar sakta hai.
"""
Yahan execute ek aisa function hai jo apne andar ek parameter leta hai,
 jiska naam humne func rakha hai. Iske andar print(func()) likha hai — 
 iska matlab yeh hai ke jo bhi function isko milega,
   yeh use run (call) kar dega aur uske result ko print kar dega."""

def outer():
    def inner():
        return"Hello from inner function"
    print("hello from outer functoion")
    return inner
result=outer()
print(result())
