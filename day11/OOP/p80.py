'''Challenge 2: Create a class BankAccount with attributes owner and balance. Add methods:

deposit(amount) — adds to balance
withdraw(amount) — subtracts from balance
show_balance() — prints current balance'''
class BankAccount():
	def __init__(self,owner,balance):
		self.owner=owner
		self.balance=balance
	def deposit(self, amount):
    		self.balance += amount  # no need for self.amount
    		print(f"Deposited ${amount}. New balance: ${self.balance}")
	def withdraw(self,amount):
		self.amount=amount
		if self.amount <= self.balance:
			self.balance -= self.amount
			print(f"Withdrew ${self.amount}. New balance: ${self.balance}")
		else:
			print("Insufficient funds!")
			
	def show_balance(self):
		print(f"Current balance for {self.owner}: ${self.balance}")
account1=BankAccount("Hema",1000)
account1.show_balance()  
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(1500)
