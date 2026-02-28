'''. Write a class Circle with attribute radius and methods:

area() — returns 3.14 * radius * radius
circumference() — returns 2 * 3.14 * radius'''
class Circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def circumference(self):
        return 2 * 3.14 * self.radius
circle1=Circle(5)
print(circle1.area())           
print(circle1.circumference())
