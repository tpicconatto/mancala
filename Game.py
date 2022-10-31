from gameboard import Gameboard
from Player import Human

gameboard = Gameboard()
player1 = Human(1)
player2 = Human(2)

def Game(P1, P2):
    while (gameboard.isWinner()== False): #alternate players making a move, if there is a winner after each move exit while loop and find winner
        print("Player 1")
        print(gameboard)
        print ("Player 1")
        index = P1.move()
        while gameboard.play(P1,index,gameboard.getValue(0,index))==-1: # while player 1 is going
            print(gameboard)
            index = P1.move()
        if(gameboard.isWinner()== True): # if there i a winner
            gameboard.addRemaining()
            print(gameboard.findWinner())
            break
        print("Player 2")
        print(gameboard)
        print("Player 2")
        index = P2.move()
        while gameboard.play(P2,index,gameboard.getValue(1,index))==-1: # while it is player 2s turn
            print(gameboard)
            index = P2.move()
        if (gameboard.isWinner() == True): # if there is a winner
            gameboard.addRemaining()
            print(gameboard.findWinner())
            break


Game(player1, player2)

