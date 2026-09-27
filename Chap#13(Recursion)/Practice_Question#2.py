#Write a recursive function to print all element in a list (HINT: USE LIST & INDEX as perameters)
def print_list (list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits=["Mango","Apple","licti","Strwberry","Banana","Cheery"]
print_list(fruits)