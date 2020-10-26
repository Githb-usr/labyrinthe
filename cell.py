# -*- coding: utf-8 -*-

import os
import sys

from configs import CELL_SIZE, LANE_CELLS


class Cell:
    '''
    Classe représentant la position de chacun des 225 éléments/cellules du jeu, fixes ou mobiles
    '''    
    def __init__(self, x, y, type_of_cell):
        self.position = (x*CELL_SIZE, y*CELL_SIZE)
        self.type_of_cell = type_of_cell
        
    def __repr__(self):
        return str((self.position, self.type_of_cell))
    
    def __eq__(self, other):
        if self.position == other.position and other.type_of_cell in LANE_CELLS:
            return True
    
    def __hash__(self):
        return hash((self.position, self.type_of_cell))
    
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
       
    # properties
    # position = property(_get_position, _set_position)
    # type_of_cell = property(_get_type, _set_type)
