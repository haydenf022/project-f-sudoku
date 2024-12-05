import pygame
from matplotlib.backend_bases import button_press_handler

from cell import Cell
from board import Board
import sudoku_generator

if __name__ == "__main__":

    # creates a pygame screen
    screen = pygame.display.set_mode((880, 880))
    screen.fill((210, 231, 244))

    # setting button constants for start screen
    button1_h = 50
    button1_w = 150
    button1_y = 660
    easy_x = 220 - 75
    medium_x = 440 - 75
    hard_x = 660 - 75

    # setting button constants for game screen
    button2_h = 50
    button2_w = 150
    button2_y = 715
    reset_x = 220 - 75
    restart_x = 440 - 75
    exit_x = 660 - 75

    difficulty = None
    run = True
    selecting = True
    font = pygame.font.Font(None, 50)

    while run:
        while selecting:
            text1 = pygame.font.Font(None, 100).render("Welcome to Sudoku!", True, (0,0,0))
            text_rect1 = text1.get_rect(center=(440, 220))
            screen.blit(text1, text_rect1)
            text2 = pygame.font.Font(None, 75).render("Choose Your Difficulty:", True, (0, 0, 0))
            text_rect2 = text2.get_rect(center=(440, 440))
            screen.blit(text2, text_rect2)
            # drawing easy button
            easy_rect = pygame.Rect(easy_x, button1_y, button1_w, button1_h)
            pygame.draw.rect(screen, (0,255,0), easy_rect)
            easy_text = font.render("Easy", True, (255,255,255))
            screen.blit(easy_text, easy_text.get_rect(center=easy_rect.center))
            # drawing medium button
            medium_rect = pygame.Rect(medium_x, button1_y, button1_w, button1_h)
            pygame.draw.rect(screen, (0,0,255), medium_rect)
            medium_text = font.render("Medium", True, (255,255,255))
            screen.blit(medium_text, medium_text.get_rect(center=medium_rect.center))
            # drawing hard button
            hard_rect = pygame.Rect(hard_x, button1_y, button1_w, button1_h)
            pygame.draw.rect(screen, (255,0,0), hard_rect)
            hard_text = font.render("Hard", True, (255,255,255))
            screen.blit(hard_text, hard_text.get_rect(center=hard_rect.center))
            # making buttons clickable
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    selecting = False
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    # easy button
                    if easy_rect.left <= mouse_pos[0] <= easy_rect.right and easy_rect.top <= mouse_pos[1] <= easy_rect.bottom:
                        difficulty = "easy"
                    # medium button
                    if medium_rect.left <= mouse_pos[0] <= medium_rect.right and medium_rect.top <= mouse_pos[1] <= medium_rect.bottom:
                        difficulty = "medium"
                    # hard button
                    if hard_rect.left <= mouse_pos[0] <= hard_rect.right and hard_rect.top <= mouse_pos[1] <= hard_rect.bottom:
                        difficulty = "hard"
                    if difficulty != None:
                        screen.fill((210, 231, 244))
                        board = Board(9, 9, screen, difficulty)
                        board.draw()
                        board.select(0, 0)
                        selecting = False
            pygame.display.update()
        if board.is_full():
            screen.fill((210, 231, 244))
            if board.check_win():
                text1 = pygame.font.Font(None, 100).render("Game Won!", True, (0, 0, 0))
                text_rect1 = text1.get_rect(center=(440, 220))
                screen.blit(text1, text_rect1)
                text2 = pygame.font.Font(None, 75).render("You May Exit The Game", True, (0, 0, 0))
                text_rect2 = text2.get_rect(center=(440, 440))
                screen.blit(text2, text_rect2)
                result_text = pygame.font.Font(None, 50).render("Exit", True, (255, 255, 255))
            else:
                text1 = pygame.font.Font(None, 100).render("Game Over!", True, (0, 0, 0))
                text_rect1 = text1.get_rect(center=(440, 220))
                screen.blit(text1, text_rect1)
                text2 = pygame.font.Font(None, 75).render("Try Again?", True, (0, 0, 0))
                text_rect2 = text2.get_rect(center=(440, 440))
                screen.blit(text2, text_rect2)
                result_text = pygame.font.Font(None, 50).render("Restart", True, (255, 255, 255))
            result_rect = pygame.Rect(440-150, 660, 300, 100)
            pygame.draw.rect(screen, (0,0,0), result_rect)
            screen.blit(result_text, result_text.get_rect(center=result_rect.center))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    selecting = False
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if result_rect.left <= mouse_pos[0] <= result_rect.right and result_rect.top <= mouse_pos[1] <= result_rect.bottom:
                        if board.check_win():
                            selecting = False
                            run = False
                        else:
                            screen.fill((210, 231, 244))
                            selecting = True
        else:
            # drawing reset button
            reset_rect = pygame.Rect(reset_x, button2_y, button2_w, button2_h)
            pygame.draw.rect(screen, (0,0,0), reset_rect)
            reset_text = font.render("Reset", True, (255,255,255))
            screen.blit(reset_text, reset_text.get_rect(center=reset_rect.center))
            # drawing restart button
            restart_rect = pygame.Rect(restart_x, button2_y, button2_w, button2_h)
            pygame.draw.rect(screen, (0,0,0), restart_rect)
            restart_text = font.render("Restart", True, (255,255,255))
            screen.blit(restart_text, restart_text.get_rect(center=restart_rect.center))
            # drawing exit button
            exit_rect = pygame.Rect(exit_x, button2_y, button2_w, button2_h)
            pygame.draw.rect(screen, (0,0,0), exit_rect)
            exit_text = font.render("Exit", True, (255,255,255))
            screen.blit(exit_text, exit_text.get_rect(center=exit_rect.center))

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
                    if event.key == pygame.K_BACKSPACE:
                        board.place_number(0)
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

                    # making buttons clickable
                    mouse_pos = pygame.mouse.get_pos()
                    # reset button
                    if reset_rect.left <= mouse_pos[0] <= reset_rect.right and reset_rect.top <= mouse_pos[1] <= reset_rect.bottom:
                        board.reset_to_original()
                    # restart button
                    if restart_rect.left <= mouse_pos[0] <= restart_rect.right and restart_rect.top <= mouse_pos[1] <= restart_rect.bottom:
                        screen.fill((210, 231, 244))
                        selecting = True
                    # exit button
                    if exit_rect.left <= mouse_pos[0] <= exit_rect.right and exit_rect.top <= mouse_pos[1] <= exit_rect.bottom:
                        run = False

                    pos = pygame.mouse.get_pos()
                    rc = board.click(pos[0], pos[1])
                    if rc:
                        board.select(rc[0], rc[1])

        # updates the game screen
        pygame.display.update()

    # kills the pygame window
    pygame.quit()
