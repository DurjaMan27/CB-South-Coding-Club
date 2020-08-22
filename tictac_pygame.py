import pygame
from pygame import gfxdraw
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
blue = (3, 206, 252)
green = (0, 255, 0)
red = (255, 0, 0)


display = pygame.display.set_mode((500, 550))  # set display size
pygame.display.set_caption("Tic Tac Toe")


def message_display(text, color, x=80, y=525, size=32):
    font = pygame.font.Font('freesansbold.ttf', size)  # set font
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = int(x), int(y)
    display.blit(text_surface, text_rect)

def game_loop():
    display.fill(white)  # set display color
    first = pygame.draw.rect(display, blue, (0, 0, 160, 160)) # draws rectangles for buttons
    second = pygame.draw.rect(display, blue, (170, 0, 160, 160))
    third = pygame.draw.rect(display, blue, (340, 0, 160, 160))
    fourth = pygame.draw.rect(display, blue, (0, 170, 160, 160))
    fifth = pygame.draw.rect(display, blue, (170, 170, 160, 160))
    sixth = pygame.draw.rect(display, blue, (340, 170, 160, 160))
    seventh = pygame.draw.rect(display, blue, (0, 340, 160, 160))
    eighth = pygame.draw.rect(display, blue, (170, 340, 160, 160))
    ninth = pygame.draw.rect(display, blue, (340, 340, 160, 160))

    pygame.draw.rect(display, blue, (0, 0, 500, 15))  # draws borders
    pygame.draw.rect(display, blue, (0, 0, 15, 500))
    pygame.draw.rect(display, blue, (0, 485, 500, 15))
    pygame.draw.rect(display, blue, (485, 0, 15, 500))

    rectangles = [[first, second, third],  # list of rectangles
                  [fourth, fifth, sixth],
                  [seventh, eighth, ninth]]

    board = [[' ', ' ', ' '],  # list to hold game board
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

    # anti aliased circle function
    def draw_circle(surface, x, y, radius, color):
        gfxdraw.aacircle(surface, x, y, radius, color)
        gfxdraw.filled_circle(surface, x, y, radius, color)

    """def draw_marker(letter, rect):  # draws player markers
        if letter == "O":
            pygame.draw.circle(display, white, (80 + rect.x, 80 + rect.y), 60)
            pygame.draw.circle(display, blue, (80 + rect.x, 80 + rect.y), 40)
        elif letter == "X":
            pygame.draw.rect(display, white, (30 + rect.x, 30 + rect.y, 100, 100))"""

    def draw_marker2(letter, rect):
        if letter == 'O':
            draw_circle(display, 80 + rect.x, 80 + rect.y, 60, white)
            draw_circle(display, 80 + rect.x, 80 + rect.y, 40, blue)
        elif letter == 'X':
            message_display('X', white, x=80 + rect.x, y=90 + rect.y, size=150)

    def draw_board():
        for rect_row, board_row in zip(rectangles, board):
            for rect, marker in zip(rect_row, board_row):  # zips board positions to respective rectangles
                if marker == 'X':  # references board list to update game display
                    draw_marker2("X", rect)
                elif marker == 'O':
                    draw_marker2("O", rect)

    def get_move(mouse_pos):  # determines which rectangle was clicked
        for i, rect_row in enumerate(rectangles):
            for j, rect in enumerate(rect_row):
                if rect.collidepoint(mouse_pos):
                    return i, j  # returns indexes of rectangle that was clicked

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

    turn_count = 0
    while True:

        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            try:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if winner() is None:
                        pos = pygame.mouse.get_pos()
                        row, col = get_move(pos)
                        if board[row][col] == ' ':
                            if turn_count % 2 == 0:
                                player = "X"
                            else:
                                player = "O"
                            board[row][col] = player
                            turn_count += 1
                            draw_board()
            except TypeError:
                pass
            if winner() is not None:
                message_display(f"{winner()} wins!", black)
                button("Play again", green, 175, 505, 175, 40, game_loop)
                button("Quit", red, 375, 505, 100, 40, quit_game)
            elif turn_count == 9:
                message_display("Tie!", black)
                button("Play again", green, 175, 505, 175, 40, game_loop)
                button("Quit", red, 375, 505, 100, 40, quit_game)

        pygame.display.update()


def button(message, color, x, y, width, height, func=None):
    pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    pygame.draw.rect(display, color, (x, y, width, height))
    message_display(message, black, x + width/2, y + height/2)

    if x+width > pos[0] > x and y+height > pos[1] > y and click[0] == 1 and func is not None:
        func()

def quit_game():
    pygame.quit()
    quit()

def game_intro():
    while True:

        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill(white)
        message_display("Tic-tac-toe", black, 250, 230, 75)

        button("Play", green, 75, 300, 150, 50, game_loop)
        button("Quit", red, 275, 300, 150, 50, quit_game)

        pygame.display.update()

game_intro()
pygame.quit()
