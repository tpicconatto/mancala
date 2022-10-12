from gameboard import Gameboard
from Player import Human

gameboard = Gameboard()
player1 = Human(1)
player2 = Human(2)

def Game(P1, P2):
    while (gameboard.isWinner()== False): #alternate players making a move, if there is a winner after each move exit while loop and find winner
        print(gameboard)
        index = P1.move()
        gameboard.play(P1,index,gameboard.getValue(0,index))
        print(gameboard)
        if(gameboard.isWinner()== True):
            gameboard.addRemaning()
            break
        index = P2.move()
        gameboard.play(P2,index,gameboard.getValue(1,index))
        if (gameboard.isWinner() == True):
            gameboard.addRemaining()
            break
    gameboard.findWinner()

Game(player1, player2)


