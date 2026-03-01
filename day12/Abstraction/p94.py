from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def eat(self):
        print("Eating!")

class Dog(Animal):
    def sound(self):      # MUST implement this!
        print("Woof!")

class Cat(Animal):
    def sound(self):      # MUST implement this!
        print("Meow!")

# animal = Animal()  # ❌ ERROR! Can't create abstract object
dog = Dog()
dog.sound()   # Woof!
dog.eat()     # Eating!