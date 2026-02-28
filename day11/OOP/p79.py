class Student():
	def __init__(self,name,age,grade):
		self.name=name
		self.age=age
		self.grade=grade
	def introduce(self):
		print(f"Hi im {self.name},im {self.age} years old and my grade is {self.grade}")
hema=Student("Hema",20,"A")
sowmya=Student("Sowmya",20,"A")
hema.introduce()
sowmya.introduce()