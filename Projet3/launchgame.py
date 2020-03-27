""" Call this module to launch the game from terminal """

import pygame
from unfroz import find_data_file
from constants import (
    ICONE,
    MENU,
    WINDOW_TITLE,
    WINDOW_SIDE,
    BLUE,
    LEVEL_1,
    LEVEL_2,
    QUIT_GAME,
    RED,
    ORANGE,
    LABYRINTHS
)
from main import main

pygame.init()

surface = pygame.display.set_mode((WINDOW_SIDE, WINDOW_SIDE))
logo = pygame.image.load(find_data_file(ICONE))
pygame.display.set_icon(logo)
pygame.display.set_caption(WINDOW_TITLE)

continue_macgyver = 1
choice = 0
while continue_macgyver:
    # Display the menu of the game
    welcome = pygame.image.load(find_data_file(MENU)).convert()
    arial_font = pygame.font.SysFont("arial", 20, True)
    level_1_text_surface = arial_font.render(LEVEL_1, False, BLUE)
    level_2_text_surface = arial_font.render(LEVEL_2, False, ORANGE)
    quit_text_surface = arial_font.render(QUIT_GAME, False, RED)
    surface.blit(welcome, (0, 0))
    surface.blit(level_1_text_surface, (100, 170))
    surface.blit(level_2_text_surface, (100, 250))
    surface.blit(quit_text_surface, (100, 310))
    pygame.display.flip()

    continue_menu = 1
    while continue_menu:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            # As we display the menu we give the player differents choices
            continue_macgyver = 1
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                # if quit() called stop the game
                quit()
            elif event.type == pygame.KEYDOWN:
                # while quit() not called continue the menu
                # the choose the maze he want to play in
                if event.key == pygame.K_RETURN:
                    # choose the laby1 with "return" button
                    continue_menu = 0
                    continue_game = 1
                    choice = "laby1"
                elif event.key == pygame.K_SPACE:
                    # choose the laby2 with "space" button
                    continue_menu = 0
                    continue_game = 1
                    choice = "laby2"

    if choice in ("laby1", "laby2"):
        # Wait for user input to get labychoice or quit game
        labychoice = LABYRINTHS[choice]

    replay = True
    # Replay used to know if user wants to play or not.
    # First replay is set to True as user wants to start game one time.
    # While replay is True, relaunch game when over.
    while replay:
        replay = main(labychoice, surface)
