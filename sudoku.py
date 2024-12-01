import pygame
from cell import Cell
from board import Board
import sudoku_generator

if __name__ == "__main__":

    # creates a pygame screen
    screen = pygame.display.set_mode((880, 1060))
    screen.fill((210, 231, 244))
    run = True
    board = Board(9, 9, screen, "test")
    board.draw()
    board.select(0, 0)

    while run:

        if board.check_win():
            print("You won")
            run = False
        # ends the loop if the escape key or the x button are clicked
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_1:
                    board.sketch_number(1)
                if event.key == pygame.K_2:
                    board.sketch_number(2)
                if event.key == pygame.K_3:
                    board.sketch_number(3)
                if event.key == pygame.K_4:
                    board.sketch_number(4)
                if event.key == pygame.K_5:
                    board.sketch_number(5)
                if event.key == pygame.K_6:
                    board.sketch_number(6)
                if event.key == pygame.K_7:
                    board.sketch_number(7)
                if event.key == pygame.K_8:
                    board.sketch_number(8)
                if event.key == pygame.K_9:
                    board.sketch_number(9)
                if event.key == pygame.K_RETURN:
                    val = board.get_value()
                    board.place_number(-val)
                if event.key == pygame.K_UP:
                    curr_selected = board.selected
                    if curr_selected[0] != 0:
                        board.select(curr_selected[0] - 1, curr_selected[1])
                if event.key == pygame.K_DOWN:
                    curr_selected = board.selected
                    if curr_selected[0] != 8:
                        board.select(curr_selected[0] + 1, curr_selected[1])
                if event.key == pygame.K_LEFT:
                    curr_selected = board.selected
                    if curr_selected[1] != 0:
                        board.select(curr_selected[0], curr_selected[1] - 1)
                if event.key == pygame.K_RIGHT:
                    curr_selected = board.selected
                    if curr_selected[1] != 8:
                        board.select(curr_selected[0], curr_selected[1] + 1)

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                rc = board.click(pos[0], pos[1])
                if rc:
                    board.select(rc[0], rc[1])

        # updates the game screen
        pygame.display.update()

    # kills the pygame window
    pygame.quit()
