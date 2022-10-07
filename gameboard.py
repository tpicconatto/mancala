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
    def getValue(self, a ,b):
        return self.board[a][b]
    def isWinner(self): #Determines if someone one
        if self.board[0].count(0) == len(self.board[0]):
            return True
        elif self.board[1].count(0) == len(self.board[1]):
            return True
        else:
            return False
    def findWinner(self):
        if self.ends[1]> self.ends[2]:
            return "Player 1 WINS"
        elif self.ends[2]>self.ends[1]:
            return "Player 2 WINS"
        else:
            return "Tie"

    def play(self, player, index, quantity):
        if player == "Player 1":
            for i in range(quantity):
                if index > 0:
                    self.board[0][index] += 1
                if index == -1:
                    self.ends[0] += 1
                else:
                    self.board[1][abs(index) + 2] += 1
                index -= 1
        if player == "Player 2":
            for i in range(quantity):
                if index > 0:
                    self.board[1][index] += 1
                if index > len(self.board[1]):
                    self.ends[1] += 1
                    index = -len(self.board1)
                else:
                    self.board[0][abs(index)] += 1
                index += 1

    def addRemaining(self):  # Adds up all remaining points after game ends
            for i in range(len(self.board[0])):
                self.ends[0] = self.ends[0] + self.board[0][i]
            for j in range(len(self.board[1])):
                self.ends[1] = self.ends[1] + self.board[0][j]
