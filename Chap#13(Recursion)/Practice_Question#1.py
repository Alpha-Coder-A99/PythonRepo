#Write a recurive function to calculate the sum of first n natural number
def Calc_sum(n):
    if n==0:
        return 0
    # print(n)
    return Calc_sum(n-1)+n

sum=Calc_sum(20)
print(sum)