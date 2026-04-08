#my first game
import random

board = [' ' for x in range(10)]
scores = {"X": 0, "O": 0, "Ties": 0}

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def printScoreboard():
    print("\n===== SCOREBOARD =====")
    print(f"  You (X): {scores['X']}")
    print(f"  Computer (O): {scores['O']}")
    print(f"  Ties: {scores['Ties']}")
    print("======================\n")

def isWinner(bo, le):
    return (
    (bo[7]==le and bo[8]==le and bo[9]==le) or
    (bo[4]==le and bo[5]==le and bo[6]==le) or
    (bo[1]==le and bo[2]==le and bo[3]==le) or
    (bo[1]==le and bo[4]==le and bo[7]==le) or
    (bo[2]==le and bo[5]==le and bo[8]==le) or
    (bo[3]==le and bo[6]==le and bo[9]==le) or
    (bo[1]==le and bo[5]==le and bo[9]==le) or
    (bo[3]==le and bo[5]==le and bo[7]==le)
    )

def playerMove():
    run = True
    while run:
        pos = input('Please select the position for X (1-9): ')
        try:
            move = int(pos)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print("Space is occupied!")
                    print("Try again!")
            else:
                print("Please Enter a valid index between 1-9")
        except:
            print("Invalid!")
            print("Please type a numerical value within the range!")

def compMove():
    possibleMoves = [x for x, letters in enumerate(board) if letters == ' ' and x != 0]
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if isWinner(boardcopy, let):
                return i
    cornersopen = [i for i in possibleMoves if i in [1, 3, 7, 9]]
    if len(cornersopen) > 0:
        return selectRandom(cornersopen)
    if 5 in possibleMoves:
        return 5
    edgesOpen = [i for i in possibleMoves if i in [2, 4, 6, 8]]
    if len(edgesOpen) > 0:
        return selectRandom(edgesOpen)
    return 0

def selectRandom(li):
    return random.choice(li)

def isBoardFull(board):
    return board.count(' ') <= 1

def resetBoard():
    for i in range(len(board)):
        board[i] = ' '

def playAgain():
    choice = input("Do you want to play again? (y/n): ").lower()
    return choice == 'y'

def main():
    print("Yo!!")
    print("Thanks for using our tic tac toe game!")
    print("This game is solely made by Rishabh Patel!")

    playing = True
    while playing:
        resetBoard()
        printBoard(board)

        while not isBoardFull(board):
            playerMove()
            printBoard(board)
            if isWinner(board, "X"):
                print("Congo! You've Won!")
                scores["X"] += 1
                break

            if isBoardFull(board):
                break

            move = compMove()
            if move == 0:
                print("Tie game!")
                scores["Ties"] += 1
                break
            insertLetter("O", move)
            print("I inserted an O at", move, ":")
            printBoard(board)
            if isWinner(board, "O"):
                print("tf you've lost!")
                print("Pathetic!")
                scores["O"] += 1
                break
        else:
            print("Tie Game!")
            scores["Ties"] += 1

        printScoreboard()

        if not playAgain():
            print("\nFinal Scores:")
            printScoreboard()
            print("Thanks for playing! See ya!")
            playing = False

main()