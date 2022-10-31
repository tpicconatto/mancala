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
        arr = ["0", "1", "2", "3", "4", "5"]
        check = True
        while (check):
            hole = str(input("Please Enter Index of Hole: "))
            if hole in arr:
                check = False
            else:
                print("You are an idiot enter 0-5")  # funny, but not the most user friendly
        hole = int(hole)
        return hole
