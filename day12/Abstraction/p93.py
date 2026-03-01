from abc import ABC, abstractmethod

class Animal(ABC):        # abstract class
    @abstractmethod
    def sound(self):      # abstract method - no body!
        pass

    def eat(self):        # normal method - has body!
        print("Eating!")
class Dog(Animal):
    def sound(self):
        print("Woof!")
class Cat(Animal):
    def sound(self):
        print("Meow!")