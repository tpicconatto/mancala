from gameboard import Gameboard
from Player import Human
from Player import Player

gameboard = Gameboard()
player1 = Human(Player(1))
player2 = Human(Player(2))

def Game(P1, P2):
    while (gameboard.isWinner()== False): #alternate players making a move, if there is a winner after each move exit while loop and find winner
        P1.move()
        P1.play(P1,P1.move(),gameboard.getValue())
        print(gameboard)
        if(gameboard.isWinner()== True):
            break
        P2.move()
        P2.play(P2,P2.move(),gameboard.getValue())
        print(gameboard)
    gameboard.findWinner()

Game(player1, player2)


