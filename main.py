gameBoard = []

def createGameBoard():
    for i in range(0,9):
        gameBoard.append([0,0,0,0,0,0,0,0,0])

def printBoard():
    for i in gameBoard:
        print(i)

def main():
    createGameBoard()
    printBoard()

if __name__ == '__main__':
    main()
