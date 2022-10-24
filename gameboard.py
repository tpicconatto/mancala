class Gameboard:
    board = [4,4,4,4,4,4],[4,4,4,4,4,4]
    ends = [0,0]
    def __str__(self): #Prints the Board Out
        stringV = str(self.ends[0])+"["
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
               stringV = stringV + " "+ str(self.board[i][j])
            stringV = stringV + "\n" + "  "
        stringV = stringV + "]"+str(self.ends[1])
        return stringV
    def getValue(self, a ,b): #Returns quantity of beads in specific hole on board
        return self.board[a][b]
    def isWinner(self): #Determines if someone won
        if self.board[0].count(0) == len(self.board[0]): #if there are no more beads in side 0 there is a winner
            return True
        elif self.board[1].count(0) == len(self.board[1]): #if there are no more beads in side 1 there is a winner
            return True
        else: #if there are beads on both sides keep playing
            return False
    def findWinner(self): #finds which player won the game
        if self.ends[0]> self.ends[1]: #if the mancala of player 1 has more beads than player 2 then print player 1 wins
            return "Player 1 WINS"
        elif self.ends[1]>self.ends[0]:#if the mancala of player 2 has more beads than player 1 then print player 2 wins
            return "Player 2 WINS"
        else: #if they are equal print it's a tie
            return "Tie"
    def goAgain(self,index): #determines if the player landed in their mancala and can go again
        if index == 6:
            return True
        elif index == -2:
            return True
        else:
            return False

    def capture(self, player, side, index, numOpp): #Handles Capture according to variation
        if player.getNumber() == 1: #player 1 gets to capture
            if numOpp != 0: #has something to capture
                if side == 1: #empties landing index
                    self.ends[0] += numOpp
                    newIn = self.board[0].index(numOpp)
                    self.board[0].pop(newIn)
                    self.board[0].insert(newIn, 0)
                    print(self)
                    self.ends[0] += self.board[1][index]
                    self.board[1].pop(index)
                    self.board[1].insert(index, 0)
                    print(self)
                else: #empties landing index (other side)
                    self.ends[0] += numOpp
                    newIn = self.board[1].index(numOpp)
                    self.board[1].pop(newIn)
                    self.board[1].insert(newIn, 0)

                    self.ends[0] += self.board[0][index]
                    self.board[1].pop(index)
                    self.board[1].insert(index, 0)
                while numOpp in self.board[0]:
                    #captures all holes containing same number of stones (on top side)
                    self.ends[0] += numOpp
                    newIn = self.board[0].index(numOpp)
                    self.board[0].pop(newIn)
                    self.board[0].insert(newIn, 0)
                while numOpp in self.board[1]:
                    #captures all holes containing same number of stones (on bottom side)
                    self.ends[0] += numOpp
                    newIn = self.board[1].index(numOpp)
                    self.board[1].pop(newIn)
                    self.board[1].insert(newIn, 0)
        if player.getNumber() == 2: #player 2
            if numOpp != 0: #has something to capture
                if side == 1: #empties landing index
                    self.ends[1] += numOpp
                    newIn = self.board[0].index(numOpp)
                    self.board[0].pop(newIn)
                    self.board[0].insert(newIn, 0)
                    print(self)
                    self.ends[1] += self.board[1][index]
                    self.board[1].pop(index)
                    self.board[1].insert(index, 0)
                    print(self)
                else: #empties landing index(other side)
                    self.ends[1] += numOpp
                    newIn = self.board[1].index(numOpp)
                    self.board[1].pop(newIn)
                    self.board[1].insert(newIn, 0)

                    self.ends[1] += self.board[0][index]
                    self.board[1].pop(index)
                    self.board[1].insert(index, 0)
                while numOpp in self.board[0]:
                    # captures all holes containing same number of stones (on top side)
                    self.ends[1] += numOpp
                    newIn = self.board[0].index(numOpp)
                    self.board[0].pop(newIn)
                    self.board[0].insert(newIn, 0)
                while numOpp in self.board[1]:
                    # captures all holes containing same number of stones (on bottom side)
                    self.ends[1] += numOpp
                    newIn = self.board[1].index(numOpp)
                    self.board[1].pop(newIn)
                    self.board[1].insert(newIn, 0)
        print(self)

    def play(self, player, index, quantity):
        if player.getNumber() == 1:  # for player 1
            ogIndex = index
            self.board[0][ogIndex] = 0
            index -= 1
            for i in range(quantity):  # keeps going number of beads
                print(self)
                print("index=", index, "quantity=", quantity)
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
            if self.goAgain(index):
                return -1
            # capture
            elif index >= -1:
                if self.board[0][index + 1] == 1:
                    side = 0
                    numOpp = self.board[1][index + 1]
                    self.capture(player, side, index, numOpp)
                return 1
            elif index < 0:
                if self.board[1][abs(index) - 3] == 1:
                    side = 1
                    numOpp = self.board[0][abs(index) - 3]
                    help = abs(index) - 3
                    self.capture(player, side, help, numOpp)
                return 1
                #
                #
        elif player.getNumber() == 2:
            ogIndex = index
            self.board[1][ogIndex] = 0
            num = -1
            if player.getNumber() == 2:  # for player 2
                for i in range(quantity):  # keeps going number of beads
                    print(self)
                    print("index=", i, "quantity=", quantity)

                    if index < len(self.board[1]) - 1:
                        self.board[1][index + 1] += 1
                    elif index == len(self.board[1])-1:
                        self.ends[1] += 1
                    else:
                        if abs(index) > 12:
                            self.board[1][0]+=1
                            index = 1
                        else:
                            num +=2
                            self.board[0][abs(index)-num] += 1
                    index += 1
                print(self)
                if self.goAgain(index):
                    return -1
                elif index > 6:
                    index = 12-index
                    if self.board[0][index] == 1:
                     numOpp = self.board[1][index]
                     side = 0
                     self.capture(player, side, index,numOpp)
                    return 1
                elif index < 6:
                    if self.board[1][index] == 1:
                        numOpp = self.board[0][index]
                        side = 1
                        self.capture(player, side, index,numOpp)
                    return 1

    def addRemaining(self):  # Adds up all remaining points after game ends
            for i in range(len(self.board[0])):
                self.ends[0] = self.ends[0] + self.board[0][i]
            for j in range(len(self.board[1])):
                self.ends[1] = self.ends[1] + self.board[0][j]