class Gameboard:
    board = [4,4,4,4,4,4],[4,4,4,4,4,4]
    ends = [0,0]
    def __str__(self): #Prints the Board Out
        stringV = str(self.ends[0])+"["
        for i in range(len(self.board)): # these 2 4 loops go through the board to print it out
            for j in range(len(self.board[i])):
               stringV = stringV + " " + str(self.board[i][j])
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
            return "Player 1 WINS: " + str(self.ends[0])+" to "+str(self.ends[1])
        elif self.ends[1]>self.ends[0]:#if the mancala of player 2 has more beads than player 1 then print player 2 wins
            return "Player 2 WINS: "+str(self.ends[1])+" to "+str(self.ends[0])
        else: #if they are equal print it's a tie
            return "Tie " +str(self.ends[0])+" to "+str(self.ends[1])
    def goAgain(self,index): #determines if the player landed in their mancala and can go again
        if index == 6: #if player lands in index of 6 then go again
            return True
        elif index == -2: #if player lands in index of -2 then go again
            return True
        else: #if player lands in any other index, they dont get to go again
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
                    self.board[0].pop(index)
                    self.board[0].insert(index, 0)
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
                    self.board[0].pop(index)
                    self.board[0].insert(index, 0)
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
                    if abs(index) > 7:
                        self.board[0][5] += 1
                        index = 5
                    else:
                        self.board[1][abs(index) - 2] += 1
                index -= 1
            print(self)
            print(index)
            if self.goAgain(index):
                return -1
            # capture
            elif index >= -1:
                if self.board[0][index + 1] == 1:
                    side = 0
                    index+=1
                    numOpp = self.board[1][index]
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
        elif player.getNumber() == 2: #if player is player 2
            ogIndex = index
            self.board[1][ogIndex] = 0
            num = -1
            for i in range(quantity):  # keeps going number of beads
                print(self)
                print("index=", i, "quantity=", quantity)

                if index < len(self.board[1]) - 1: #if index is within this sides boundaries, add 1 to the next hole
                    self.board[1][index + 1] += 1
                elif index == len(self.board[1])-1: #if it is one index past the length of this side, add to the mancala
                    self.ends[1] += 1
                else:
                    if abs(index) > 12: #if it is past the boundaries on the other side, go back to the original side at index 0
                        self.board[1][0]+=1
                        index = 1
                    else: #is it is past one index above the length, switch to other board and add to corresponding index
                        num +=2
                        self.board[0][abs(index)-num] += 1
                index += 1
            print(self)
            if self.goAgain(index): #if go again true return -1
                return -1
            elif index > 6: #if past boundaries of side check if should capture and return 1
                index = 12-index
                if self.board[0][index] == 1: #check if should capture
                    numOpp = self.board[1][index]
                    side = 0
                    self.capture(player, side, index,numOpp)
                return 1
            elif index < 6: #if index within boundaries check if should capture and return 1
                if self.board[1][index] == 1: #check if should capture
                    numOpp = self.board[0][index]
                    side = 1
                    self.capture(player, side, index,numOpp)
                return 1

    def addRemaining(self):  # Adds up all remaining points after game ends
            for i in range(len(self.board[0])): #adds the remaining stone for p1
                self.ends[0] = self.ends[0] + self.board[0][i]
                self.board[0][i]=0
            for j in range(len(self.board[1])): #adds the remaining stones for P1
                self.ends[1] = self.ends[1] + self.board[1][j]
                self.board[1][j] = 0