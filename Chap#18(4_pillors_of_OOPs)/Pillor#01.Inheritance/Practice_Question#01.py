#Creat a class Account with 2 attributes(balance&Accountno),Creat methods for debit ,Credit and prnting the balances
class Acount:
    def __init__(self,bal,Accno):
        self.balance=bal
        self.AccountNumber=Accno
        #Creating debit method
    def debit(self,amount):
        self.balance-=amount
        print(f"price{amount} was debited")
        print("total balance=",self.get_balance())
    #Creating credit method
    def credit(self,amount):
        self.balance+=amount
        print(f"Rs{amount} was credited")
        print("Total_Balnace=",self.get_balance())
    #Creting total balancing
    def get_balance(self):
        return self.balance

Acc1=Acount(100000,34567)
# print(Acc1.balance)
# print(Acc1.AccountNumber)
Acc1.debit(10000)
Acc1.credit(500)
Acc1.credit(50000)
Acc1.debit(1000)