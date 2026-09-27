# Nested Function
# Function ke andar function define karna.
 
def outer():
    
    def inner():
        print("Hello")
    
    inner()
    