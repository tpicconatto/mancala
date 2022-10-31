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
        while (check): # while check is true
            hole = str(input("Please Enter Index of Hole: "))
            if hole in arr: # if the hole is in the array
                check = False
            else: # if the user entered a number out of bounds
                print("Enter number 0-5")
        hole = int(hole)
        return hole
