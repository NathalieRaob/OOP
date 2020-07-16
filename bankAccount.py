class BankAccount:
    def __init__(self,int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = 0
    def deposit(self, amount):
        #increases the account balance by the given amount
        self.balance += amount
        return self
    def withdraw(self, amount):
        #decreases the account balance by the given amount if there are sufficient funds
        #if there is not enough money, print a message "insufficient funds: Charging a $5 fee" and deduct $5
        self.balance -= amount 
        if self.balance < amount:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")      
        return self 
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self 
    def yield_interest(self):
        #increases the account balance by the current balance * the interest rate(as long as the balance is positive)
        #calculated the interest rate in a year 
        if self.balance > 0:
            self.int_rate *= self.balance
            print(f"rate: {self.int_rate}")
        return self 

    
first_account = BankAccount()
first_account.deposit(500).deposit(3000).deposit(700).withdraw(600).yield_interest().display_account_info()

second_account = BankAccount()
second_account.deposit(400).deposit(800).withdraw(500).withdraw(400).withdraw(300).withdraw(900).yield_interest().display_account_info()



#SOLUTION 
class BankAccount:
    def __init__(self, int_rate=0, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else: 
            self.balance -= 5
            print("Insufficient Funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self 

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.int_rate
            print(f"Rate:{self.int_rate}")
        return self 

ba1 = BankAccount(balance=100)
ba2 = BankAccount(.01, 500)

ba1.deposit(500).deposit(3000).deposit(700).withdraw(600).yield_interest().display_account_info()
ba2.deposit(100).deposit(100).withdraw(100).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()