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
        self.sudoku_generator_obj = SudokuGenerator(9, removed)
        self.sudoku_generator_obj.board = sudoku_generator.generate_sudoku(9, removed)
        self.board = self.sudoku_generator_obj.board
        self.cells = []
        self.original_board = [row[:] for row in self.sudoku_generator_obj.board]
        for row_index in range(len(self.board)):
            for column_index in range(len(self.board[row_index])):
                self.cells.append(
                    Cell(
                        self.screen,
                        self.board[row_index][column_index],
                        row_index,
                        column_index,
                    )
                )
        self.selected = (0, 0)
        self.all_correct = True

    def draw(self):
        # uses the draw method in the cell class for all of the cells in the list
        [cell.draw() for cell in self.cells]

        # next 2 for loops draw the lines for cell delimiters
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

        # next 4 for loops draw the lines for box delimiters
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
        # initializes variables for selected cell
        prev_row = self.selected[0]
        prev_col = self.selected[1]
        # redraws the black cell delimiters after a new cell is selected
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
        # sets the selected attribute to the new cell
        self.selected = (row, col)
        new_row = self.selected[0]
        new_col = self.selected[1]
        # draws the red delimiters around the new selected cell
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
        # initializes variables for selected cell
        selected_row = self.selected[0]
        selected_col = self.selected[1]
        # if the number being placed isn't valid, it makes sure the user will lose when submitting
        if not self.sudoku_generator_obj.is_valid(selected_row, selected_col, value) and value != 0:
            self.all_correct = False
        # checks if the spot selected can be changed, if so, it adds the number to the arrays
        if self.board[selected_row][selected_col] == 0:
            self.cells[selected_row * 9 + selected_col].set_cell_value(value)
            self.board[selected_row][selected_col] = value
        # redraws board and selected cell
        self.draw()
        self.select(self.selected[0], self.selected[1])
        

    def sketch_number(self, value):
        # initializes variables for selected cell
        selected_row = self.selected[0]
        selected_col = self.selected[1]
        # checks if the spot selected can be changed, if so, it draws the sketch || negative value signifies sketch
        if self.board[selected_row][selected_col] == 0:
            self.cells[selected_row * 9 + selected_col].set_cell_value(-value)
        # redraws board and selected cell
        self.draw()
        self.select(self.selected[0], self.selected[1])

    def click(self, x, y):
        # determines if the user clicked on one of the cells
        if x in range(170, 711):
            if y in range(80, 621):
                # returns the cell the user clicked on
                return (int((y - 80) / 60), int((x - 170) / 60))
        return None

    def get_value(self):
        # returns the value of the cell
        return self.cells[self.selected[0] * 9 + self.selected[1]].value

    def is_full(self):
        # checks if the board is full
        ret = True
        for cell in self.cells:
            if cell.value <= 0:
                ret = False
        return ret

    def check_win(self):
        # determines if the user won or lost
        if self.is_full():
            return self.all_correct

    def reset_to_original(self):
        self.board = [row[:] for row in self.original_board]
        for row_index in range(len(self.board)):
            for col_index in range(len(self.board[row_index])):
                value = self.board[row_index][col_index]
                self.cells[row_index * 9 + col_index].set_cell_value(value)
        self.draw()