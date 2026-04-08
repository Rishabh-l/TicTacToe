#my first game
import random

board = [' ' for x in range(10)]

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
    run=True
    while run:
        pos=input('Please select the position for X (1-9): ')
        try:
            move=int(pos)
            if move>0 and move<10:
                if spaceIsFree(move)==True:
                    run=False
                    insertLetter('X',move)
                else:
                    print("Space is occupied!")
                    print("Try again!")
            else:
                print("Please Enter a valid index between 1-10")
        except:
            print("Invalid!")
            print("Please type a numerical value within the range!")

    

def compMove():
    possibleMoves=[x for x,letters in enumerate (board) if letters==' ' and x!=0]
    for let in ['O','X']:
        for i in possibleMoves:
            boardcopy=board[:]
            boardcopy[i]=let
            if (isWinner(boardcopy,let)):
                move=i
                return move
    cornersopen=[]
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersopen.append(i)
    if len(cornersopen)>0:
        move=selectRandom(cornersopen)
        return move
    if 5 in possibleMoves:
        move=5
        return move
    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        return selectRandom(edgesOpen)
    return 0
                    
def selectRandom(li):
    return random.choice(li)

def isBoardFull(board):
    return board.count(' ')<1

def main():
    print("Yo!!")
    print("Thanks for using our tic tac toe game!")
    print("This game is solely made by Rishabh Patel!")
    printBoard(board)
    while not isBoardFull(board):
        playerMove()
        printBoard(board)
        if isWinner(board, "X"):
            print("Congo! You've Won!")
            return

        if isBoardFull(board):
            break

        move=compMove()
        if move==0:
            print("Tie game!")
            return
        insertLetter("O", move)
        print("I inserted an O at", move, ":")
        printBoard(board)
        if isWinner(board, "O"):
            print("tf you've lost!")
            print("Pathetic!")
            return
    if isBoardFull(board):
        print("Tie Game!")



main()