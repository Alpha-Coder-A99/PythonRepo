"""
Closure mein inner function outer function ke variables ko remember kar sakta hai,
 even after the outer function has finished"""

# Closures
def outer(x):
    def inner(y):
        return x + y
    return inner