class BankAccount:

    def __init__(self, account_holder, balance):

        self.account_holder = account_holder

        self.balance = balance


    def show_balance(self):

        print("Current balance:", self.balance)


    def deposit(self, amount):

        self.balance = self.balance + amount

        print("Amount deposited successfully")


    def withdraw(self, amount):

        if amount <= self.balance:

            self.balance = self.balance - amount

            print("Amount withdrawn successfully")

        else:

            print("Insufficient balance")


b1 = BankAccount("Manoj", 20000)

b1.show_balance()

b1.deposit(5000)

b1.show_balance()

b1.withdraw(10000)

b1.show_balance()