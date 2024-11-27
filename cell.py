import pygame


class Cell:

    # constructor for the cell class
    def __init__(self, screen, value=0, row=0, col=0) -> None:
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    # sets the value of the cell to the value passed
    def set_cell_value(self, value):
        self.value = value

    # sets the value of the cell to a negative version of the value passed to signify sketch
    def set_sketched_value(self, value):
        self.value = -value

    # draws the cell on the screen
    # currently just draws white square
    def draw(self):
        color = (255, 255, 255)
        pygame.draw.rect(self.screen, color, pygame.Rect(30, 30, 60, 60))
