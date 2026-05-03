from abc import ABC, abstractmethod


class Pet(ABC):
    """
    Interface for pet animals.
    Any class implementing Pet must provide getName, setName, and play.
    In Python, interfaces are modeled as ABCs with only abstract methods.
    """

    @abstractmethod
    def get_name(self) -> str:
        """returns the pet's name"""
        pass

    @abstractmethod
    def set_name(self, name: str) -> None:
        """sets the pet's name"""
        pass

    @abstractmethod
    def play(self) -> None:
        """defines how the pet plays"""
        pass