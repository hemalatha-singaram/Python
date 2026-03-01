from abc import ABC,abstractmethod
class Shape():
	@abstractmethod
	def area(self):
		pass
class Rectangle(Shape):
	def area(self):
		print(l*w)
class Circle(Shape):
	def area(self):
		print(3.14*r*r)
l=length=int(input("Enter length: "))
w=breadth=int(input("Enter breadth: "))
r=radius=int(input("Enter radius: "))
rect=Rectangle()
rect.area()
c=Circle()
c.area()
