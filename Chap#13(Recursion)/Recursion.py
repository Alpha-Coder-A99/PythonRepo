#When function call itself repeatedly.
"Recursion is a programming technique where a function calls itself "
"directly or indirectly in order to solve a problem by breaking it down into smaller,"
" more manageable sub-problems."
def show(n):
    # if n==0: # Base of code hthi basic condition
        # return
    print(n)
    show(n-1)
    print("End")


show(8)
"This function is called Recursive function"