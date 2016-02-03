# Game Name:		Rock, Paper and Scissors
# Creator:			Aira Carvalho
# Date:				  02/03/2016
# PyVersion:		2.x

''' New version of my Rock, Paper and Scissors. This time I've tried to implement 'classes' which is a new subject to me. I'm happy with the results. Enjoy! '''

# Imports all Modules.
import random
import sys

# Creating and Keeping Scores.
playerScore = 0
cpuScore = 0

# Global list of possibilities.
possible_moves = ["rock", "paper", "scissors", "quit"]

# Main Intro.
def intro():

	print "Welcome to 'Rock', 'Paper' and 'Scissors'. \n\nThe Rules are simple: Choose what you want to play and see if you can beat the CPU."

	player_name = raw_input("\nFirst, tell me what's your name. ")

	return player_name

# Asks what is player's move.
def playerMove():

	player_move = " "

	while player_move not in possible_moves:

		player_move = raw_input("\nAre you playing Rock, Paper or Scissors? Or 'Quit' to exit. ").lower()

	return player_move

# Generates CPU's move.
def cpuMove():

	cpu_move = possible_moves[random.randint(0,len(possible_moves)-2)]
	return cpu_move

# Checks who's the winner.
class checkWinner(object):

	def __init__(self, player, cpu):
		self.player = player
		self.cpu = cpu
		
	# Checks if player's the winner.
	def playerWins(self):

		if self.player == "rock" and self.cpu == "scissors":
			return True

		elif self.player == "paper" and self.cpu == "rock":
			return True

		elif self.player == "scissors" and self.cpu == "paper":
			return True

		else:
			return False

	# Check if player's the looser.
	def playerLooses(self):

		if self.player == "rock" and self.cpu == "paper":
			return True

		elif self.player == "paper" and self.cpu == "scissors":
			return True

		elif self.player == "scissors" and self.cpu == "rock":
			return True

		else:
			return False

# Player is the Winner.
def isWinner():

	global playerScore

	print "\nCongratulations %s, you've WON this round." % (player_name)

	playerScore += 1

# Player is the Looser.
def isLooser():

	global cpuScore

	print "\nSorry %s, but you've LOST this round." % (player_name)

	cpuScore += 1

# It's a draw.
def isDraw():

	print "\nWell, that was a DRAW."

# Prints the Actual Score and last move.
def score():

	print "\nTotal Score: \nPlayer Score: %s \nCPU Score: %s" % (playerScore, cpuScore)

# Calls Intro function.
player_name = intro()

# Main game loop.
playAgain = True
while playAgain is True:

	player_turn = playerMove()
	if player_turn == "quit":
		sys.exit()

	cpu_turn = cpuMove()

	check_player = checkWinner(player_turn, cpu_turn)

	player_wins = check_player.playerWins()
	player_looses = check_player.playerLooses()

	if player_wins == True:
		isWinner()

	elif player_looses == True:
		isLooser()

	else:
		isDraw()

	print "You've played '%s' and the CPU played '%s'." % (player_turn, cpu_turn)
	score()
