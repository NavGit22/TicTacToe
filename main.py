import random

# TicTacToe Text Based Game
print("Welcome to TICTACTOE Game")

user_values = ['0','1','2','3','4','5','6','7','8']
player_x_won = ['X','X','X']
player_o_won = ['O','O','O']


def print_board():
    print('\n')
    print(f'{user_values[0]} | {user_values[1]} | {user_values[2]}')
    print('----------')
    print(f'{user_values[3]} | {user_values[4]} | {user_values[5]}')
    print('----------')
    print(f'{user_values[6]} | {user_values[7]} | {user_values[8]}')
    print('\n')


def check_game_status():
    check_board = {
        1: [user_values[0], user_values[1], user_values[2]],
        2: [user_values[3], user_values[4], user_values[5]],
        3: [user_values[6], user_values[7], user_values[8]],
        4: [user_values[0], user_values[3], user_values[6]],
        5: [user_values[1], user_values[4], user_values[7]],
        6: [user_values[2], user_values[5], user_values[8]],
        7: [user_values[0], user_values[4], user_values[8]]
    }
    for key, val in check_board.items():
        if val == player_x_won:
            print("Player X won the Game")
            return True
        elif val == player_o_won:
            print("Player O won the Game")
            return True
    return False


def check_already_populated(position):
    if user_values[position] == 'X' or user_values[position] == 'O':
        return True
    else:
        return False


def player_1():
    valid = False
    while not valid:
        value = int(input(f"Player X. Please enter the position from 0 to 8 for marking: "))
        if value < 9:
            if not check_already_populated(value):
                user_values[value] = 'X'
                print_board()
                valid = True


def player_2():
    valid = False
    while not valid:
        value = int(input(f"Player O. Please enter the position from 0 to 8 for marking: "))
        if value < 9:
            if not check_already_populated(value):
                user_values[value] = 'O'
                print_board()
                valid = True


def computer():
    valid = False
    while not valid:
        value = random.randint(0, 8)
        if not check_already_populated(value):
            user_values[value] = 'O'
            print_board()
            valid = True


end_game = False
player_2_enable = input("Do you have player 2 (Y) or Wanna play against Computer (N)?").upper()

print_board()


while not end_game:
    player_1()
    if check_game_status():
        end_game = True

    if not end_game and player_2_enable == 'Y':
        player_2()
        if check_game_status():
            end_game = True
    elif not end_game and player_2_enable == 'N':
        computer()
        if check_game_status():
            end_game = True



