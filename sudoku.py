import pygame
from cell import Cell

if __name__ == "__main__":

    # creates a pygame screen
    screen = pygame.display.set_mode((500, 600))
    run = True

    while run:
        # ends the loop if the escape key or the x button are clicked
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            elif event.type == pygame.QUIT:
                run = False

        # testing drawing on the screen, creates a default cell
        cell = Cell(screen)
        cell.draw()

        # updates the game screen
        pygame.display.update()

    # kills the pygame window
    pygame.quit()
