# Game Name:			Rock, Paper and Scissors
# Created by:			Aira Carvalho da Silva
# Date:				01/26/2016
# Python Version:		Python 2.x

''' The rules are simple: You have to choose between three options: "Rock, Paper or Scissors".
The computer will also choose one. Rocks beats Scissors, Paper beats Rock and Scissors beats Paper.'''

# Imports all modules needed to this script.
import random
import sys

# Keeps track of score.
playerScore = 0
cpuScore = 0

# Global lists of Possibilities
possible_moves = ["rock", "paper", "scissors", "quit"]

# Asks for the Player's name.
playerName = raw_input("Hello, what's your name? ")

# This function asks the player to Choose what he wants to play.
def playerMove():

	playerChoose = " "
	
	while playerChoose not in possible_moves:
		playerChoose = raw_input("\nDo you want to play 'Rock', 'Paper' or 'Scissors' (Or type 'Quit' to exit)? ").lower()
	return playerChoose

# This function chooses what the CPU is going to play next.
def cpuMove():

	cpuChoose = possible_moves[(random.randint(0,2))]
	return cpuChoose	

# This function checks who's the Winner.
def checkWinner(player, cpu):
	player_wins = "player_wins"
	cpu_wins = "cpu_wins"
	draw = "draw"
	
	if player == "rock" and cpu == "scissors":
		return player_wins
		
	elif player == "paper" and cpu == "rock":
		return player_wins
		
	elif player == "scissors" and cpu == "paper":
		return player_wins
		
	elif player == "rock" and cpu == "paper":
		return cpu_wins
		
	elif player == "paper" and cpu == "scissors":
		return cpu_wins
		
	elif player == "scissors" and cpu == "rock":
		return cpu_wins
		
	else:
		return draw

# Winning Function
def playerWins():
	
	global playerScore

	playerScore += 1
	print "\nCongratulations '%s', you've WON this round." % (playerName)

# Loosing Function
def playerLooses():
	
	global cpuScore

	cpuScore += 1
	print "\nI'm sorry '%s', but you've LOST this round." % (playerName)

# Main Loop for the Script. Calls all the functions.
playAgain = True
while playAgain == True:
	
	player_move = playerMove()
	if player_move == "quit":
		sys.exit()
	
	cpu_move = cpuMove()
	
	final_result = checkWinner(player_move, cpu_move)
	
	if final_result == "player_wins":
		playerWins()
	
	elif final_result == "cpu_wins":
		playerLooses()
		
	else:
		print "Well, that was a DRAW."
	
	print " "
	print "You've played '%s' and the CPU played '%s'. \n" % (player_move, cpu_move)
	print "The total score is: \nPlayer Score: %s \nCPU Score: %s" % (playerScore, cpuScore)
	print " "
