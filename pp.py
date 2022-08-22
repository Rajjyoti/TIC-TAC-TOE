
# coding: utf-8

# In[ ]:



import random
def display_board(board): #function that can print out a board.
    print('\n'*100)
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])
   
    
def player_input():  # function that can take in a player input and assign their marker as 'X' or 'O'.
    marker=''
    while not marker=='X' or marker=='O':
        marker=(input('Player 1, enter marker: X or O ').upper())
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')
    

def place_marker(board,marker,position):   #function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
    board[position]=marker
    
def space_check(board,position):    #function that returns a boolean indicating whether a space on the board is freely available.
    return board[position]==' '
    
def posi(board):   #function that asks for a player 1's next position.
    position=0
    while position not in range(1,10) or not space_check(board,position):
        position=int(input('Player 1 choose position: (1-9) '))
    return position

def posi2(board):   #function that asks for a player 2's next position.
    position=0
    while position not in range(1,10) or not space_check(board,position):
        position=int(input('Player 2 choose position: (1-9) '))
    return position

def full_check(board):   #checks if the board is full.
    for i in range(1,10):
        if space_check(board,i):
            return False
    else:
        return True
    
def decide():  #randomly decides who takes the first play.
    if random.randint(0,1)==0:
        return 'Player 1'
    else:
        return 'Player 2'
    
def win_check(board,mark):   #checks for win conditions.
     return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
    
def ask():  #asks if they want to play again.
    choice=input('Play again? Yes or No: ')
    return choice=='Yes'



while True:
    board=[' ']*10
    player1,player2=player_input()
    turn=decide()
    print(turn + ' will go first')
    
    play=input('Ready? y or n ')
    if play.lower()=='y':
        game_on=True
    else:
        game_on=False
        
    while game_on:
        if turn== 'Player 1':  #if player 1 gets the first chance.
            display_board(board)
            position=posi(board)
            place_marker(board,player1,position)
            
            if win_check(board,player1):
                print('Player 1 won.')
                game_on=False
            elif full_check(board):
                print('Tie')
                break
            else:
                turn='Player 2'
        
        else:   #if player 2 gets first chance
            display_board(board)
            position=posi2(board)
            place_marker(board,player2,position)
            
            if win_check(board,player2):
                print('Player 2 won.')
                game_on=False
            elif full_check(board):
                print('Tie')
                break
            else:
                turn='Player 1'
                
    if not ask():  #if player doesnt want to play again.
        print('BYE!')
        break
            
            
            
    
    
    
    
        
    

