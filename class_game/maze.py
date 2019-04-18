from class_game.position import Position
from constants import *
from random import sample


class Map:

    def __init__(self, filename):
        self.filename = filename
        self.paths = []

    def is_path_position(self, position):
        return position in self.paths

    def load_from_file(self):
        """Fonction qui permet de charger la carte du labyrinthe"""
        start = []
        end = []
        wall = []
        structure = []
        with open(self.filename) as infile:
            for x, line in enumerate(infile):
                for y, c in enumerate(line):
                    if c == path_char:
                        self.paths.append(Position(x, y))
                    elif c == start_char:
                        start.append(Position(x, y))
                        self.paths.append(Position(x, y))
                    elif c == end_char:
                        end.append(Position(x, y))
                        self.paths.append(Position(x, y))
                    elif c == wall_char:
                        wall.append(Position(x, y))
        objects_to_find = sample(self.paths, 3)
        print(objects_to_find)
        structure.append(start)
        structure.append(end)
        structure.append(self.paths)
        structure.append(wall)

        print(structure)
        return structure




def main():
    level = Map("level1")

    p = Position(0, 0).right().right().down()
    print(level.is_path_position(p))


if __name__ == "__main__":
    main()
