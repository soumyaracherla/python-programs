class Account:
    def deposit(self,amount):
        print("this is account class deposited function")

    def withdraw(self,amount):
        print("this is account class withdraw function")


class SavingAccount(Account):
    # in encapsulation == we are hiding accno and balanace var
    __accountnumber =0  # use _attr_name to make it private
    __balance=0

    def __init__(self,accountnumber,balance):
        self.accountnumber=accountnumber
        self.balance=balance

    def deposit(self,amount):
        print("this is savingaccount class deposite")
        self.balance += amount
        print("current balance now is", self.balance)

    def withdraw(self,amount):
        print("this is savingaccount class withdrawal")
        self.balance-=amount
        print("current balance now is", self.balance)


obj= SavingAccount(1001,30000)
obj.deposit(5000)

obj.accountnumber=100001
print(obj.accountnumber)
