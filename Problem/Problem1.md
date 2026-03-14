Bank Management System (Inheritance Problem)
Problem Statement

Design a Bank Management System using inheritance.

Create a base class BankAccount with the following:

Attributes

account_holder

balance

Methods

deposit(amount) → adds money to balance

withdraw(amount) → withdraw money if balance is sufficient

display_balance() → prints current balance

Create Two Child Classes
1. SavingsAccount

Extra Feature:

Interest rate = 5%

Method:

add_interest()

This method should calculate interest and add it to balance.

2. CurrentAccount

Extra Feature:

Minimum balance = 1000

Override the withdraw() method so that:

If balance goes below 1000, print "Minimum balance violation".

Example Usage
s = SavingsAccount("Devanshu", 10000)
s.deposit(2000)
s.add_interest()
s.display_balance()

c = CurrentAccount("Rahul", 5000)
c.withdraw(4500)
Expected Output (Example)
Deposited: 2000
Interest Added
Balance: 12600

Minimum balance violation