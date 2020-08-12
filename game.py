#function to display  Game board
from IPython.display import clear_output

def display_board(board):
    clear_output()
    print('  |   |')
    print(' '+board[7]+'  '+board[8]+'  '+board[9])
    print('  |   |')
    print('-----------')
    print('  |   |')
    print(' '+board[4]+'  '+board[5]+'  '+board[6])
    print('  |   |')
    print('-----------')
    print('  |   |')
    print(' '+board[1]+'  '+board[2]+'  '+board[3])
    print('  |   |')
    print('-----------')
# function to choose player to play first  
def player_input():
    marker=''
    while marker!='X'and marker!='O':
        marker=input('player1:choose X or O').upper()
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')
#placing player marker in specified position
def place_marker(board,marker,position):
    board[position]=marker
#function will called everytime to check win
def win_check(board,mark):
   return(( board[1]==board[2]==board[3]==mark)or( board[4]==board[5]==board[6]==mark)or( board[7]==board[8]==board[9]==mark)or( board[7]==board[4]==board[1]==mark)or( board[2]==board[5]==board[8]==mark)or( board[3]==board[6]==board[9]==mark)or( board[1]==board[5]==board[9]==mark)or( board[3]==board[5]==board[7]==mark))


#function to choose player to play randomly at first time
import random
def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return 'player1'
    else:
        return 'player2'

#function to check is input place available
def space_check(board,position):
    return board[position] ==' '

#function to check for tie condition
def full_board_check(board):
    for i in range(1,10):
        if(space_check(board,i)):
            return False
    return True
#input choice function
def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('choose a position:(1:9)'))
        
    return position
# function to play game again
def replay():
    choice=input('play again? enter yes or no')
    return choice=='yes'


#main code area
print('welcome to Tic Tac Toe')
while True:
    the_board=[' ']*10
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn+'will go first')
    play_game=input('ready to play!Y or N?')
    if play_game=='Y':
        game_on=True
    else:
        game_on=False
    while game_on:
        if turn=='player1':
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player1_marker,position)
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('player 1 has won!')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE')
                    game_on=False
                else:
                    turn='player2'
        else:    
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player2_marker,position)
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('player 2 has won!')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE')
                    game_on=False
                else:
                    turn='player1'
    if not replay():
        break
        
            
           
            