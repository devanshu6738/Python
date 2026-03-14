class Bank:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"Your money is successfully deposit, Now Your current balance is {self.balance}")

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f"money withdrawn, Now your available balance is {self.balance}")
    
    def DisplayBalance(self):
        print(f"Your Available Balance is  {self.balance}")

class SavingsAccount(Bank):
   def Add_Interest(self):
       interest=self.balance*0.05
       self.balance+=interest
       print(f"Interest added : {interest}")

class CurrentAccount(Bank):
    def Withdrawn(self,amount):
        if self.balance - amount < 1000:
            print("Minimum balance violation")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

s = SavingsAccount("Devanshu", 10000)

s.deposit(2000)
s.Add_Interest()
s.DisplayBalance()

        
