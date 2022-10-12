import gameboard from gameboard
gameboard = Gameboard()
def Game(P1, P2):
    while (gameboard.isWinner()==false): #alternate players making a move, if there is a winner after each move exit while loop and find winner
        P1.move()
        P1.play(P1,P1.move(),getValue())
        if(gameboard.isWinner()==true):
            break
        P2.move()
        P2.play(P2,P2.move(),getValue())
    findWinner()
