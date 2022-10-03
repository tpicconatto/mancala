class Gameboard:
    board = [4,4,4,4,4,4],[4,4,4,4,4,4]
    ends = [0,0]
    def __str__(self): #Prints the Board Out
        stringV = str(self.ends[0])+"["
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
               stringV = stringV + " "+ str(self.board[i][j])
            stringV = stringV + "\n"
        stringV = stringV + "]"+str(self.ends[1])
        return stringV
    def isWinner(self): #Determines if someone one
        if self.board[0].count(0) == len(self.board[0]):
            return True
        elif self.board[1].count(0) == len(self.board[1]):
            return True
        else:
            return False
    def addRemaining(self): #Adds up all remaining points after game ends
        for i in range(len(self.board[0])):
            self.ends[0] = self.ends[0] + self.board[0][i]
        for j in range(len(self.board[1])):
            self.ends[1] = self.ends[1] + self.board[0][j]
    def findWinner(self):
        if self.ends[1]> self.ends[2]:
            return "Player 1 WINS"
        elif self.ends[2]>self.ends[1]:
            return "Player 2 WINS"
        else:
            return "Tie"

