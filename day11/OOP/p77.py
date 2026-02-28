class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def describe(self):
        print(f"I am a {self.color} {self.brand}")

    def drive(self):
        print(f"{self.brand} is driving!")

car1 = Car("Toyota", "red")
car1.describe()   # I am a red Toyota
car1.drive()      # Toyota is driving!
#Modifying Object Data
car1 = Car("Toyota", "red")
print(car1.color)   # red

car1.color = "blue"  # change the color
print(car1.color)   # blue
