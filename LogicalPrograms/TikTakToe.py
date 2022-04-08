'''
@Author: Nikita
@Date: 2022-04-07 23: 53: 00
@Last Modified by:Nikita
@Last Modified time: 2022-04-07 23: 53: 00
@Title: Gambler
'''

board={
    'T1':' ','T2':' ', 'T3': ' ',
    'I1':' ','I2':' ' ,'I3':' ',
    'K1':' ','K2':' ','K3':' '
}

player=1
total_moves=0   #it is not more than 9
end_chake=0

def check():           #check the moves of player one
    """
        Description:
            Function to Check all possible condition of wining 
        Parameter:
            No parameter
        Return:   
            returning one if codition of wining satisfy and which player won
    """	
    #for horizontal
    if board['T1']== 'X' and board['T2']== 'X' and board['T3']== 'X':
            print("player one won")
            return 1
    if board['I1']== 'X' and board['I2']== 'X' and board['I3']== 'X':
            print("player one won")
            return 1
    if board['I1']== 'X' and board['I2']== 'X' and board['I3']== 'X':
            print("player one won")
            return 1
    #diagonal
    if board['T1']== 'X' and board['I2']== 'X' and board['K3']== 'X':
        print("player one won")
        return 1

    #vertical
    if board['T1']== 'X' and board['I1']== 'X' and board['K1']== 'X':
        print("player one won")
        return 1
    if board['T2']== 'X' and board['I2']== 'X' and board['I3']== 'X':
        print("player one won")
        return 1
    if board['T3']== 'X' and board['I3']== 'X' and board['K3']== 'X':
        print("player one won")
        return 1 
    
    # MOVES fOR PLAYER TWO
    if board['T1']== 'X' and board['T2']== 'X' and board['T3']== 'X':
            print("player one won")
            return 1
    if board['I1']== 'X' and board['I2']== 'X' and board['I3']== 'X':
            print("player one won")
            return 1
    if board['I1']== 'X' and board['I2']== 'X' and board['I3']== 'X':
            print("player one won")
            return 1
    #diagonal
    if board['T1']== 'X' and board['I2']== 'X' and board['K3']== 'X':
        print("player one won")
        return 1

    #vertical
    if board['T1']== 'X' and board['I1']== 'X' and board['K1']== 'X':
        print("player one won")
        return 1
    if board['T2']== 'X' and board['I2']== 'X' and board['I3']== 'X':
        print("player one won")
        return 1
    if board['T3']== 'X' and board['I3']== 'X' and board['K3']== 'X':
        print("player one won")
        return 1 
    
    return 0                #if check fails


print('T1|T2|T3')   #simple tak board
print('- +- +-')
print('I1|I2|I3')   
print('- +- +-')
print('K1|K2|k3')   
print('- +- +-')
print("****************************")

while True:
    print(board['T1']+'|'+board['T2']+'|'+board['T3'])
    print('-+-+-')
    print(board['I1']+'|'+board['I2']+'|'+board['I3'])
    print('-+-+-')
    print(board['K1']+'|'+board['K2']+'|'+board['K3'])
    end_chake = check()
    if total_moves==9 or end_chake==1:
        break
    
    while True:     #Input From Players
        if player == 1: 
            p1=input("Player one   ")                    #choose player 1
            if p1 in board and  board[p1] == ' ': #to check valid key and white space only
                board[p1] = 'X'
                player=2
                break
            else:
                print("invalid input,plz try again")
                continue
            
        else:  #player 2
            
            p2=input("Player two")
            if p2 in board and board[p2] == ' ':
                board[p2] = 'O'
                player=1
                break
            else:
                print("invalid input,plz try again")
                continue   
    total_moves+=1
    print("******************************")
    print()