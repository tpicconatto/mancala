def Game(P1, P2):
    while (isWinner() == false): #alternate players making a move, if there is a winner after each move exit while loop and find winner
        P1.move()
        play(P1,P1.move(),getValue())
        if(isWinner()==true):
            break
        P2.move()
        play(P2,P2.move(),getValue())
    findWinner()
