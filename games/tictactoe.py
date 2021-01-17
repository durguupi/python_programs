theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M':
            ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}


def intialBoard():
    # print('------+---------+--------')
    print('top-L' + ' | ' + 'top-M' + ' | ' + 'top-R')
    print('------+---------+--------')
    print('mid-L' + ' | ' + 'mid-M' + ' | ' + 'mid-R')
    print('------+---------+--------')
    print('low-L' + ' | ' + 'low-M' + ' | ' + 'low-R')
    # print('------+---------+--------')
    print()


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


intialBoard()
printBoard(theBoard)
user_input = input("Enter the value: ")
theBoard[user_input] = "X"
printBoard(theBoard)
