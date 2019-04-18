# Importing modules
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
from constants import *


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

# Variable that continues the loop if = 1, stops if = 0
main_loop = 1

# Main loop
while main_loop:
    for event in pygame.event.get():  # We track the list of all the events received
        # If user quit the program stop or if the user presses a ESCAPE key
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            main_loop = 0