from codecs import backslashreplace_errors


class BankAccount:
    all_accounts = []
    # don't forget to add some default values for these parameters!

    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount < 0:
            self.balance -= 5
            return print('Insufficient funds: Charging a $5 fee')
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f'Balance: ${self.balance}')

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

    @classmethod
    def display_all_accounts(cls):
        for account in cls.all_accounts:
            print(
                f'Interest Rate: {account.int_rate} | Balance: {account.balance}')


# account1 = BankAccount(0.01)
# account2 = BankAccount(1, 1000)

# account1.deposit(100).deposit(100).deposit(100).withdraw(
#     100).yield_interest().display_account_info()

# account2.deposit(100).deposit(100).withdraw(100).withdraw(100).withdraw(
#     100).withdraw(100).yield_interest().display_account_info()

# BankAccount.display_all_accounts()
