#!/usr/bin/python3
# -*- coding: Utf-8 -*
LABY_SIZE = 15
WALL_LETTER = "X"
SPACE_LETTER = " "
MCGYVER_LETTER = "M"
OBJECT_LIST = ["E", "T", "N"]
GARDIAN_LETTER = "G"
NUMBER_SIDE_SPRITE = 15
SPRITE_SIDE = 30
WINDOW_SIDE = NUMBER_SIDE_SPRITE * SPRITE_SIDE
WINDOW_TITLE = "MACGYVER"

ICONE = "images/macgyver.jpg"
ETHER = "images/ether.jpg"
TUBE = "images/tube.jpg"
NEEDLE = "images/seringue.jpg"
MENU = "images/menu_macgyver.jpg"
BACKGROUND = "images/grass.jpg"
WALL = "images/mur.jpg"
GARDIAN = "images/gardien.jpg"
MACGYVER = "images/macgyver.jpg"
ITEMS = "images/items.png"

WIN = "images/win.png"
LOST = "images/lost.jpeg"

SCORE_1 = "images/1image.png"
SCORE_2 = "images/2image.png"
SCORE_3 = "images/3image.png"

BLUE = (0, 75, 255)
RED = (255, 0, 0)
YELLOW = (240, 236, 32)
GREEN = (32, 240, 38)
ORANGE = (250, 174, 31)

LABYRINTHS = {
    "laby1": [
        "M   XXXXXX   XX",
        "X    X  XX  XXX",
        "XXX  XX X   XXX",
        "X   XX    X  XX",
        "  X    XX X    ",
        "XX XXX X  XXXX ",
        "XX X    XXX  X ",
        "XX X XX    X XX",
        "     X XXX   XX",
        " XX XX       XX",
        " XX X XXX  X  X",
        "  X   X   XX  X",
        "X   X    X XX  ",
        "X XXX XX    X X",
        "  XXX  XX GX  X",
    ],
    "laby2": [
        "M  XXXX XX   XX",
        "X   XX  X X   X",
        "X X    XX  XX X",
        "  X XX    X X  ",
        " XXX   X XX  X ",
        "   X  XX XXX   ",
        " X X    XX X XX",
        "  XX XX    X   ",
        "X XX X X X   X ",
        "XX  XX      XX ",
        "XX XX XXX XX   ",
        "X     XX  X  X ",
        "  XXX    XX X  ",
        "X  X XX   X X X",
        "XX   X  X   X G",
    ]
}