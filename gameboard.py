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
    def capture(self,player,side,index):
        if player.getNumber == 1:
            if numOpp != 0:
                while numOpp in self.board[1]:
                    self.ends[1] += numOpp
                    newIn = self.board[0].index(numOpp)
                    self.board[0].pop(newIn)
                    self.board.insert(newIn, 0)
            else:
                self.board[0][index] = 1


    def play(self, player, index, quantity):
        ogIndex = index
        if player.getNumber() == 1: #for player 1
            index -=1
            for i in range(quantity-1): #keeps going number of beads
                print(self)
                print(index)
                if index >= 0:
                    self.board[0][index] += 1
                elif index == -1:
                    self.ends[0] += 1
                else:
                    if abs(index)>=len(self.board[0]):
                        self.board[0][len(self.board[0])-1] += 1
                        index = len(self.board[0])-2
                    else:
                        self.board[1][abs(index) + 2] += 1
                index -= 1
            self.board[0][ogIndex] = 0
            if self.goAgain(index):
                return -1
            elif index > 0:
                if self.board[0][index] == 0:
                    side = 0
                    self.capture(self,player,side,index)
                    return 1
            elif index < 0:
                if self.board[0][abs(index)+2] == 0:
                    side = 1
                    self.capture(self,player,side,abs(index)+2)
                    return 1
                else:
                    self.board[1][abs(index)+2]+=1
                    return 1
                #
                #
        elif player.getNumber() == 2:
            index+=1
            for i in range(quantity-1):
                if index > 0:
                    self.board[1][index] += 1
                elif index > len(self.board[1]):
                    self.ends[1] += 1
                    index = -len(self.board[1]+1)
                else:
                    if index == -2:
                        self.board[1][0]+=1
                        index = 1
                    self.board[0][abs(index)+2] += 1
                index += 1
            if self.goAgain(index):
                return -1
            elif index >= 0:
                if self.board[1][index] == 0:
                    side = 1
                    self.capture(self, player, side, index)
                    return 1
            elif index < 0:
                if self.board[0][abs(index) + 2] == 0:
                    side = 0
                    self.capture(self, player, side, abs(index) + 2)
                    return 1

    def addRemaining(self):  # Adds up all remaining points after game ends
            for i in range(len(self.board[0])):
                self.ends[0] = self.ends[0] + self.board[0][i]
            for j in range(len(self.board[1])):
                self.ends[1] = self.ends[1] + self.board[0][j]
