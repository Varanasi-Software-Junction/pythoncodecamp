from random import randint

player1 = input("Enter name of player 1\n")
player2 = input("Enter name of player 2\n")
score1 = 0
score2 = 0
currentplayer = 1
while True:
    print("Player 1 : ", score1, ", Player 2 : ", score2)
    if currentplayer == 1:
        currentname = player1
    else:
        currentname = player2
    n = randint(1, 8)
    noofmoves = 0

    while True:
        option = int(input(currentname + " pick a number\n"))
        if option == n:
            points = (3 - noofmoves) * 100
            print(currentname, "gets ", points)
            if currentplayer == 1:
                score1 += points

            else:
                score2 += points
            currentplayer = 3 - currentplayer
            break
        elif option < n:
            print("More")
        else:
            print("Less")
        noofmoves += 1
        if noofmoves > 2:
            print("Chances over")
            currentplayer = 3 - currentplayer
            break
