import random


def GetR():
    r = random.randint(0,99) + 1
    return r

def JumpBall():
    r = GetR()
    if r <= 50:
        poss = False
    else:
        poss = True
    Possession(userScore, oppScore, poss, num)

def Possession(userScore, oppScore, poss, num):
    r = GetR()
    if r <= 14:
        if poss == True:
            userScore = userScore + 3
            print("Your team scores a three!", "                ", userScore, "-", oppScore)
            poss = not poss
        else:
            oppScore = oppScore + 3
            print("The opponent hits a three!", "               ", userScore, "-", oppScore)
            poss = not poss
    elif r <= 40:
        if poss == True:
            print("Your team misses a three!" , "                ", userScore, "-", oppScore)
            poss = not poss
        else:
            print("The opponent misses a three!" , "             ", userScore, "-", oppScore)
            poss = not poss
    elif r <= 60:
        if poss == True:
            userScore = userScore + 2
            print("Your team scores 2! ", "                     ", userScore, "-", oppScore)
            poss = not poss
        else:
            oppScore = oppScore + 2
            print("The opponent scores 2!", "                   ", userScore, "-", oppScore)
            poss = not poss
    elif r <= 80:
        if poss == True:
            print("Your team misses a 2!", "                    ", userScore, "-", oppScore)
            poss = not poss
        else:
            print("The opponent misses a 2!", "                 ", userScore, "-", oppScore)
            poss = not poss
    elif r <= 90:
        if poss == True:
            print("Your team turns the ball over.", "           ", userScore, "-", oppScore)
            poss = not poss
        else:
            print("The opponent turns the ball over.", "        ", userScore, "-", oppScore)
            poss = not poss
    else:
        r2 = random.randint(1,2)
        if poss == True:
            userScore = userScore + r2
            print("Your team is fouled and makes", r2, " FT", "      ", userScore, "-", oppScore)
            poss = not poss
        else:
            oppScore = oppScore + r2
            print("opponent is fouled and makes", r2, " FT", "       ", userScore, "-", oppScore)
            poss = not poss
    num = num - 1
    if num > 0:
        Possession(userScore, oppScore, poss, num)
    else:
        FinishGame(userScore, oppScore, poss, num)

def FinishGame(userScore, oppScore, poss, num):
    if userScore > oppScore:
        print("You won: ", userScore, "-", oppScore)
    elif oppScore > userScore:
        print("You lost: ", userScore, "-", oppScore)
    else:
        print("THIS GAME IS HEADED TO OVERTIME!!!")
        num = num + 15
        Possession(userScore, oppScore, poss, num)

num = random.randint(140,160)           
userScore = 0
oppScore = 0
poss = True
JumpBall()


