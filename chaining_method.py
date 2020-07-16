class User:
    def __init__ (self, user_name, email_address):
        self.name = user_name
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"User:{self.name}, Balance:${self.account_balance}")
        return self 
    def transfer_money(self,other_user,amount):
        #decrease the user's balance by the amount and add that amount to other_user's balance 
        other_user.account_balance += amount ##could also say other_user.make_deposit(amount)
        self.account_balance -= amount ##could also say self.make_withdrawal(amount)
        return self
        
user_one = User('Nath','nathfan@gmail.com')
user_two = User('Pathy', 'path@gmail.com')
user_three = User('Fab', 'fab@gmail.com')

user_one.make_deposit(1000).make_deposit(350).make_deposit(700).make_withdrawal(500).display_user_balance()
user_two.make_deposit(2000).make_deposit(4000).make_withdrawal(350).make_withdrawal(650).display_user_balance()
user_three.make_deposit(20000).make_withdrawal(3400).make_withdrawal(500).make_withdrawal(600).display_user_balance()
user_one.transfer_money(user_three,500).display_user_balance()
user_three.display_user_balance()
