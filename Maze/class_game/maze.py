from Maze.class_game.position import Position
from Maze.constants import *
from random import sample


class Maze:

    def __init__(self, filename):
        self.filename = filename
        self.start = ()
        self.end = ()
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
                        self.start = Position(y * size_sprite, x * size_sprite)
                        self.paths.append(Position(y * size_sprite, x * size_sprite))
                    elif c == end_char:
                        self.end = Position(y * size_sprite, x * size_sprite)
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
        print(self.paths)

        return self.paths and self.wall0 and self.wall1 and self.wall2 and self.wall3 and self.wall4 and self.wall5 and self.wall6 and self.wall7 and self.wall8 and self.wall9 and self.objects_to_find and self.start and self.end

    def display(self, window_name, wall0_name, wall1_name, wall2_name, wall3_name,
                wall4_name, wall5_name, wall6_name, wall7_name, wall8_name, wall9_name, needle_name, tube_name,
                ether_name):

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
    level = Maze("Maze/level/level1")
    level.load_from_file()
    # [(0, 0), (30, 0), (60, 0), (120, 0), (150, 0), (180, 0), (210, 0), (240, 0), (300, 0), (330, 0), (360, 0),
    # (390, 0), (60, 30), (120, 30), (300, 30), (390, 30), (0, 60), (30, 60), (60, 60), (90, 60), (120, 60), (180, 60),
    # (210, 60), (240, 60), (300, 60), (360, 60), (390, 60), (0, 90), (120, 90), (180, 90), (240, 90), (270, 90),
    # (300, 90), (360, 90), (60, 120), (90, 120), (120, 120), (180, 120), (360, 120), (390, 120), (420, 120), (0, 150),
    # (60, 150), (180, 150), (240, 150), (270, 150), (300, 150), (420, 150), (0, 180), (60, 180), (90, 180), (120, 180),
    # (150, 180), (180, 180), (240, 180), (300, 180), (330, 180), (360, 180), (390, 180), (420, 180), (0, 210),
    # (30, 210), (60, 210), (120, 210), (240, 210), (390, 210), (120, 240), (180, 240), (210, 240), (240, 240),
    # (270, 240), (330, 240), (390, 240), (30, 270), (60, 270), (90, 270), (120, 270), (180, 270), (270, 270),
    # (330, 270), (360, 270), (390, 270), (30, 300), (120, 300), (180, 300), (210, 300), (270, 300), (390, 300),
    # (420, 300), (30, 330), (60, 330), (90, 330), (120, 330), (210, 330), (270, 330), (300, 330), (330, 330),
    # (420, 330), (180, 360), (210, 360), (330, 360), (360, 360), (390, 360), (0, 390), (30, 390), (60, 390), (90, 390),
    # (120, 390), (180, 390), (240, 390), (270, 390), (300, 390), (330, 390), (390, 390), (420, 390), (0, 420),
    # (120, 420), (150, 420), (180, 420), (240, 420), (420, 420)]
    p = Position(0, 0).right()
    print(p)
    print(level.is_path_position(p))


if __name__ == "__main__":
    main()
