#!/usr/bin/python3
# -*- coding: Utf-8 -*
import pygame
import pygame.locals
from unfroz import find_data_file
from constants import (
    LABY_SIZE,
    WALL_LETTER,
    SPACE_LETTER,
    MCGYVER_LETTER,
    OBJECT_LIST,
    GARDIAN_LETTER,
    MACGYVER,
    WINDOW_SIDE,
    WIN,
    LOST,
    BLUE,
    RED,
    YELLOW,
    GREEN,
    ORANGE
)


class Macgyver:
    """ Main character class, include moving methods and victory conditions. """
    def __init__(self, pos_x, pos_y, level):

        self.pos_x = pos_x
        self.pos_y = pos_y
        #  Macgyver direction images:
        self.right = pygame.image.load(find_data_file(MACGYVER)).convert_alpha()
        self.left = pygame.image.load(find_data_file(MACGYVER)).convert_alpha()
        self.up = pygame.image.load(find_data_file(MACGYVER)).convert_alpha()
        self.down = pygame.image.load(find_data_file(MACGYVER)).convert_alpha()
        #  Used to stock picked up objects:
        self.bucket = []
        #  Laby chosen by user
        self.level = level
        #  Boolean to know if game is over
        self.finish = False
        #  Boolean to know if game is won or not
        self.result = False

    @property
    def score(self):
        """ To win, bucket`attribute is used to count objects picked up by the main character.
            If main character has 3 objects he wins. """
        return len(self.bucket)

    def move(self, direction, structure_laby):
        """ Apply a movement based on input direction.
        Direction parameter is a string and define the direction wished by user.
        For each direction we could move main character to future location.
        If possible (see all conditions in apply_move method) """
        #Dict to match direction with future main character locations
        #Keys = direction, Values = position_future.
        condition_dict = {
            "d":{"position_future": (self.pos_x+1, self.pos_y),
            "is_out_laby": self.pos_x < (LABY_SIZE - 1)},
            "q":{"position_future": (self.pos_x-1, self.pos_y),
            "is_out_laby": self.pos_x > 0},
            "z":{"position_future": (self.pos_x, self.pos_y-1),
            "is_out_laby": self.pos_y > 0},
            "s":{"position_future": (self.pos_x, self.pos_y+1),
            "is_out_laby": self.pos_y < (LABY_SIZE - 1)}
            }

        if direction in condition_dict.keys():
            self.apply_move(direction,
                structure_laby,
                condition_dict[direction]["position_future"],
                condition_dict[direction]["is_out_laby"])

    def apply_move(self, direction, structure_laby, position_future, is_out_laby):
        if is_out_laby:
            """Apply movement if possible based on position_future parameter.
            Special condition: if position_future parameter is equal to GARDIAN_LETTER
            it means that the game is over and we can check
            if the main character won or not (see check_victory_or_defeat)"""
            if not structure_laby[position_future] == WALL_LETTER:
                #  take the object and look if the personage position match the object
                if structure_laby[position_future] in OBJECT_LIST:
                    self.stock_quest_item(structure_laby[position_future])
                # victory condition to end the game
                elif structure_laby[position_future] == GARDIAN_LETTER:
                    self.check_victory_or_defeat()
                #update Macgyver position
                structure_laby[position_future] = MCGYVER_LETTER
                structure_laby[(self.pos_x, self.pos_y)] = SPACE_LETTER
                self.pos_x = position_future[0]
                self.pos_y = position_future[1]

    def stock_quest_item(self, object_value):
        self.bucket.append(object_value)

    def check_victory_or_defeat(self):
        #check victory
        self.finish = True
        surface = pygame.display.set_mode((WINDOW_SIDE, WINDOW_SIDE))
        winner = pygame.image.load(find_data_file(WIN)).convert_alpha()
        looser = pygame.image.load(find_data_file(LOST)).convert_alpha()
        level_1 = "Press Enter for Level 1"
        level_2 = "Press Space for Level 2"
        quit_game = "Or Press Escape to QUIT"

        # if win
        if len(OBJECT_LIST) == len(self.bucket):

            self.result = True
            arial_font = pygame.font.SysFont("arial", 20, True)
            win_text_surface = arial_font.render("YOU WON'", False, GREEN)
            level_1_text_surface = arial_font.render(level_1, False, BLUE)
            level_2_text_surface = arial_font.render(level_2, False, ORANGE)
            quit_text_surface = arial_font.render(quit_game, False, RED)
            surface.blit(winner, (1, 1))
            surface.blit(win_text_surface, (150, 150))
            surface.blit(level_1_text_surface, (100, 170))
            surface.blit(level_2_text_surface, (100, 250))
            surface.blit(quit_text_surface, (100, 310))

        # if lost
        else:
            self.result = False
            arial_font = pygame.font.SysFont("arial", 20, True)
            lost_text_surface = arial_font.render("YOU LOOSE", False, YELLOW)
            level_1_text_surface = arial_font.render(level_1, False, BLUE)
            level_2_text_surface = arial_font.render(level_2, False, ORANGE)
            quit_text_surface = arial_font.render(quit_game, False, RED)
            surface.blit(looser, (1, 1))
            surface.blit(lost_text_surface, (150, 150))
            surface.blit(level_1_text_surface, (100, 170))
            surface.blit(level_2_text_surface, (100, 250))
            surface.blit(quit_text_surface, (100, 310))

        pygame.display.flip()