import math

board = [' ' for x in range(10)]
board[0]='Non valid'


def printBoard(board):
    print(' ' + board[1] + '  | ' + board[2] + ' | ' + board[3])
    print('------------')
    print(' ' + board[4] + '  | ' + board[5] + ' | ' + board[6])
    print('------------')
    print(' ' + board[7] + '  | ' + board[8] + ' | ' + board[9])


def IsWinner(board,symbol):
    return (board[1]== symbol and board[2]==symbol and board[3]==symbol) or (board[4]== symbol and board[5]==symbol and board[6]==symbol) or (board[7]== symbol and board[8]==symbol and board[9]==symbol) or (board[1]== symbol and board[4]==symbol and board[7]==symbol) or (board[3]== symbol and board[6]==symbol and board[9]==symbol) or (board[2]== symbol and board[5]==symbol and board[8]==symbol) or (board[1]== symbol and board[5]==symbol and board[9]==symbol) or (board[3]== symbol and board[5]==symbol and board[7]==symbol)


def spaceIsFree(pos):
    return board[pos]==' '


def insertLetter(letter,pos):
    board[pos]=letter


def empty_squares(board):
    return ' ' in board


# calucalting the no of squares which has yet to be fiilled
def num_empty_square(board):
    return board.count(' ')


# caluclating no of avaialable moves
def available_moves(bord):
    return [i for i,x in enumerate(bord) if x==' ']


# Taking human player move as input
def playerMove(symbol):
    run = True
    while run:
        move = input("please select a position to enter the {sym} between 1 to 9 => ".format(sym=symbol))
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter(symbol , move)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('please type a number between 1 and 9')
        except:
            print('Please type a number')


# implemented the MaxMin algoritham
def getOptimumMove(board, playerTurn):
    other_player = 'O' if playerTurn == 'X' else 'X'

    if IsWinner(board,other_player):
        return {'position': None, 'score': 1 * (num_empty_square(board)) if other_player == 'X' else -1 * (num_empty_square(board))}
    elif not empty_squares(board):
        return {'position': None, 'score': 0}    

    if playerTurn == 'X':
        best = {'position': None, 'score': -math.inf}
    else:
        best = {'position': None, 'score': math.inf}

    for possible_move in available_moves(board):
        if possible_move != 0:
            board[possible_move] = playerTurn
            curr_score = getOptimumMove(board, other_player)

            board[possible_move] = ' '
            curr_score['position'] = possible_move

            if playerTurn == 'X':
                if curr_score['score'] > best['score']:
                    best = curr_score
            else:
                if curr_score['score'] < best['score']:
                    best = curr_score

    return best

def gamePlay():
    # print("Enter your Player Name:")
    PlayerName=input("Enter your Player Name => ")
    PreviousTurn='N'
    PlayerTurn='O'
    print('Your Player Name is =>',PlayerName)
    print('Bot name is => Chitti')
    print('First turn is yours')
    printBoard(board)
    while(num_empty_square(board)!=0):
        if PlayerTurn=='O':
            playerMove('O')
            PreviousTurn='O'
            PlayerTurn='X'
        else:
            positionObj=getOptimumMove(board,'X')
            board[positionObj['position']]='X'
            PreviousTurn='X'
            PlayerTurn='O'
        printBoard(board)
        if(PreviousTurn!='N' and IsWinner(board,'X')):
            break
        elif (PreviousTurn!='N' and IsWinner(board,'O')):
            break
        elif (PreviousTurn!='N' and num_empty_square(board)==0):
            break
    
    if(PreviousTurn!='N' and IsWinner(board,'X')):
        print('Chitti won the game')
    elif (PreviousTurn!='N' and IsWinner(board,'O')):
        print(PlayerName,' won the game')
    elif (PreviousTurn!='N' and num_empty_square(board)==0):
        print("Match was a draw well played")

    
gamePlay()