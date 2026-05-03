from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for all animals.
    Protected legs attribute — subclasses define leg count via constructor.
    walk() is concrete — shared behavior.
    eat() is abstract — every animal eats differently.
    """

    def __init__(self, legs: int):
        self._legs = legs       # protected — single underscore convention

    @property
    def legs(self) -> int:
        return self._legs

    def walk(self) -> None:
        """default walk behavior — uses leg count"""
        print(f"Walking on {self._legs} legs.")

    @abstractmethod
    def eat(self) -> None:
        """each animal eats differently — must be implemented by subclass"""
        pass

    def __str__(self):
        return f"{self.__class__.__name__} | Legs: {self._legs}"
