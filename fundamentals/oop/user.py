class User:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        if (self.account_balance - amount < 0):
            return print('Error: Balance can not go below 0.')
        self.account_balance -= amount

    def display_user_balance(self):
        return f'User: {self.name}, Balance: {self.account_balance}'

    def transfer_money(self, user, amount):
        if self.account_balance - amount < 0:
            return print('Error: Balance can not go below 0.')
        self.make_withdrawal(amount)
        user.make_deposit(amount)


account1 = User('Dawson', 'temp1@mail.com')
account2 = User('Joe', 'temp2@mail.com')
account3 = User('Person', 'temp3@mail.com')

account1.make_deposit(3)
account1.make_deposit(50)
account1.make_deposit(200)
print(account1.display_user_balance())

account2.make_deposit(1)
account2.make_deposit(1)
account2.make_withdrawal(1)
account2.make_withdrawal(2)  # Error, cannot go below zero
print(account2.display_user_balance())

account3.make_deposit(1000)
account3.make_withdrawal(100)
account3.make_withdrawal(50)
account3.make_withdrawal(25)
print(account3.display_user_balance())

account1.transfer_money(account3, 100)
print(account1.display_user_balance())
print(account3.display_user_balance())

account2.transfer_money(account1, 1000000)  # Error, cannot go below 0.
print(account1.display_user_balance())
print(account2.display_user_balance())
