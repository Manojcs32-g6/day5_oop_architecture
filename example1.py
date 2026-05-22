class NetflixAccount:

    def __init__(self, subscription_balance):

        self.__subscription_balance = subscription_balance

        self.movies_watched = 0


    def add_balance(self, bal):

        self.__subscription_balance += bal

        print("Balance added successfully")


    def watch_movie(self):

        if self.__subscription_balance <= 0:

            print("Recharge required")

        else:

            print("Movie started")

            self.__subscription_balance -= 1

            self.movies_watched += 1


    def show_balance(self):

        print("Balance:", self.__subscription_balance)

        print("Movies Watched:", self.movies_watched)


n1 = NetflixAccount(5)

n1.watch_movie()

n1.watch_movie()

n1.add_balance(10)

n1.show_balance()