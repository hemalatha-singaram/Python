class Bank:
    def __init__(self, balance):
        self.__balance = balance   # private

    def show_balance(self):
        print(self.__balance)
b = Bank(1000)
b.show_balance()      # works
print(b.__balance)    # ERROR