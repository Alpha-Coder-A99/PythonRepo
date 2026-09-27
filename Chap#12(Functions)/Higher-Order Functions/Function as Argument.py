"Ek function ko doosre function ke argument ke taur par pass karna."
def greet():
    return "Hello"

def execute(func):
    print(func())

"""
Yahan execute ek aisa function hai jo apne andar ek parameter leta hai,
jiska naam humne func rakha hai. Iske andar print(func()) likha hai — 
iska matlab yeh hai ke jo bhi function isko milega,
yeh use run (call) kar dega aur uske result ko print kar dega."""


execute(greet)