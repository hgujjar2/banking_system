from abc import ABC, abstractmethod

class bankaccount(ABC):
    #constructor
    def __init__(self,account_number,account_type,account_holder):
        self.account_number = account_number # include account _number as an attribute
        self.account_type = account_type
        self.account_holder = account_holder
        self.balance = 0
# decorator
    @abstractmethod
    def deposit(self,amount):
        pass
    @abstractmethod
    def withdrawl(self, amount) :
        pass

    def display_balance(self):
        return self.balance
 # making class
class savingsaccount(bankaccount):
#defining method
    def deposit(self, amount):
        if amount >0:
            self.balance +=amount
            print(f"deposited ${amount:.2f} into {self.account_type} account for {self.account_holder}.")
        else:
            print("invalid deposit ammount")
# defining 2nd method
    def withdrawl(self, amount):
        if amount > 0 and self.balance>=amount:
            self.balance -= amount
            print(f"withdraw ${amount:.2f} into {self.account_type} account for {self.account_holder}.")
        else:
            print("invalid withdrawl amount or insufficient amount")
# 2nd class
class currentaccount(bankaccount):
# call constructor to add additional attribute (overdraft_limit)
    def __init__(self, account_number, account_type, account_holder, overdraft_limit=100):
        super().__init__(account_number, account_type, account_holder)
        self.overdraft = overdraft_limit
    def deposit(self, amount):
        if amount >0:
            self.balance += amount
            print(f"deposited ${amount:.2f} into {self.account_type} account for {self.account_holder}.")
        else:
            print("invalid deposit amount")
    def withdrawl(self, amount):
        if amount > 0 and (self.balance + self.overdraft_limit) >=amount:
            self.balance -= amount
            print(f"withdraw ${amount:.2f} into {self.account_type} account for {self.account_holder}.")
        else:
            print("invalid withdrawl amount or overdraft limit exceed.")

 # dictionary to store amount information
accounts = {}

  # dictionary to map account numbers to account holders
account_numbers = {}

  #user input for creating accounts and trasactions
while True:
    print("\nSelect an option:")
    print("1. create account")
    print("2. deposit")
    print("3. withdraw")
    print("4. display account balances")
    print("5. Quit")

    choice = input("enter your choice:")

    if choice == "1":
        account_type = input("enter account type (savings or current):")
        account_holder = input("enter account holder's name:")
        account_number = input("enter account number:")

# check if the account number alrady exists

        if account_number in account_numbers:
            print('Account already created')
        else:
# create the account
# and use .lower to lower case all the code to avoid mistakes
            if account_type.lower()=="savings" or account_type.lower() =="current":
                if account_type.lower()== "savings":
                    accounts[account_holder] = savingsaccount(account_number, account_type, account_holder)
                else:
                    accounts[account_holder] = currentaccount(account_number, account_type, account_holder)
                account_numbers[account_number] = account_holder
                print(f"{account_holder}'s {account_type} account created successfully. ")
            else:
                print("invalid account type.")
# use elif statement to deposit 

    elif choice == "2":
        account_holder = input("enter account holer's name")
        if account_holder in accounts:
            account_type = accounts[account_holder].account_type
            amount = float(input(f"enter deposit amount for {account_holder}'s {account_type} account:"))
            accounts[account_holder].deposit(amount)
        else:
            print("account holder not found")
# use elif statement to withdraw
    elif choice =="3":
        account_holder = input("enter account holer's name")
        if account_holder in accounts:
            account_type = accounts[account_holder].account_type
            amount = float(input(f"enter withdrawl amount for {account_holder}'s {account_type} account:"))
            accounts[account_holder].withdrawl(amount)
        else:
            print("account holder not found")
# to check account balance
    elif choice =="4":
        for account_holder, account in accounts.items():
            print(f"{account_holder}'s {account.account_type} account balance: ${account.display_balance():.2f}")
# to exit
    elif choice == "5":
        print("exiting the banking system.")
        break

    else:
        print("invalid choice.please try again.")





    
