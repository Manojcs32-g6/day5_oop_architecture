class BankAccount:

    def __init__(self, balance):

        self.__balance = balance


    def deposit(self, amount):

        self.__balance += amount

        print("Amount deposited")


    def withdraw(self, amount):

        if amount <= self.__balance:

            self.__balance -= amount

            print("Amount withdrawn")

        else:

            print("Insufficient balance")


    def show_balance(self):

        print("Current Balance:", self.__balance)


b1 = BankAccount(10000)

b1.deposit(5000)

b1.withdraw(3000)

b1.show_balance()