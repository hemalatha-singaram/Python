class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # calls Animal's __init__
        self.breed = breed       # Dog's own extra attribute

dog = Dog("Bruno", "Labrador")
print(dog.name)    # Bruno   -- from Animal
print(dog.breed)   # Labrador -- from Dog