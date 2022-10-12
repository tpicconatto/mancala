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
    def isWinner(self): #Determines if someone won
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
    def goAgain(self,index):
        if index > len(self.board[1]):
            self.ends[1] += 1
            return True
        elif index == -1:
            self.ends[0] += 1
            return True
        else:
            return False
    def capture(self,player,index, side):
        total = 1
        self.board[side][index] = 0
        if side == 0: # if we are on side 1
            cap = self.board[1][index]
            total = total + cap
            self.board[1][index] = 0
        else: # if we are on side 1
            cap = self.board[0][index]
            total = total + cap
            self.board[0][index] = 0

        for i in range(2): # goes through 2D array to see if any other holes have the same anount of stones that were captured
            for j in range(6):
                if self.board[i,j] == cap: # if the hole we are at has the same number of stones then cap
                    total = total + cap
                    self.board[i,j] = 0

        if player.getNumber == 1:  # if we are player one (to decide which moncala to add to)
            self.ends[0] = self.ends[0] + cap
        else: # if we are player two (to decide which moncala to add to)
            self.ends[1] = self.ends[1] + cap

    def play(self, player, index, quantity):
        if player.getNumber() == 1: #for player 1
            for i in range(quantity-1): #keeps going number of beads
                if index > 0:
                    self.board[0][index] += 1
                if index == -1:
                    self.ends[0] += 1
                else:
                  if abs(index)>=len(self.board[0]):
                      self.board
                    self.board[1][abs(index) + 2] += 1
                index -= 1
            if self.goAgain(index):
                return -1
            elif index > 0:
                if self.board[0][index] == 0:
                    side = 0
                    self.capture(self,player,side,index)
            elif index <

        if player.getNumber() == 2:
            for i in range(quantity-1):
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
