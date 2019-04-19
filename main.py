# Importing modules
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, K_RIGHT, K_DOWN, K_LEFT, K_UP
# -tc- Eviter les imports utilisant l'étoile! Ce n'est pas conforme à la PEP8
from maze.constants import *
from maze.class_game.maze import Maze
from maze.class_game.hero import Hero
from maze.class_game.position import Position

# -tc- Essayer de mettre tous ce code dans une classe

# Pygame initialization
pygame.init()

# Loading resources :

# 1- Creating the Window
# -tc- Les constantes devraient être nommées en majuscules
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
# -tc- Tu as vraiment besoin de plusieurs sprites de mur? Si oui, utilise une
# -tc- liste de longueur 10 plutôt que 10 variables wall0 à wall10
# -tc- Attention, les lignes ne doivent pas dépasser 80 caractères
wall0 = pygame.transform.scale(
    pygame.image.load(structure_wall).convert().subsurface(40, 20, 20, 20),
    (30, 30)
)
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

# Create the hero
mg = Hero(level)

# Variable that define which object is caught or not
# -tc- Pourquoi ne pas avoir un attribut dans la classe Hero qui indique les 
# -tc- objet ramassé. Utilise une liste plutôt que des variables séparées.
tube_catch = False
ether_catch = False
needle_catch = False
inventory_objects = 0

# Variable that continues the loop if = 1, stops if = 0
# -tc- Plutôt utiliser True que 1, ça documente l'intention d'utiliser une
# -tc- logique booléenne
main_loop = 1

# Main loop
while main_loop:

    # Loop Speed Limitation
    pygame.time.Clock().tick(30)

    # Display maze in window
    # -tc- Ca fait beaucoup d'argument à passer à display. Utiliser une liste
    # -tc- sera plus pratique et fera plus de sens.
    level.display(window, wall0, wall1, wall2, wall3, wall4, wall5,
                  wall6, wall7, wall8, wall9, needle, tube, ether)
    window.blit(start, level.start.position)
    window.blit(end, level.end.position)
    window.blit(keeper, level.end.position)

    for event in pygame.event.get():  # We track the list of all the events received
        # If user quit the program stop or if the user presses a ESCAPE key
        # -tc- Utiliser des parenthèses pour clarifier
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            # -tc- main_loop = False ferait plus de sens que 0
            main_loop = 0

        # -tc- utiliser elif plutôt que if à chaque fois
        if event.type == KEYDOWN:
            # If the key is right
            if event.key == K_RIGHT:
                # -tc- Mettre la logique de déplacement dans une méthode move
                # -tc- dans la classe Hero
                p = mg.position.right()
                if level.is_path_position(p):
                    mg.position = mg.position.right()

            # If the key is lefl
            # -tc- elif!
            if event.key == K_LEFT:
                p = mg.position.left()
                if level.is_path_position(p):
                    mg.position = mg.position.left()

            # If the key is up
            # -tc- elif!
            if event.key == K_UP:
                p = mg.position.up()
                if level.is_path_position(p):
                    mg.position = mg.position.up()

            # If the key is down
            # -tc- elif!
            if event.key == K_DOWN:
                p = mg.position.down()
                if level.is_path_position(p):
                    mg.position = mg.position.down()
                    print(mg.position)

    # Display new positions
    # -tc- A quoi sert ce rectangle?
    pygame.draw.rect(window, (0, 0, 0), (0, 0, 450, 450))
    # -tc- Tu as déjà affiché le plateau de jeu en début de boucle.
    # -tc- Tu ne dois le faire que une fois par boucle
    level.display(window, wall0, wall1, wall2, wall3, wall4, wall5,
                  wall6, wall7, wall8, wall9, needle, tube, ether)
    # -tc- Ces affichages ont déjà été fais en début de boucle
    window.blit(start, level.start.position)
    window.blit(end, level.end.position)
    window.blit(keeper, level.end.position)
    window.blit(hero, mg.position.position)
    print(mg.position.position)
    pygame.display.flip()

