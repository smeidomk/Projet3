#!/usr/bin/python3
# -*- coding: Utf-8 -*
import pygame
from pygame.locals import (QUIT, KEYDOWN, K_ESCAPE, K_RETURN)
from pygame.locals import (K_SPACE, K_RIGHT, K_LEFT, K_UP, K_DOWN)
from macgyver import Macgyver
from labyrinth import Level

#class Main

def main(labychoice, surface):
    score = 0
    level = Level(labychoice)
    #Display the labyrinth
    level.display(surface, score)
    #initialise Macgyver's position in the labyrinth
    mcgyver = Macgyver(level.pos_mcgyver[0], level.pos_mcgyver[1], level)

    while True:

        pygame.time.Clock().tick(30)
        # Initialise the personage
        for event in pygame.event.get():
            # Display mcgyver position after every movement

            if event.type == QUIT:
                quit()
            elif event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    quit()
                # if mcgyver move to the right
                elif event.key == K_RIGHT:
                    mcgyver.move("d", level.structure)
                # if mcgyver goes left in the laby
                elif event.key == K_LEFT:
                    mcgyver.move("q", level.structure)
                # if mcgyver move up in the laby
                elif event.key == K_UP:
                    mcgyver.move("z", level.structure)
                # if mcgyver move down in the laby
                elif event.key == K_DOWN:
                    mcgyver.move("s", level.structure)

        # display the score of mcgyver on the screen
        level.display(surface, mcgyver.score)
        level.read_coordinates()
        #print("Position x: ", mcgyver.x, "Position y: ", mcgyver.y)

        pygame.display.flip()
        # if macgyver end the game the user can choose to replay or quit the game
        if mcgyver.finish:
            mcgyver.check_victory_or_defeat()
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                        # if the user want to leave the game after reaching the guardian
                        quit()
                    elif event.type == KEYDOWN:
                        #if the user tap space the game restart with laby1
                        if event.key == K_SPACE:
                            return True
                        #if the user tap the return button he can replay in laby2
                        elif event.key == K_RETURN:
                            return True
                        #if he choose the escape button he can quit the game