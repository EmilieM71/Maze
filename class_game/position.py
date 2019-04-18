class Position:
    """Classe définissant une position caractérisée par :
    - son abscisse en x
    - son ordonnée en y
    le point supérieur gauche ayant pour position x=0 et y=0"""

    # méthode constructeur
    def __init__(self, x, y):
        self.position = (x, y)  # Définition de l'attribut position en x et y

    # méthode modifiant l'affiché l'objet quand on l'appelle
    def __repr__(self):
        return str(self.position)

    # Hash d'un nombre
    def __hash__(self):
        return hash(self.position)

    # Comparateur d'égalité pour 2 positions
    def __eq__(self, pos):
        return self.position == pos.position

    # Méthode qui retourne une position
    def up(self):
        x, y = self.position
        return Position(x, y-1)

    def down(self):
        x, y = self.position
        return Position(x, y+1)

    def right(self):
        x, y = self.position
        return Position(x+1, y)

    def left(self):
        x, y = self.position
        return Position(x-1, y)
