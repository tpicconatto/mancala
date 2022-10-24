from abc import ABC, abstractmethod
class Player(ABC):
    playernum = 0

    def __init__(self, playerNum):
        self.playerNum = playerNum
    def getNumber(self):
        return self.playerNum
    @abstractmethod
    def move(self):
        pass
class Human(Player):
    def move(self):
        hole = int(input("Please Enter Index of Hole: "))
        return hole
