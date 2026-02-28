class Calculator():
	def add(self,a,b):
		return a+b
	def sub(self,a,b):
		return a-b
	def mul(self,a,b):
		return a*b
	def div(self,a,b):
		if b==0:
			return "cant divide by zero"
		return a/b
calc=Calculator()
print(calc.add(5, 3))      
print(calc.sub(10, 4))
print(calc.mul(3, 4)) 
print(calc.div(10, 2)) 