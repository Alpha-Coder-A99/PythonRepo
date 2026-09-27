"""
Local scope ka matlab hota hai ki ek variable sirf usi function ke andar zinda hota hai,
jahan wo define kiya gaya ho.
"""
def my_function():
    local_var = "I am local"
    print(local_var)

my_function()
# print(local_var)  # Error: local_var is not defined outside the function

"⚠️ Yahan ek important principle bhi seekhenge: har jagah global use karna good design nahi hota."