# Aira Carvalho       -       January, 2016
# Rock, Paper and Scissors
import random

playerScore = 0
cpuScore = 0

def displayIntro():
    
    print "Welcome to Rock, Paper, Scissors."
    print "Do you think you can beat me? Let's see about that."

def playerChoose():
    
    playerMove = " "
    
    while playerMove != "rock" and playerMove != "paper" and playerMove != "scissors" and playerMove != "exit":
        playerMove = raw_input("What's your move, Player (rock, paper or scissors)? Or type 'exit' to stop playing. ")
    return playerMove

def cpuChoose():
    
    cpuMove = " "
    
    cpuRand = random.randint(1,3)
    
    while cpuMove != "rock" and cpuMove != "paper" and cpuMove != "scissors":
        if cpuRand == 1:
            cpuMove = "rock"
            return cpuMove
        elif cpuRand == 2:
            cpuMove = "paper"
            return cpuMove
        else:
            cpuMove = "scissors"
            return cpuMove

def checkWinner(player, cpu):
    
    if player == "rock" and cpu == "paper":
        return "cpu"
        
    elif player == "rock" and cpu == "scissors":
        return "player"
        
    elif player == "scissors" and cpu == "paper":
        return "player"
        
    elif player == "scissors" and cpu == "rock":
        return "cpu"
        
    elif player == "paper" and cpu == "rock":
        return "player"
        
    elif player == "paper" and cpu == "scissors":
        return "cpu"
        
    else:
        return "draw"

def totalScore():
    print "The total score is:\nPlayer Score: %s \nCPU Score: %s" % (playerScore, cpuScore)

displayIntro()

playAgain = "yes"
while playAgain == "yes" or playAgain == "y":

    playerRound = playerChoose()
    if playerRound == "exit":
        break
    
    cpuRound = cpuChoose()
    
    winner = checkWinner(playerRound, cpuRound)
    
    if winner == "player":
        print "Congratulations, you've won this round! Your move was '%s' and mine was '%s'." % (playerRound, cpuRound)
        playerScore += 1
    elif winner == "cpu":
        print "In you face! I've won this round! Your move was '%s' and mine was '%s'." % (playerRound, cpuRound)
        cpuScore += 1
    else:
        print "Well, that's a draw. Your move was '%s' and mine was '%s'." % (playerRound, cpuRound)

    totalScore()
