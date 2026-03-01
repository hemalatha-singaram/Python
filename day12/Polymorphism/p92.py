class Animal:
    def sound(self):
        print("Some animal sound")

class Dog(Animal):
    def sound(self):
        print("Woof!")

class Cat(Animal):
    def sound(self):
        print("Meow!")

animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.sound()

