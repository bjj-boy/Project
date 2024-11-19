import pygame
import random
import sys
pygame.init()
# Настройка размеров окна и шрифта
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 200
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55
MOUSE_FONT = pygame.font.SysFont('comicsans', 40)
# Цвета
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 23, 23)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)
board = [[None]*BOARD_COLS for _ in range(BOARD_ROWS)]
def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE*2), (WIDTH, SQUARE_SIZE*2), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE*2, 0), (SQUARE_SIZE*2, HEIGHT), LINE_WIDTH)
def draw_circle(pos, color):
    pygame.draw.circle(screen, color, pos, CIRCLE_RADIUS, CIRCLE_WIDTH)
def draw_cross(pos, color):
    start = (pos[0]-SPACE, pos[1]-SPACE)
    end = (pos[0]+SPACE, pos[1]+SPACE)
    pygame.draw.line(screen, color, start, end, CROSS_WIDTH)
    pygame.draw.line(screen, color, (pos[0]-SPACE, pos[1]+SPACE), (pos[0]+SPACE, pos[1]-SPACE), CROSS_WIDTH)
def check_win(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]%3][condition[0]//3] == board[condition[1]%3][condition[1]//3] == board[condition[2]%3][condition[2]//3] == player:
            return True
    return False
def draw_board():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                draw_cross((col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), CROSS_COLOR)
            elif board[row][col] == 'O':
                draw_circle((col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), CIRCLE_COLOR)
def main():
    global board;
    clock = pygame.time.Clock()
    player_turn = True
    ai_turn = False
    draw_board()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not check_win('X') and not check_win('O'):
                mouseX, mouseY = event.pos
                clicked_row = min(int(mouseY / SQUARE_SIZE),2)
                clicked_col = min(int(mouseX / SQUARE_SIZE),2)
                if board[clicked_row][clicked_col] is None:
                    board[clicked_row][clicked_col] = 'X'
                    player_turn = False
                    ai_turn = True
                    draw_board()
                    pygame.display.update()
                    pygame.time.wait(100)
                    draw_cross((clicked_col * SQUARE_SIZE + SQUARE_SIZE // 2, clicked_row * SQUARE_SIZE + SQUARE_SIZE // 2), CROSS_COLOR)
                    pygame.display.update()
                    pygame.time.wait(100)
                    board[clicked_row][clicked_col] = 'X'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    board = [[None]*BOARD_COLS for _ in range(BOARD_ROWS)]
                    player_turn = True
                    ai_turn = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        if ai_turn and not check_win('X'):
            available_moves = []
            for row in range(BOARD_ROWS):
                for col in range(BOARD_COLS):
                    if board[row][col] is None:
                        available_moves.append((row, col))
            if len(available_moves) > 0:
                move = random.choice(available_moves)
                board[move[0]][move[1]] = 'O'
                draw_board()
                pygame.display.update()
                pygame.time.wait(500)
                ai_turn = False
                player_turn = True
        if check_win('X'):
            draw_board()
            pygame.display.update()
            text = MOUSE_FONT.render("Игрок X побеждает!", True, RED)
            screen.blit(text, (WIDTH // 2 - 150, HEIGHT // 2 - 25))
            pygame.display.update()
            pygame.time.wait(2000)
            exit();
        elif check_win('O'):
            draw_board()
            pygame.display.update()
            text = MOUSE_FONT.render("Игрок О побеждает!", True, RED)
            screen.blit(text, (WIDTH // 2 - 150, HEIGHT // 2 - 25))
            pygame.display.update()
            pygame.time.wait(2000)
            exit();
        elif all([cell != None for row in board for cell in row]):
            draw_board()
            pygame.display.update()
            text = MOUSE_FONT.render("Это ничья!", True, RED)
            screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2 - 25))
            pygame.display.update()
            pygame.time.wait(2000)
            exit();
if __name__ == "__main__":
    main()
