import discord
from discord.ext import commands
import random


#We define the board as an array

board = ["-","-","-",
        "-","-","-",
        "-","-","-",] 

#Global Variables

winner = None

inputValid = False

gameOn = True

computer = None

cpu_turn = True

#User selection

player = str(input("Choose X or 0, type what do you want to play as."))
player = player.upper()

#Input validation

while player != "X" and player != "0":

    print(f"{player} is not a valid character to play Tic Tac Toe, please try again.")
    player = str(input("Choose X or 0, type what do you want to play as."))
    player = player.upper()

    if player == "X" or player == "0":
        print(f"You have chosen to play as {player}.")

#Function that makes the scoreboard a little more appealing 

def showBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

#Function that defines the player/s position/s

def playerPosition(board):

    position = input("Select a position from the board from left to right ranging from 1-9. Type in the number of the position.")
    isNum = position.isnumeric()

    if isNum == True:
        position = int(position)
        print(f"Player {player} has chosen to play position {position}.")

    while isNum == False:
        print(f"{position} is not a valid board number. Please try again.")
        position = input("Select a position from the board from left to right ranging from 1-9. Type in the number of the position.")
        isNum = position.isnumeric()

        if position.isnumeric:
            position = int(position)
            print(f"Player {player} has chosen to play position {position}.")
    isNum = True
    
    if position >= 1 and position <= 9 and board[position - 1] == "-":
            board[position - 1] = player
    else: 
        print(f"AI is already in position {position} of the board. Try another spot. ")

#Function that checks for win by row

def checkRow(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        print("Winner Winner Chicken Dinner!!")
        print("Row 1 is the Winner!")
        return True
    elif board[3] == board[4] == board[5] and board[4] != "-":
        print("Winner Winner Chicken Dinner!!")
        print("Row 2 is the Winner!")
        return True
    elif board[6] == board[7] == board[8] and board[7] != "-":
        print("Winner Winner Chicken Dinner!!")
        print("Row 3 is the Winner!")
        return True
    
#Function that checks for win in columns

def checkColumn(board):
    global winner
    if board[0] == board[3] == board[6] and board[3] != "-":
        print("Winner Winner Chicken Dinner!!")
        print("Column 1 is the Winner!")
        return True
    elif board[1] == board[4] == board[7] and board[4] != "-":
        print("Winner Winner Chicken Dinner!!")
        print("Column 2 is the Winner!")
        return True
    elif board[2] == board[5] == board[8] and board[5] != "-":
        print("Winner Winner Chicken Dinner!!")
        print("Column 3 is the Winner!")
        return True

#Function that checks for win diagonally

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[4] != "-":
        print("Winner Winner Chicken Dinner!!")
        print("Diagonal left is the Winner!")
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        print("Winner Winner Chicken Dinner!!")
        print("Diagonal right is the Winner!")
        return True
    
#Function that checks if there has been a tie

def checkTie(board):
    global gameOn
    if "-" not in board:
        print("ITS A TIE!")
        gameOn = False

#Master Function that wraps up all win conditions in one

def checkWin():
    if checkColumn(board) or checkDiagonal(board) or checkRow(board):
        print(f"Winner is {winner}")
        gameOn = False

#Function that defines what the CPU plays as

def defininePlayers():
    global player
    global computer

    if player == "X":
        computer = "0"
    elif player == "0":
        computer = "X"
    
#Function for random board move for CPU

def computerPosition(board):
    global computer

    cpu_turn = True
    
    cpu_position = random.randint(0,8)

    while gameOn == True:
        if "-" in board[cpu_position]:
            board[cpu_position] = computer
            continue
        else:
            return defininePlayers()
        
#Loop to run game

while gameOn:
    showBoard(board)
    playerPosition(board)
    defininePlayers()
    computerPosition(board)
    checkTie(board)
    checkWin()