from gameboard import Gameboard
from Player import Human

gameboard = Gameboard()
player1 = Human(1)
player2 = Human(2)

def Game(P1, P2):
    while (gameboard.isWinner()== False): #alternate players making a move, if there is a winner after each move exit while loop and find winner
        gameboard.play(P1,P1.move(),gameboard.getValue())
        print(gameboard)
        if(gameboard.isWinner()== True):
            break
        gameboard.play(P2,P2.move(),gameboard.getValue())
        print(gameboard)
    gameboard.findWinner()

Game(player1, player2)


