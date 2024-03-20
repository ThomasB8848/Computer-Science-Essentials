"""
1st National Bank of Browntown Online Banking Application
This declares the customer as a name.
"""
class Customer():
#This is an OBJECT. It has properties of Withdraw, Deposit, BalanceCheck
    def __init__ (self, name, balance = 100.00):
        self.name = name
        self.balance = balance
        print("Account made for", name, " Current Balance: $", balance)
#This declares the withdraw function with the properties of amount, then takes the balance away from the amount, then returns the new balance.
    def withdraw(self,amount):
        self.balance = self.balance - amount
        return self.balance
#This declares the deposit function with the properties of amount, then adds the balance and the amount to give you the new balance 
    def deposit(self,amount):
        self.balance = self.balance + amount
        return self.balance
    #This declares and gives you the new balance of what you had before manipulating the withdraw and deposit functions.
    def check_balance(self):
        return self.balance
# This gives you welcome messages and instructions.
print("Welcome to the 1st National Bank of Browntown App")
print("All new customers get $100 deposited into their account for signing up!")
print()
name = input("Let's Get Started! What is your name: ")
customer = Customer(name)
# Gives you choices from 1 to 3, asking whether you would like to withdraw, deposit, or check your current balance.
while True:
    print("What would you like to do: (1) Withdraw   (2) Deposit   (3) Check Balance")
    choice = input("->")

    # This is the withdraw function.
    if choice == "1":
        print("How much are you withdrawing")
        amount = float(input("->"))
        customer.withdraw(amount)
        print("You have withdrawn ", amount)
        print("Your new balance is", customer.balance)

    # This is the depositing function.
    elif choice == "2":
        print("How much are you depositing")
        amount = float(input("->"))
        customer.deposit(amount)
        print("Your new balance is", customer.balance)

    # This is the Check balance function
    elif choice == "3":
        print("Your Balance is", customer.balance)

    # This is the "have a great day" message
else:
    print("Have a great day!")
        
