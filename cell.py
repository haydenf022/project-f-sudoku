import pygame
from constants import *

pygame.init()


class Cell:

    # constructor for the cell class
    def __init__(self, screen, value=0, row=0, col=0) -> None:
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.font = pygame.font.Font("freesansbold.ttf", FONT_SIZE)
        self.sketched_font = pygame.font.Font("freesansbold.ttf", SKETCH_FONT_SIZE)

    # sets the value of the cell to the value passed
    def set_cell_value(self, value):
        self.value = value

    # sets the value of the cell to a negative version of the value passed to signify sketch
    def set_sketched_value(self, value):
        self.value = -value

    # draws the cell on the screen
    def draw(self):
        pygame.draw.rect(self.screen, WHITE, pygame.Rect(self.col * CELL_SIZE + BOARD_LEFT, self.row * CELL_SIZE + BOARD_TOP, CELL_SIZE, CELL_SIZE))
        if self.value > 0:
            text = self.font.render(str(self.value), True, BLACK, WHITE)
            textRect = text.get_rect()
            textRect.center = (self.col * CELL_SIZE + BOARD_LEFT + OFFSET_FOR_TEXT, self.row * CELL_SIZE + BOARD_TOP + OFFSET_FOR_TEXT)
            self.screen.blit(text, textRect)
        elif self.value == 0:
            pass
        else:
            text = self.sketched_font.render(str(-self.value), True, BLACK, WHITE)
            textRect = text.get_rect()
            textRect.center = (self.col * CELL_SIZE + BOARD_LEFT + OFFSET_FOR_SKETCH_TEXT, self.row * CELL_SIZE + BOARD_TOP + OFFSET_FOR_SKETCH_TEXT)
            self.screen.blit(text, textRect)
