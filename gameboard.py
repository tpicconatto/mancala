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
            print("finding winner")
            return True
        elif self.board[1].count(0) == len(self.board[1]):
            print("finding winner")
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
            return True
        elif index == -2:
            return True
        else:
            return False

    def capture(self, player, side, index, numOpp):
        print("into capture")
        print(str(player.getNumber()))
        print(str(numOpp))
        print(str(index))
        if player.getNumber() == 1:
            if numOpp != 0:
                print("into capture")
                if side == 1:
                    print("into capture")
                    self.ends[0] += numOpp
                    newIn = self.board[0].index(numOpp)
                    self.board[0].pop(newIn)
                    self.board[0].insert(newIn, 0)
                    print(self)
                    self.ends[0] += self.board[1][index]
                    self.board[1].pop(index)
                    self.board[1].insert(index, 0)
                    print(self)
                else:
                    self.ends[0] += numOpp
                    newIn = self.board[1].index(numOpp)
                    self.board[1].pop(newIn)
                    self.board[1].insert(newIn, 0)

                    self.ends[0] += self.board[0][index]
                    self.board[1].pop(index)
                    self.board[1].insert(index, 0)
                while numOpp in self.board[0]:
                    print("enter loop")
                    self.ends[0] += numOpp
                    newIn = self.board[0].index(numOpp)
                    self.board[0].pop(newIn)
                    self.board[0].insert(newIn, 0)
                while numOpp in self.board[1]:
                    print("enter loop two")
                    self.ends[0] += numOpp
                    newIn = self.board[1].index(numOpp)
                    self.board[1].pop(newIn)
                    self.board[1].insert(newIn, 0)
        print("finish capture")
        print(self)

    def play(self, player, index, quantity):
        if player.getNumber() == 1:  # for player 1
            ogIndex = index
            self.board[0][ogIndex] = 0
            index -= 1
            for i in range(quantity):  # keeps going number of beads
                print(self)
                print("index=", index, "i=", i, "quantity=", quantity)

                if index >= 0:
                    self.board[0][index] += 1
                elif index == -1:
                    self.ends[0] += 1
                else:
                    if abs(index) >= len(self.board[1]):
                        self.board[0][len(self.board[0]) - 1] += 1
                        index = 0
                    else:
                        self.board[1][abs(index) - 2] += 1
                index -= 1
            print(self)
            print("index=", index, "quantity=", quantity)
            if self.goAgain(index):
                return -1
            # capture
            elif index >= 0:
                if self.board[0][index + 1] == 1:
                    side = 0
                    numOpp = self.board[1][index + 1]
                    self.capture(self, player, side, index, numOpp)
                return 1
            elif index < 0:
                print("got here")
                print("index=", index, "quantity=", quantity)
                if self.board[1][abs(index) - 3] == 1:
                    side = 1
                    numOpp = self.board[0][abs(index) - 3]
                    print("nummOpp = " + str(numOpp))
                    help = abs(index) - 3
                    self.capture(player, side, help, numOpp)
                return 1
                #
                #
        elif player.getNumber() == 2:
            ogIndex = index
            self.board[1][ogIndex] = 0
            if player.getNumber() == 2:  # for player 2
                for i in range(quantity):  # keeps going number of beads
                    print(self)
                    print("index=", index, "i=", i, "quantity=", quantity)

                    if index < len(self.board[1]) - 1:
                        self.board[1][index + 1] += 1
                    elif index == len(self.board[1]):
                        self.ends[1] += 1
                    else:
                        if abs(index) > len(self.board[1]) + 1:
                            self.board[1][len(self.board[1]) + 1] += 1
                            index = 0
                        else:
                            self.board[0][abs(index)] += 1
                    index += 1
                print(self)
                print("index=", index, "quantity=", quantity)
                if self.goAgain(index):
                    return -1
                elif index + 1 >= 0:
                    # if self.board[1][index] == 0:
                    side = 0
                    # self.capture(self, player, side, index)
                    return 1
                elif index + 1 < 0:
                    if self.board[0][abs(index) - 2] == 0:
                        side = 1
                        self.capture(self, player, side, abs(index) - 2)
                        return 1
                    else:
                        self.board[0][abs(index) - 2] += 1
                        return 1

    def addRemaining(self):  # Adds up all remaining points after game ends
            for i in range(len(self.board[0])):
                self.ends[0] = self.ends[0] + self.board[0][i]
            for j in range(len(self.board[1])):
                self.ends[1] = self.ends[1] + self.board[0][j]