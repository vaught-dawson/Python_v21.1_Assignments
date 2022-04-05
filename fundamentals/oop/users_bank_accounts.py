import bank_account


class User:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.accounts = {}

    def make_deposit(self, amount, account_name):
        if not account_name in self.accounts:
            return print(f'Account {account_name} not found. Please make an account first.')
        self.accounts[account_name].deposit(amount)
        return self

    def make_withdrawal(self, amount, account_name):
        if not account_name in self.accounts:
            return print(f'Account {account_name} not found. Please make an account first.')
        self.accounts[account_name].withdraw(amount)
        return self

    def display_user_balance(self, account_name):
        if not account_name in self.accounts:
            return print(f'Account {account_name} not found. Please make an account first.')
        print(account_name)
        self.accounts[account_name].display_account_info()
        return self

    def transfer_money(self, other_user, other_account_name, amount, account_name):
        if not account_name in self.accounts:
            return print(f'Account {account_name} not found. Please make an account first.')
        if not other_account_name in other_user.accounts:
            return print(f'Account {other_account_name} not found. Please make an account first.')

        # Making sure the money was successfully withdrawn
        withdrawal_response = self.accounts[account_name].withdraw(amount)
        if not withdrawal_response == None:
            other_user.make_deposit(amount, other_account_name)
        return self

    def add_account(self, account_name, account):
        self.accounts[account_name] = account
        return self

    def remove_account(self, accunt_name):
        del self.accounts[accunt_name]
        return self


account1 = User('Dawson', 'temp1@mail.com')
account2 = User('Joe', 'temp2@mail.com')
account3 = User('Person', 'temp3@mail.com')

account1.make_deposit(100, 'Checking')
account1.add_account('Checking', bank_account.BankAccount(0.02, 0))
account1.make_deposit(100, 'Checking').display_user_balance('Checking')
account1.add_account('Savings', bank_account.BankAccount(
    0.02, 1000)).display_user_balance('Savings')

account2.add_account('Checking', bank_account.BankAccount(0.02, 1000))
account2.transfer_money(account1, 'Savings', 10000, 'Checking')
account2.transfer_money(account1, 'Savings', 100,
                        'Checking').display_user_balance('Checking')
account1.display_user_balance('Savings')
