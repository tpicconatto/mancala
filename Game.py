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
    def addRemaining(self): #Adds up all remaining points after game ends
        for i in range(len(self.board[0])):
            self.ends[0] = self.ends[0] + self.board[0][i]
        for j in range(len(self.board[1])):
            self.ends[1] = self.ends[1] + self.board[0][j]