# Write a program if a list contains a palindrome of elements
# (Hint: use  copy() method)
"""palindrome mean esa cheez jo samna sa aur picha sa same hoti hn 
This is palindrome:maam=maam,racecar= rececar
list.copy() ya shalow copy return karta hn ik list ki"""
num1=[1,2,1]
num2=[1,2,3]
copy_num1=num1.copy()
copy_num1.reverse()
if copy_num1==num1:
    print("pallindrome")
else:
    print("Not Palindrome")