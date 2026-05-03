from class_animal import Animal
from class_ipet import Pet


class Fish(Animal, Pet):
    """
    Fish: extends Animal AND implements Pet interface.
    0 legs. Has a name (Pet requirement).
    Overrides walk() — fish swim, not walk.
    Overrides eat(). Implements getName, setName, play.
    UML explicitly shows walk() on Fish — meaning it overrides Animal.walk().
    """

    def __init__(self):
        Animal.__init__(self, legs=0)
        self._name = "Unknown"

    def get_name(self) -> str:
        """returns the fish's name"""
        return self._name

    def set_name(self, name: str) -> None:
        """sets the fish's name"""
        self._name = name

    def play(self) -> None:
        """fish play by swimming around the tank"""
        print(f"{self._name} is swimming playfully around the tank!")

    def walk(self) -> None:
        """fish cannot walk — they swim instead"""
        print(f"{self._name} cannot walk, but swims gracefully.")

    def eat(self) -> None:
        """fish eat flakes or small organisms"""
        print(f"{self._name} nibbles on fish flakes.")

    def __str__(self):
        return f"Fish | Name: {self._name} | Legs: {self._legs}"
