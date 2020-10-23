# -*- coding: utf-8 -*-

import os
import sys

from configs import CELL_SIZE


class Cell:
    '''
    Classe représentant la position de chacun des 225 éléments/cellules du jeu, fixes ou mobiles
    '''
    # sys.setrecursionlimit(10**6)
    # wall_count = 0
    # lane_count = 0
    # item_count = 0
    # guard_count = 0
    # hero_count = 0
    # total_count = 0
    
    def __init__(self, x, y, type_of_cell):
        self.position = (x*CELL_SIZE, y*CELL_SIZE)
        self.type_of_cell = type_of_cell
        
    def __repr__(self):
        return str(self.position)
    
    def get_position(self):
        return self.position
        
    def get_type(self):
        return self.type_of_cell
    
    def set_position(self, new_position):
        self.position = new_position
        
    def set_type(self, new_toc):
        self.type_of_cell = new_toc
    
    def delete(self):
        pass
    
    def compare(self, other_cell):
        position = other_cell.get_position()
        toc = other_cell.get_type()
        
        if (self.position == position) and (self.type_of_cell == toc):
            return True
        else:
            return False
        
    # properties
    # position = property(_get_position, _set_position)
    # type_of_cell = property(_get_type, _set_type)
