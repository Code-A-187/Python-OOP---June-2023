class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def make_sound(self):
        return 'woof-woof'


class Cat(Animal):
    def make_sound(self):
        return 'meow'


class Chicken(Animal):
    def make_sound(self):
        return "chwerk chwerk"


def animal_sound(Animal: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat('fluffy'), Dog('puhcho'), Chicken('stanka')]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
