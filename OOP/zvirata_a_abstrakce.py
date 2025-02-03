from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        return "Sound"

    def describe(self):
        return f"Im {self.__class__.__name__} and I {self.sound()}!"

class Dog(Animal):
        def sound(self):
            return "Bark"

class Cat(Animal):
        def sound(self):
            return "Meow"

class Cow(Animal):
        def sound(self):
            return "Mooo"

class Karlik(Animal):
        def sound(self):
            return "Moneyyyy"

        def describe(self):
            return f"Jmenuju se {self.__class__.__name__} a tohle tezce nedavam..."


def check(animals: list[Animal]) -> list[tuple[str, str]]:
    lst = []
    for animal in animals:
        tup = ()
        tup = animal.sound(), animal.describe() 
        lst.append(tup)
    return lst

# Tests
dog = Dog()
assert dog.sound() == "Bark"
assert dog.describe() == "Im Dog and I Bark!"

cat = Cat()
assert cat.sound() == "Meow"
assert cat.describe() == "Im Cat and I Meow!"

cow = Cow()
assert cow.sound() == "Mooo"
assert cow.describe() == "Im Cow and I Mooo!"

karlik = Karlik()
assert karlik.sound() == "Moneyyyy"
assert karlik.describe() == "Jmenuju se Karlik a tohle tezce nedavam..."

assert check([dog, cat]) == [("Bark", "Im Dog and I Bark!"), ("Meow", "Im Cat and I Meow!")]

