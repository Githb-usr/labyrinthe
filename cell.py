# -*- coding: utf-8 -*-


class Cell:
    '''
    Classe représentant la position de chacun des 225 éléments du jeu, fixes ou mobiles
    '''
    
    def __init__(self, x, y, type_of_cell):
        self.x = x
        self.y = y
        self.position = (x, y)
        self.type_of_cell = type_of_cell
        
    def __repr__(self):
        return str(self.position)
