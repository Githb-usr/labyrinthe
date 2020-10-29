#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from config.configs import CELL_SIZE, LANE_CELLS


class Cell:
    '''
    Class representing the position of each of the elements/cells of the set, fixed or mobile.
    '''    
    def __init__(self, x, y, type_of_cell, image):
        self.position = (x*CELL_SIZE, y*CELL_SIZE)
        self.type_of_cell = type_of_cell
        self.image = image
        
    def __repr__(self):
        return str((self.position, self.type_of_cell))
    
    def __eq__(self, other):
        '''
        We compare 2 cells to see if they are equal.
        :param other: another Cell object
        '''
        if self.position == other.position and other.type_of_cell in LANE_CELLS:
            return True
    
    def __hash__(self):
        return hash((self.position, self.type_of_cell))
    
    def get_position(self):
        return self.position
    
    def set_position(self, new_position):
        self.position = new_position
        
    def get_type(self):
        return self.type_of_cell
        
    def set_type(self, new_toc):
        self.type_of_cell = new_toc
        
    def get_img(self):
            return self.image
    
    def set_img(self, new_img):
        self.position = new_img
    
    # properties
    # position = property(_get_position, _set_position)
    # type_of_cell = property(_get_type, _set_type)
