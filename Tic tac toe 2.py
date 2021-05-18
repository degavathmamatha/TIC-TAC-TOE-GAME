import random
print("\n************** TIC TAC TOE GAME HUMAN v/s COMPUTER ***************")
print("\n                                         WELCOME TO GAME 'TIC TAC TOE' GAME ")
player1_name=input("Input your name: ")
print("\U0001F590",player1_name,"you are the first player and \U0001F4BB computer is second player.")
def dict1():
    global board
    board={
        '1':' ','2':' ','3':' ',
        '4':' ','5':' ','6':' ',
        '7':' ','8':' ','9':' ',
    }
def check(): 
    #### this condition for if user or human is winner#####
    if board['1']=='X' and board['2']=='X' and board['3']=='X'or board['4']=='X' and board['5']=='X' and board['6']=='X' or board['7']=='X' and board['8']=='X' and board['9']=='X' or board['1']=='X' and board['4']=='X' and board['7']=='X' or board['2']=='X' and board['5']=='X' and board['8']=='X' or board['3']=='X' and board['6']=='X' and board['9']=='X' or board['3']=='X' and board['5']=='X' and board['7']=='X' or board['1']=='X' and board['5']=='X' and board['9']=='X':
        print(player1_name,'you win game!!')
        return 1
    #### this condition for if computer is winner#####
    elif board['1']=='O' and board['2']=='O' and board['3']=='O' or board['4']=='O' and board['5']=='O' and board['6']=='O' or board['7']=='O' and board['8']=='O' and board['9']=='O' or board['1']=='O' and board['4']=='O' and board['7']=='O' or board['2']=='O' and board['5']=='O' and board['8']=='O' or board['3']=='O' and board['6']=='O' and board['9']=='O' or board['3']=='O' and board['5']=='O' and board['7']=='O' or board['1']=='O' and board['5']=='O' and board['9']=='O':
        print('\U0001F4BB win the game')
        return 2
    else:
        return 0

def play_game():
    dict1()
    total_moves=0
    player=1
    print("These are position which you have to choose")
    print("1"," |", "2 |","3")
    print("---+---+----")
    print("4"," |", "5 |","6")
    print("---+---+----")
    print("7"," |", "8 |","9\n")
    print("\U0001F600LETS PLAY THE GAME",player1_name,'TIC TAC TOE\U0001F600\n')

    while True:
        print("\n")
        print(board['1']+'   |'+board['2']+'   |'+board['3'])
        print("----+----+----")
        print(board['4']+'   |'+board['5']+'   |'+board['6'])
        print("----+----+----")
        print(board['7']+'   |'+board['8']+'   |'+board['9'],"\n")

        end_check=check()#####for check winner condition
        if end_check==1:
            print("Congrats",player1_name,"you are  winner!!!\U0001F600\U0001F600")
            break
        elif end_check==2:
            print("\U0001F600\U0001F600  win,and you lose the game!!!")
            break
        if total_moves==9:
            print("game draw")
            break
        while True:
            if player==1:######chance for user
                print(player1_name,"your mark is 'X' so input your position")
                p1_input=input("your mark position is: ")
                if p1_input in board and board[p1_input]==' ':
                    board[p1_input]='X'
                    player="computer"
                    break
                else:
                    print('This position already chose by computer\nPlease try another position')
                    continue
            else:
                if player=="computer":####chance for computer
                    p2_input=str(random.randint(1,9))
                    print("\U0001F4BB mark 'O' position is",p2_input)
                    if (p2_input) in board and board[p2_input]==' ':
                        board[p2_input]='O'
                        player=1
                        break
                    else:
                        print('This position already chose by human')
                        continue
        total_moves+=1
    print()
play_game()
def again_play():#### if you want to play again
    user=input("you want to play again\ny or n: ")

    if user=="y":
        play_game()
        again_play()
    elif user=="n":
        print("exit\U0001F917")
again_play()