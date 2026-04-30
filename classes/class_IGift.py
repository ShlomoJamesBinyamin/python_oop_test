from abc import ABC, abstractmethod

class IGift(ABC):
    @abstractmethod
    def open_gift(self):
        pass