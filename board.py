import pygame
from cell import Cell
from sudoku_generator import SudokuGenerator
import sudoku_generator


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        match self.difficulty:
            case "easy":
                removed = 30
            case "medium":
                removed = 40
            case "hard":
                removed = 50
            case "test":
                removed = 3
        self.sudoku_generator = SudokuGenerator(9, removed)
        self.sudoku_generator.board = sudoku_generator.generate_sudoku(9, removed)
        self.immutable_cells = self.sudoku_generator.board
        self.cells = []
        for row_index in range(len(self.immutable_cells)):
            for column_index in range(len(self.immutable_cells[row_index])):
                self.cells.append(
                    Cell(
                        self.screen,
                        self.immutable_cells[row_index][column_index],
                        row_index,
                        column_index,
                    )
                )
        self.selected = (0, 0)

    def draw(self):

        [cell.draw() for cell in self.cells]

        for i in range(10):
            pygame.draw.rect(
                self.screen,
                (0, 0, 0),
                pygame.Rect(170, i * 60 + 80, 540, 2),
            )

        for i in range(10):
            pygame.draw.rect(
                self.screen,
                (0, 0, 0),
                pygame.Rect(i * 60 + 170, 80, 2, 540),
            )

        for i in range(1, 3):
            pygame.draw.rect(
                self.screen,
                (0, 0, 0),
                pygame.Rect(170, i * 180 + 80, 540, 5),
            )

        for i in range(1, 3):
            pygame.draw.rect(
                self.screen,
                (0, 0, 0),
                pygame.Rect(i * 180 + 170, 80, 5, 540),
            )

    def select(self, row, col):
        prev_row = self.selected[0]
        prev_col = self.selected[1]
        pygame.draw.rect(
            self.screen,
            (0, 0, 0),
            pygame.Rect(170 + prev_col * 60, 80 + prev_row * 60, 2, 60),
        )
        pygame.draw.rect(
            self.screen,
            (0, 0, 0),
            pygame.Rect(230 + prev_col * 60, 80 + prev_row * 60, 2, 60),
        )
        pygame.draw.rect(
            self.screen,
            (0, 0, 0),
            pygame.Rect(170 + prev_col * 60, 80 + prev_row * 60, 60, 2),
        )
        pygame.draw.rect(
            self.screen,
            (0, 0, 0),
            pygame.Rect(170 + prev_col * 60, 140 + prev_row * 60, 60, 2),
        )
        self.selected = (row, col)
        new_row = self.selected[0]
        new_col = self.selected[1]
        pygame.draw.rect(
            self.screen,
            (255, 0, 0),
            pygame.Rect(170 + new_col * 60, 80 + new_row * 60, 2, 60),
        )
        pygame.draw.rect(
            self.screen,
            (255, 0, 0),
            pygame.Rect(230 + new_col * 60, 80 + new_row * 60, 2, 60),
        )
        pygame.draw.rect(
            self.screen,
            (255, 0, 0),
            pygame.Rect(170 + new_col * 60, 80 + new_row * 60, 60, 2),
        )
        pygame.draw.rect(
            self.screen,
            (255, 0, 0),
            pygame.Rect(170 + new_col * 60, 140 + new_row * 60, 60, 2),
        )

    def place_number(self, value):
        selected_row = self.selected[0]
        selected_col = self.selected[1]
        if self.immutable_cells[selected_row][selected_col] == 0:
            self.cells[selected_row * 9 + selected_col].set_cell_value(value)
            self.sudoku_generator.board[selected_row][selected_col] = value
        self.draw()
        self.select(self.selected[0], self.selected[1])

    def sketch_number(self, value):
        selected_row = self.selected[0]
        selected_col = self.selected[1]
        if self.immutable_cells[selected_row][selected_col] == 0:
            self.cells[selected_row * 9 + selected_col].set_cell_value(-value)
        self.draw()
        self.select(self.selected[0], self.selected[1])

    def click(self, x, y):
        # print(x, y)
        if x in range(170, 711):
            if y in range(80, 621):
                # print((int((y - 80) / 60), int((x - 170) / 60)))
                return (int((y - 80) / 60), int((x - 170) / 60))
        return None

    def get_value(self):
        return self.cells[self.selected[0] * 9 + self.selected[1]].value

    def is_full(self):
        ret = True
        for cell in self.cells:
            if cell.value <= 0:
                ret = False
        return ret

    def check_win(self):
        if self.is_full():
            return is_valid_sudoku(self.sudoku_generator.board)


def is_valid_sudoku(board):
    for row in board:
        if not is_valid_set(row):
            return False
    for col in range(9):
        if not is_valid_set([board[row][col] for row in range(9)]):
            return False

    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            if not is_valid_set(
                [board[r][c] for r in range(row, row + 3) for c in range(col, col + 3)]
            ):
                return False

    return True


def is_valid_set(nums):
    seen = set()
    for num in nums:
        if num == 0:
            continue
        if num in seen or num < 1 or num > 9:
            return False
        seen.add(num)
    return True
