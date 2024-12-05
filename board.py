import pygame
from cell import Cell
from sudoku_generator import SudokuGenerator
import sudoku_generator
from constants import *

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
        self.sudoku_generator_obj = SudokuGenerator(ROW_LENGTH, removed)
        self.sudoku_generator_obj.board = sudoku_generator.generate_sudoku(ROW_LENGTH, removed)
        self.board = self.sudoku_generator_obj.board
        self.cells = []
        self.original_board = [row[:] for row in self.sudoku_generator_obj.board]
        for row_index in range(len(self.board)):
            for column_index in range(len(self.board[row_index])):
                self.cells.append(Cell(self.screen, self.board[row_index][column_index], row_index, column_index))
        self.selected = (0, 0)
        self.all_correct = True

    def draw(self):
        # uses the draw method in the cell class for all of the cells in the list
        [cell.draw() for cell in self.cells]

        # next two for loops draw the lines for cell delimiters
        for cell in range(10):
            pygame.draw.rect(self.screen, BLACK, pygame.Rect(BOARD_LEFT, cell * CELL_SIZE + BOARD_TOP, BOARD_WIDTH, THIN_LINE_WIDTH))

        for cell in range(10):
            pygame.draw.rect(self.screen, BLACK, pygame.Rect(cell * CELL_SIZE + BOARD_LEFT, BOARD_TOP, THIN_LINE_WIDTH, BOARD_WIDTH))

        # next four for loops draw the lines for box delimiters
        for cell in range(1, 3):
            pygame.draw.rect(self.screen, BLACK, pygame.Rect(BOARD_LEFT, cell * DISTANCE_BETWEEN_THICK_LINES + BOARD_TOP, BOARD_WIDTH, THICK_LINE_WIDTH))

        for cell in range(1, 3):
            pygame.draw.rect(self.screen, BLACK, pygame.Rect(cell * DISTANCE_BETWEEN_THICK_LINES + BOARD_LEFT, BOARD_TOP, THICK_LINE_WIDTH, BOARD_WIDTH))

        
    def select(self, row, col):
        # initializes variables for selected cell
        prev_row = self.selected[0]
        prev_col = self.selected[1]
        # redraws the black cell delimiters after a new cell is selected
        pygame.draw.rect(self.screen, BLACK, pygame.Rect(BOARD_LEFT + prev_col * CELL_SIZE, BOARD_TOP + prev_row * CELL_SIZE, THIN_LINE_WIDTH, CELL_SIZE))
        pygame.draw.rect(self.screen, BLACK, pygame.Rect(CELL_0_0_RIGHT + prev_col * CELL_SIZE, BOARD_TOP + prev_row * CELL_SIZE, THIN_LINE_WIDTH, CELL_SIZE))
        pygame.draw.rect(self.screen, BLACK, pygame.Rect(BOARD_LEFT + prev_col * CELL_SIZE, BOARD_TOP + prev_row * CELL_SIZE, CELL_SIZE, THIN_LINE_WIDTH))
        pygame.draw.rect(self.screen, BLACK, pygame.Rect(BOARD_LEFT + prev_col * CELL_SIZE, 140 + prev_row * CELL_SIZE, CELL_SIZE, THIN_LINE_WIDTH))
        # sets the selected attribute to the new cell
        self.selected = (row, col)
        new_row = self.selected[0]
        new_col = self.selected[1]
        # draws the red delimiters around the new selected cell
        pygame.draw.rect(self.screen, RED, pygame.Rect(BOARD_LEFT + new_col * CELL_SIZE, BOARD_TOP + new_row * CELL_SIZE, THIN_LINE_WIDTH, CELL_SIZE))
        pygame.draw.rect(self.screen, RED, pygame.Rect(CELL_0_0_RIGHT + new_col * CELL_SIZE, BOARD_TOP + new_row * CELL_SIZE, THIN_LINE_WIDTH, CELL_SIZE))
        pygame.draw.rect(self.screen, RED, pygame.Rect(BOARD_LEFT + new_col * CELL_SIZE, BOARD_TOP + new_row * CELL_SIZE, CELL_SIZE, THIN_LINE_WIDTH))
        pygame.draw.rect(self.screen, RED, pygame.Rect(BOARD_LEFT + new_col * CELL_SIZE, 140 + new_row * CELL_SIZE, CELL_SIZE, THIN_LINE_WIDTH))

    def place_number(self, value):
        # initializes variables for selected cell
        selected_row = self.selected[0]
        selected_col = self.selected[1]
        # if the number being placed isn't valid, it makes sure the user will lose when submitting
        if not self.sudoku_generator_obj.is_valid(selected_row, selected_col, value) and value != 0:
            self.all_correct = False
        # checks if the spot selected can be changed, if so, it adds the number to the arrays
        if self.board[selected_row][selected_col] == 0:
            self.cells[selected_row * ROW_LENGTH + selected_col].set_cell_value(value)
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
            self.cells[selected_row * ROW_LENGTH + selected_col].set_cell_value(-value)
        # redraws board and selected cell
        self.draw()
        self.select(self.selected[0], self.selected[1])

    def click(self, x, y):
        # determines if the user clicked on one of the cells
        if x in range(BOARD_LEFT, BOARD_RIGHT):
            if y in range(BOARD_TOP, BOARD_BOTTOM):
                # returns the cell the user clicked on
                return (int((y - BOARD_TOP) / CELL_SIZE), int((x - BOARD_LEFT) / CELL_SIZE))
        return None

    def get_value(self):
        # returns the value of the cell
        return self.cells[self.selected[0] * ROW_LENGTH + self.selected[1]].value

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
                self.cells[row_index * ROW_LENGTH + col_index].set_cell_value(value)
        self.draw()