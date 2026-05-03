from class_animal import Animal
from class_ipet import Pet


class Cat(Animal, Pet):
    """
    Cat: extends Animal AND implements Pet interface.
    4 legs. Has a name (Pet requirement).
    Overrides eat(). Implements getName, setName, play.
    walk() inherited from Animal.
    UML shows two constructors — modeled with optional name parameter.
    """

    def __init__(self, name: str = "Unknown"):
        Animal.__init__(self, legs=4)
        self._name = name           # protected — belongs to Pet interface context

    def get_name(self) -> str:
        """returns the cat's name"""
        return self._name

    def set_name(self, name: str) -> None:
        """sets the cat's name"""
        self._name = name

    def play(self) -> None:
        """cats play with yarn or chase things"""
        print(f"{self._name} is playing and chasing things around!")

    def eat(self) -> None:
        """cats eat cat food or hunt small prey"""
        print(f"{self._name} is eating cat food.")

    def __str__(self):
        return f"Cat | Name: {self._name} | Legs: {self._legs}"
