from abc import ABC, abstractmethod
class Player(ABC):
    @abstractmethod
    def move(self):
        pass
class Human(Player):
    def move(self):
        hole = int(input("Please Enter Index of Hole"))
        return hole
