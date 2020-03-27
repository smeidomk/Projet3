#!/usr/bin/python3
# -*- coding: Utf-8 -*
import random
import pygame
import pygame.locals
from unfroz import find_data_file
from constants import (
    TUBE,
    LABY_SIZE,
    SPRITE_SIDE,
    MCGYVER_LETTER,
    MACGYVER,
    BACKGROUND,
    NEEDLE,
    ETHER,
    WALL,
    GARDIAN,
    SCORE_1,
    SCORE_2,
    SCORE_3
)


class Level:
    # Level define the coordinates of the elements use to build the labyrinth
    # Create the objects and position them randomly in the labyrinth
    # Display every element with pygame

    def __init__(self, laby):
        self.laby = laby
        self.structure = 0
        self.read_coordinates()
        self.randomize_obj()

    def read_coordinates(self):
        # create a dictionnary of coordinates for the labyrinth
        structure_level = {}
        pos_y = 0
        # for every line in the labyrinth we add 1 in coordinates
        for line in self.laby:
            pos_x = 0
            for sprite in line:
                if sprite == MCGYVER_LETTER:
                    self.pos_mcgyver = (pos_x, pos_y)
                structure_level[(pos_x, pos_y)] = sprite
                pos_x += 1
            pos_y += 1
        self.structure = structure_level

    def randomize_obj(self):
        # randomize_obj locate randomly every objects in the labyrinth
        # LABY_SIZE - 1 = 14
        objects = ["E", "T", "N"]
        pos_x = random.randint(0, 14)
        pos_y = random.randint(0, 14)
        # objects are positionize regarding their coordinates (pos_x, pos_y)
        for obj in objects:
            while self.structure[(pos_x, pos_y)] in ["M", "X", "G", "E", "T", "N"]:
                pos_x = random.randint(0, 14)
                pos_y = random.randint(0, 14)
            self.structure[(pos_x, pos_y)] = obj

    def display(self, surface, score):
        # display every element of the of the labyrinth
        pymage = pygame.image

        background = pymage.load(find_data_file(BACKGROUND)).convert_alpha()
        mcgyver = pymage.load(find_data_file(MACGYVER)).convert_alpha()
        tube = pymage.load(find_data_file(TUBE)).convert_alpha()
        needle = pymage.load(find_data_file(NEEDLE)).convert_alpha()
        gardian = pymage.load(find_data_file(GARDIAN)).convert_alpha()
        wall = pymage.load(find_data_file(WALL)).convert_alpha()
        ether = pymage.load(find_data_file(ETHER)).convert_alpha()

        # display every elements of the labyrinth
        # the labyrinth with a list
        laby_map = []
        # level represent every line of the labyrinth
        level = ""
        surface.blit(background, (0, 0))

        # display every element
        for coord, sprite in self.structure.items():
            pos_x = coord[0] * SPRITE_SIDE
            pos_y = coord[1] * SPRITE_SIDE
            # display the wall
            if sprite == 'X':
                surface.blit(wall, (pos_x, pos_y))
            # display the main character
            elif sprite == 'M':
                surface.blit(mcgyver, (pos_x, pos_y))
            # display the gardian
            elif sprite == 'G':
                surface.blit(gardian, (pos_x, pos_y))
            # display a random object
            elif sprite == 'E':
                surface.blit(ether, (pos_x, pos_y))
            # display a random object
            elif sprite == 'T':
                surface.blit(tube, (pos_x, pos_y))
            # display a random object
            elif sprite == 'N':
                surface.blit(needle, (pos_x, pos_y))
            # add a sprite on the level
            level += sprite
            # add a level
            if len(level) == LABY_SIZE:
                laby_map.append(level)
                level = ""
        #  update the laby:
        self.laby = laby_map

        # display the score
        score_one = pymage.load(find_data_file(SCORE_1)).convert_alpha()
        score_two = pymage.load(find_data_file(SCORE_2)).convert_alpha()
        score_three = pymage.load(find_data_file(SCORE_3)).convert_alpha()

        if score == 1:
            surface.blit(score_one, (420, 0))
        elif score == 2:
            surface.blit(score_two, (420, 0))
        elif score == 3:
            surface.blit(score_three, (420, 0))

        pygame.display.flip()
