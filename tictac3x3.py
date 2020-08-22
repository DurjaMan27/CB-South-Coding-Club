board = [[' ', ' ', ' '],  # list to hold game board
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

def print_board():  # prints the board
    print("    1    2    3")
    for count, row in enumerate(board, 1):
        print(count, row)


def winner():  # check for a winner. Only works for 3 x 3 board
    for row in board:  # check horizontals
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    for col in range(3):  # check verticals
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':  # check diagonals
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]


def get_move():  # asks players for input. returns row and column indexes
    space_chosen = False
    while not space_chosen:
        row_choice = int(input("What row do you want to play? (1, 2, 3) ")) - 1
        col_choice = int(input("What column do you want to play? (1, 2, 3) ")) - 1
        if row_choice < 0 or row_choice > 2 or col_choice < 0 or col_choice > 2:  # checks if inputs are in bounds
            print("make sure input is between (1, 2, 3)")
        elif board[row_choice][col_choice] == ' ':  # check if space is empty
            space_chosen = True
        else:
            print("Spot unavailable. Try again!")
    return row_choice, col_choice


def play():
    turn_count = 0  # count of the number of turns that have elapsed in the game
    while winner() is None and turn_count < 9:
        print_board()
        if turn_count % 2 == 0:
            player = "X"
        else:
            player = "O"
        print(f"{player}'s turn")
        row, col = get_move()
        board[row][col] = player
        turn_count += 1
    print_board()
    if winner() is None:
        print("Tie!")
    else:
        print(f"{winner()} wins!")


play()



