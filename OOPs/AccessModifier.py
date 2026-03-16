# Create a class BankAccount with the following requirements:

# Public variable

# account_holder → name of the account holder.

# Protected variable

# _account_type → savings or current account.

# Private variable

# __balance → account balance (should not be accessed directly).

# Create the following methods:

# deposit(amount) → add money to the account.

# withdraw(amount) → withdraw money if balance is sufficient.

# show_balance() → display the current balance.

# Demonstrate:

# Accessing public variables

# Accessing protected variables

# Restriction on private variables.

class BankAccount:
    def __init__(self,name,acc_type,balance):
        self.name=name
        self._acc_type=acc_type
        self.__balance=balance

    def Deposit_Amount(self,amount):
        self.__balance+=amount
        print("Deposited :",amount)

    def WithdrawAmount(self,amount):
        if self.__balance >= amount:
            self.__balance-=amount
            print("money withdrawn !! Available Balance:",self.__balance)
            print()
        else:
            print("insufficient balance")

    def Display_Balance(self):
        print(self.__balance)

    
Devanshu=BankAccount("Devanshu","saving",2000)
Devanshu.Deposit_Amount(1000)
Devanshu.WithdrawAmount(2000)
# print(Devanshu.__balance) error 


