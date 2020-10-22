# -*- coding: utf-8 -*-

import os

from configs import CELL_SIZE


class Cell:
    '''
    Classe représentant la position de chacun des 225 éléments/cellules du jeu, fixes ou mobiles
    '''
    
    def __init__(self, x, y):
        self.position = (x*CELL_SIZE, y*CELL_SIZE)
        
    def __repr__(self):
        return str(self.position)
