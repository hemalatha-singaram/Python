    class Animal:
        def __init__(self, name):
            self.name = name

        def eat(self):
            print(f"{self.name} is eating!")
    class Cat(Animal):   
        def meow(self):
            print(f"{self.name} says meow!")
    cat = Cat("kitty")
    cat.eat()   
    cat.meow()   