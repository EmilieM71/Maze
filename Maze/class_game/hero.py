class Hero:

    def __init__(self, maze):
        self.maze = maze
        self.position = self.maze.start

    def move(self, direction):
        """Déplacer le personnage"""
        new_position = getattr(self.position, direction)()
        if new_position in self.maze:
            self.position = new_position
