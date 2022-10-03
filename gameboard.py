class Gameboard:
    board = [4,4,4,4,4,4],[4,4,4,4,4,4]
    ends = [0,0]
    print ("h")
    def __str__(self):
        stringV = str(self.ends[0])+"["
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
               stringV = stringV + " "+ str(self.board[i][j])
            stringV = stringV + "\n"
        stringV = stringV + "]"+str(self.ends[1])
        return stringV
    def isWinner(self):
        if self.board[0].count(0) == len(self.board[0]):
            return True
        elif self.board[1].count(0) == len(self.board[1]):
            return True
        else:
            return False