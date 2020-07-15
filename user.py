class User:
    def __init__ (self, user_name, email_address):
        self.name = user_name
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f"User:{self.name}, Balance:${self.account_balance}")
        return self 
    def transfer_money(self,other_user,amount):
        #decrease the user's balance by the amount and add that amount to other_user's balance 
        other_user.account_balance += amount
        self.account_balance -= amount
        
    

user_one = User('Nath', 'nathfan98@gmail.com')
user_one.make_deposit(1000)
user_one.make_deposit(350)
user_one.make_deposit(700)
user_one.make_withdrawal(50)


user_two = User('Pathy', 'path@gmail.com')
user_two.make_deposit(2000)
user_two.make_deposit(4000)
user_two.make_withdrawal(350)
user_two.make_withdrawal(650)

user_three = User('Fab', 'fab@gmail.com')
user_three.make_deposit(20000)
user_three.make_withdrawal(3400)
user_three.make_withdrawal(500)
user_three.make_withdrawal(600)

user_one.display_user_balance()
user_two.display_user_balance()
user_three.display_user_balance()

user_one.transfer_money(user_three, 500)
user_one.display_user_balance()
user_three.display_user_balance()