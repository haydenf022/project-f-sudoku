import pygame

pygame.init()


class Cell:

    # constructor for the cell class
    def __init__(self, screen, value=0, row=0, col=0) -> None:
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.font = pygame.font.Font("freesansbold.ttf", 32)
        self.sketched_font = pygame.font.Font("freesansbold.ttf", 16)

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
        pygame.draw.rect(
            self.screen,
            color,
            pygame.Rect(self.col * 60 + 170, self.row * 60 + 80, 60, 60),
        )
        if self.value > 0:
            text = self.font.render(
                str(self.value),
                True,
                (0, 0, 0),
                (255, 255, 255),
            )
            textRect = text.get_rect()
            textRect.center = (self.col * 60 + 200, self.row * 60 + 110)
            self.screen.blit(text, textRect)
        elif self.value == 0:
            pass
        else:
            text = self.sketched_font.render(
                str(-self.value),
                True,
                (0, 0, 0),
                (255, 255, 255),
            )
            textRect = text.get_rect()
            textRect.center = (self.col * 60 + 185, self.row * 60 + 95)
            self.screen.blit(text, textRect)
