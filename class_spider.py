from class_animal import Animal


class Spider(Animal):
    """
    Spider: extends Animal only — not a Pet.
    8 legs. Overrides eat() with spider-specific behavior.
    walk() inherited from Animal — uses 8 legs.
    """

    def __init__(self):
        super().__init__(legs=8)

    def eat(self) -> None:
        """spiders trap and consume prey in their web"""
        print("Spider traps prey in its web and consumes it.")

    def __str__(self):
        return f"Spider | Legs: {self._legs}"
