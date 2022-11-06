#My TicTacToe Game

print('================================')
print("Welcome to your Tic-Tac-Toe game")
print('')

# Invite players to iidentity their self, and their choose a colour in the list 
player_one= input("Player one identify yourself:")
print("Choose a colour in the list (blue)/(black)/(orange)/(white)/(green)/(pink)/(brown)(yellow)(red):")

print('')

# Each player enter his colour
colour =''
player_one_colour = input ('Choose your colour :')  
if player_one_colour == 'blue' or 'black' or 'orange' or 'white' or 'green' or 'pink'or'brown'or'yellow'or'red':
   print(f'As the player one,you choose {player_one_colour} as your colour')

print("..............................................................")
print("")

player_two=input("Player two identify yourself :")
print("Choose a colour in the list (blue)/(black)/(orange)/(white)/(green)/(pink)/(brown)(yellow)(red):")
print('')

colour =''
player_two_colour = input ('Choose your colour :')  
if player_two_colour == 'blue' or 'black' or 'orange' or 'white'or 'green' or 'pink' or 'brown'or 'yellow'or 'red':
   print(f'As the player two,you choose {player_two_colour} as your colour')
     
# Brief  presentation and of each player then, tell them their colour choosen
   print("..............................................................")
print("")
print(f"Great ! {player_one} is the  player one and {player_one} colour is  {player_one_colour},{player_two} is the player two and {player_two} colour is {player_two_colour}")
print('')
print("==============================================================")

print("")
 
# A Small Message to let them know that the game can start now
print("***********************Now you can start**********************")
print("")
print("**************************************************************")


def main():
    player = next_player("")
    board =  create_board()
    while not (has_winner(board) or is_a_draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
# Congratulate player
    display_board(board)
    print("Congratulations!, Thank you for have been trying!")
  
# Create the game board
def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board
# Then display the game board, to let the player see how it look
def display_board(board):
   
    print("==*==")
    print("==*==")
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print('-+-+-')
    print(f"{board[0]}|{board[3]}|{board[6]}")
    print('-+-+-')
    print(f"{board[0]}|{board[3]}|{board[6]}")
    print('-+-+-')
    print(f"{board[0]}|{board[3]}|{board[6]}")
    print("==*==")
    print("==*==")
  
    print()
    
def is_a_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True
 #Define the rule of the to let player compare while playing   
def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[6] == board[3] == board[9])


def make_move(player, board):
    
    
    # Player can see his name while playing
    square = int(input(f"@@@@@@@@ {player_one}'s turn to choose a square (1-9): "))
 
    print("")   
    print("")
    # Player can see his name while playing
    square = int(input(f"¤¤¤¤¤¤¤¤ {player_two}'s turn to choose a square (1-9): "))
    board[square - 1] = player

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":    
         return "o"


# Call the main function to execute the code
if __name__ == "__main__":
    main()