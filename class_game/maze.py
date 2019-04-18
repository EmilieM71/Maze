from class_game.position import Position
from constants import *
from random import sample


class Maze:

    def __init__(self, filename):
        self.filename = filename
        self.start = []
        self.end = []
        self.paths = []
        self.wall0 = []
        self.wall1 = []
        self.wall2 = []
        self.wall3 = []
        self.wall4 = []
        self.wall5 = []
        self.wall6 = []
        self.wall7 = []
        self.wall8 = []
        self.wall9 = []
        self.objects_to_find = []

    def is_path_position(self, position):
        return position in self.paths

    def load_from_file(self):
        """Fonction qui permet de charger la carte du labyrinthe"""
        with open(self.filename) as infile:
            for x, line in enumerate(infile):
                for y, c in enumerate(line):
                    if c == path_char:
                        self.paths.append(Position(y * size_sprite, x * size_sprite))
                    elif c == start_char:
                        self.start.append(Position(y * size_sprite, x * size_sprite))
                        self.paths.append(Position(y * size_sprite, x * size_sprite))
                    elif c == end_char:
                        self.end.append(Position(y * size_sprite, x * size_sprite))
                        self.paths.append(Position(y * size_sprite, x * size_sprite))
                    elif c == '0':
                        self.wall0.append(Position(y * size_sprite, x * size_sprite))
                    elif c == '1':
                        self.wall1.append(Position(y * size_sprite, x * size_sprite))
                    elif c == '2':
                        self.wall2.append(Position(y * size_sprite, x * size_sprite))
                    elif c == '3':
                        self.wall3.append(Position(y * size_sprite, x * size_sprite))
                    elif c == '4':
                        self.wall4.append(Position(y * size_sprite, x * size_sprite))
                    elif c == '5':
                        self.wall5.append(Position(y * size_sprite, x * size_sprite))
                    elif c == '6':
                        self.wall6.append(Position(y * size_sprite, x * size_sprite))
                    elif c == '7':
                        self.wall7.append(Position(y * size_sprite, x * size_sprite))
                    elif c == '8':
                        self.wall8.append(Position(y * size_sprite, x * size_sprite))
                    elif c == '9':
                        self.wall9.append(Position(y * size_sprite, x * size_sprite))
        self.objects_to_find = sample(self.paths, 3)

        return self.paths and self.wall0 and self.wall1 and self.wall2 and self.wall3 and self.wall4 and self.wall5 and self.wall6 and self.wall7 and self.wall8 and self.wall9 and self.objects_to_find and self.start and self.end

    def display(self, window_name, start_name, end_name, keeper_name, wall0_name, wall1_name, wall2_name, wall3_name,
                wall4_name, wall5_name, wall6_name, wall7_name, wall8_name, wall9_name, needle_name, tube_name,
                ether_name):
        for position in self.start:
            window_name.blit(start_name, position.position)
        for position in self.end:
            window_name.blit(end_name, position.position)
            window_name.blit(keeper_name, position.position)
        for position in self.wall0:
            window_name.blit(wall0_name, position.position)
        for position in self.wall1:
            window_name.blit(wall1_name, position.position)
        for position in self.wall2:
            window_name.blit(wall2_name, position.position)
        for position in self.wall3:
            window_name.blit(wall3_name, position.position)
        for position in self.wall4:
            window_name.blit(wall4_name, position.position)
        for position in self.wall5:
            window_name.blit(wall5_name, position.position)
        for position in self.wall6:
            window_name.blit(wall6_name, position.position)
        for position in self.wall7:
            window_name.blit(wall7_name, position.position)
        for position in self.wall8:
            window_name.blit(wall8_name, position.position)
        for position in self.wall9:
            window_name.blit(wall9_name, position.position)
        objects = [needle_name, tube_name, ether_name]
        x = 0
        for position in self.objects_to_find:
            window_name.blit(objects[x], position.position)
            x += 1


def main():
    level = Maze("level/level1")

    p = Position(0, 0).right().right().down()
    print(level.is_path_position(p))


if __name__ == "__main__":
    main()
