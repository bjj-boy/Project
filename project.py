import random
import os
import time
BOARD_SIZE = 3
CELL_SIZE = 12
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def draw_board(board):
    clear_screen()
    print(f"{RED}{'-' * ((CELL_SIZE * BOARD_SIZE) + (BOARD_SIZE - 1))}{RESET}\n")
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            cell_content = board[row][col]
            if cell_content == 'X':
                print(f"| {GREEN}{'X'.center(CELL_SIZE)}{RESET}", end="")
            elif cell_content == 'O':
                print(f"| {RED}{'O'.center(CELL_SIZE)}{RESET}", end="")
            else:
                print(f"| {' '.center(CELL_SIZE)}", end="")
            if col < BOARD_SIZE - 1:
                print(" |", end="")
        print("\n" + f"{RED}{'-' * ((CELL_SIZE * BOARD_SIZE) + (BOARD_SIZE - 1))}{RESET}")
def check_win(board, player):
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    for condition in win_conditions:
        if all(board[r][c] == player for r, c in condition):
            return True
    return False
def main():
    board = [[' '] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    player = 'X'
    while True:
        draw_board(board)
        print(f"\nPlayer {player}'s turn.")
        move = input("Введи номер строки и колонки (через пробел от 1 до 3): ").split()
        if len(move) != 2:
            print("Ничего не пойму. Напиши номер строки и колонки через пробел от 1 до 3.")
            continue
        try:
            row, col = map(int, move)
            if row < 1 or row > 3 or col < 1 or col > 3:
                raise ValueError
        except ValueError:
            print("Ничего не пойму. Напиши номер строки и колонки через пробел от 1 до 3.")
            continue
        row -= 1
        col -= 1
        if board[row][col] != ' ':
            print("Слепой? Занято! Иди найди себе другую.")
            continue
        board[row][col] = player
        if check_win(board, player):
            draw_board(board)
            print(f"\nИгравший за {player} выиграл!")
            break
        if all(all(cell != ' ' for cell in row) for row in board):
            draw_board(board)
            print("\nНичья!")
            break
        player = 'O' if player == 'X' else 'X'
        time.sleep(1)
if __name__ == "__main__":
    main()
