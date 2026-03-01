class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def deposit(self, amount):
        if amount > 0:              
            self.__balance += amount
        else:
            print("Amount must be positive!")

    def withdraw(self, amount):
        if amount <= self.__balance:  
            self.__balance -= amount
        else:
            print("Insufficient funds!")

account = BankAccount("Hema", 1000)
print(account.get_balance())   
account.deposit(500)
print(account.get_balance())   
account.withdraw(200)
print(account.get_balance()) 
account.deposit(-999)          