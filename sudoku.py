import pygame

from board import Board
from constants import *

if __name__ == "__main__":

    # creates a pygame screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    screen.fill(BACKGROUND_COLOR)

    difficulty = None
    run = True
    selecting = True
    font = pygame.font.Font(None, SMALL_FONT_SIZE)

    while run:
        while selecting:
            text1 = pygame.font.Font(None, LARGE_FONT_SIZE).render("Welcome to Sudoku!", True, BLACK)
            text_rect1 = text1.get_rect(center=WELCOME_WIN_LOSE_TEXT_CENTER)
            screen.blit(text1, text_rect1)
            text2 = pygame.font.Font(None, MEDIUM_FONT_SIZE).render("Choose Your Difficulty:", True, BLACK)
            text_rect2 = text2.get_rect(center=DIFFICULTY_EXIT_TRY_AGAIN_TEXT_CENTER)
            screen.blit(text2, text_rect2)
            # drawing easy button
            easy_rect = pygame.Rect(DIFFICULTY_X[0], START_SCREEN_BUTTONS[2], START_SCREEN_BUTTONS[1], START_SCREEN_BUTTONS[0])
            pygame.draw.rect(screen, GREEN, easy_rect)
            easy_text = font.render("Easy", True, WHITE)
            screen.blit(easy_text, easy_text.get_rect(center=easy_rect.center))
            # drawing medium button
            medium_rect = pygame.Rect(DIFFICULTY_X[1], START_SCREEN_BUTTONS[2], START_SCREEN_BUTTONS[1], START_SCREEN_BUTTONS[0])
            pygame.draw.rect(screen, BLUE, medium_rect)
            medium_text = font.render("Medium", True, WHITE)
            screen.blit(medium_text, medium_text.get_rect(center=medium_rect.center))
            # drawing hard button
            hard_rect = pygame.Rect(DIFFICULTY_X[2], START_SCREEN_BUTTONS[2], START_SCREEN_BUTTONS[1], START_SCREEN_BUTTONS[0])
            pygame.draw.rect(screen, RED, hard_rect)
            hard_text = font.render("Hard", True, WHITE)
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
                        screen.fill(BACKGROUND_COLOR)
                        board = Board(9, 9, screen, difficulty)
                        board.draw()
                        board.select(0, 0)
                        selecting = False
                        difficulty = None
            pygame.display.update()
        if board.is_full():
            screen.fill(BACKGROUND_COLOR)
            if board.check_win():
                text1 = pygame.font.Font(None, LARGE_FONT_SIZE).render("Game Won!", True, BLACK)
                text_rect1 = text1.get_rect(center=WELCOME_WIN_LOSE_TEXT_CENTER)
                screen.blit(text1, text_rect1)
                text2 = pygame.font.Font(None, MEDIUM_FONT_SIZE).render("You May Exit The Game", True, BLACK)
                text_rect2 = text2.get_rect(center=DIFFICULTY_EXIT_TRY_AGAIN_TEXT_CENTER)
                screen.blit(text2, text_rect2)
                result_text = pygame.font.Font(None, SMALL_FONT_SIZE).render("Exit", True, WHITE)
            else:
                text1 = pygame.font.Font(None, LARGE_FONT_SIZE).render("Game Over!", True, BLACK)
                text_rect1 = text1.get_rect(center=WELCOME_WIN_LOSE_TEXT_CENTER)
                screen.blit(text1, text_rect1)
                text2 = pygame.font.Font(None, MEDIUM_FONT_SIZE).render("Try Again?", True, BLACK)
                text_rect2 = text2.get_rect(center=DIFFICULTY_EXIT_TRY_AGAIN_TEXT_CENTER)
                screen.blit(text2, text_rect2)
                result_text = pygame.font.Font(None, SMALL_FONT_SIZE).render("Restart", True, WHITE)
            result_rect = pygame.Rect(RESULT_LEFT, RESULT_TOP, RESULT_WIDTH, RESULT_HEIGHT)
            pygame.draw.rect(screen, BLACK, result_rect)
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
                            screen.fill(BACKGROUND_COLOR)
                            selecting = True
        else:
            # drawing reset button
            reset_rect = pygame.Rect(CONTROLS_X[0], GAME_SCREEN_BUTTONS[2], GAME_SCREEN_BUTTONS[1], GAME_SCREEN_BUTTONS[0])
            pygame.draw.rect(screen, BLACK, reset_rect)
            reset_text = font.render("Reset", True, WHITE)
            screen.blit(reset_text, reset_text.get_rect(center=reset_rect.center))
            # drawing restart button
            restart_rect = pygame.Rect(CONTROLS_X[1], GAME_SCREEN_BUTTONS[2], GAME_SCREEN_BUTTONS[1], GAME_SCREEN_BUTTONS[0])
            pygame.draw.rect(screen, BLACK, restart_rect)
            restart_text = font.render("Restart", True, WHITE)
            screen.blit(restart_text, restart_text.get_rect(center=restart_rect.center))
            # drawing exit button
            exit_rect = pygame.Rect(CONTROLS_X[2], GAME_SCREEN_BUTTONS[2], GAME_SCREEN_BUTTONS[1], GAME_SCREEN_BUTTONS[0])
            pygame.draw.rect(screen, BLACK, exit_rect)
            exit_text = font.render("Exit", True, WHITE)
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
                        screen.fill(BACKGROUND_COLOR)
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
