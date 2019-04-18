# Importing modules
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
from constants import *
from class_game.maze import Maze


# Pygame initialization
pygame.init()

# Loading resources :

# 1- Creating the Window
window = pygame.display.set_mode((cote_screen_game, cote_screen_game))

# 2- Window icon
icon = pygame.image.load(image_icon)
pygame.display.set_icon(icon)

# 3- Window title
pygame.display.set_caption(title_window)

# Load image for game (crop and resizing)
start = pygame.transform.scale((pygame.image.load(floor_tiles)).subsurface(160, 20, 20, 20), (30, 30))
end = pygame.transform.scale((pygame.image.load(floor_tiles)).subsurface(220, 20, 20, 20), (30, 30))
path = pygame.transform.scale(pygame.image.load(floor_tiles).convert().subsurface(60, 60, 20, 20), (30, 30))
wall0 = pygame.transform.scale(pygame.image.load(structure_wall).convert().subsurface(40, 20, 20, 20), (30, 30))
wall1 = pygame.transform.scale(pygame.image.load(structure_wall).convert().subsurface(20, 40, 20, 20), (30, 30))
wall2 = pygame.transform.scale(pygame.image.load(structure_wall).convert().subsurface(20, 20, 20, 20), (30, 30))
wall3 = pygame.transform.scale(pygame.image.load(structure_wall).convert().subsurface(20, 80, 20, 20), (30, 30))
wall4 = pygame.transform.scale(pygame.image.load(structure_wall).convert().subsurface(80, 20, 20, 20), (30, 30))
wall5 = pygame.transform.scale(pygame.image.load(structure_wall).convert().subsurface(80, 80, 20, 20), (30, 30))
wall6 = pygame.transform.scale(pygame.image.load(structure_wall).convert().subsurface(210, 0, 20, 20), (30, 30))
wall7 = pygame.transform.scale(pygame.image.load(structure_wall).convert().subsurface(210, 20, 20, 20), (30, 30))
wall8 = pygame.transform.scale(pygame.image.load(structure_wall).convert().subsurface(220, 10, 20, 20), (30, 30))
wall9 = pygame.transform.scale(pygame.image.load(structure_wall).convert().subsurface(200, 10, 20, 20), (30, 30))
hero = pygame.transform.scale(pygame.image.load(hero_source).convert_alpha().subsurface(0, 0, 32, 32), (30, 30))
keeper = pygame.transform.scale(pygame.image.load(keeper_image).convert_alpha(), (25, 25))
needle = pygame.transform.scale(pygame.image.load(needle_image).convert(), (23, 30))
tube = pygame.transform.scale(pygame.image.load(tube_image).convert_alpha(), (30, 23))
ether = pygame.transform.scale(pygame.image.load(ether_image).convert(), (30, 30))
syringe = pygame.transform.scale(pygame.image.load(syringe_image).convert_alpha(), (30, 30))

# Create maze
level = Maze("level/level1")
level.load_from_file()
position_hero = level.start
position_guardian = level.end

# Variable that continues the loop if = 1, stops if = 0
main_loop = 1

# Main loop
while main_loop:
    for event in pygame.event.get():  # We track the list of all the events received
        # If user quit the program stop or if the user presses a ESCAPE key
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            main_loop = 0

    level.display(window, start, end, keeper, wall0, wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9,
                  needle, tube, ether)

    pygame.display.flip()

