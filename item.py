# -*- coding: utf-8 -*-

from cell import Cell
from configs import ITEM_CELL


class Item(Cell):
    '''
    Classe gérant le héros du jeu
    '''
        
    def __init__(self, x, y, img, type_of_cell=ITEM_CELL):
        Cell.__init__(self, x, y, type_of_cell)
        self.image = img
