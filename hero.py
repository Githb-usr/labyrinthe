# -*- coding: utf-8 -*-

from cell import Cell
from map import Map
import interface
from configs import CELL_SIZE, SCREEN_SIZE, MAP_SIZE, LANE_CELL, LANE_CELLS


class Hero(Cell):
    '''
    Classe gérant le héros du jeu
    '''
        
    def __init__(self, x, y, type_of_cell):
        Cell.__init__(self, x, y, type_of_cell)
        self.name = 'MacGyver'
        self.repr = interface.display_hero(self)

    def move_left(self, map):
        '''
        Changement de position du héros lors d'un déplacement vers la gauche
        '''
        new_pos = (self.position[0] - CELL_SIZE, self.position[1])
        new_cell = Cell(int(new_pos[0] / CELL_SIZE), int(new_pos[1] / CELL_SIZE), LANE_CELL)
        cells = list(map.all_cells)
        if self.position[0] > 0:
            if new_cell in cells:
                for cell in cells:
                    if cell.position == new_cell.position:
                        interface.collect_item(self, map.items_list)
                self.position = new_pos
                return self.position
            else:
                return self.position
                        
    def move_up(self, map):
        '''
        Changement de position du héros lors d'un déplacement vers le haut
        '''
        new_pos = (self.position[0], self.position[1] - CELL_SIZE)
        new_cell = Cell(int(new_pos[0] / CELL_SIZE), int(new_pos[1] / CELL_SIZE), LANE_CELL)
        cells = list(map.all_cells)
        if self.position[1] > 0:
            if new_cell in cells:
                for cell in cells:
                    if cell.position == new_cell.position:
                        interface.collect_item(self, map.items_list)
                self.position = new_pos
                return self.position
            else:
                return self.position

    def move_right(self, map):
        '''
        Changement de position du héros lors d'un déplacement vers la droite
        '''
        new_pos = (self.position[0] + CELL_SIZE, self.position[1])
        new_cell = Cell(int(new_pos[0] / CELL_SIZE), int(new_pos[1] / CELL_SIZE), LANE_CELL)
        cells = list(map.all_cells)
        if self.position[0] < MAP_SIZE[0] - CELL_SIZE:
            if new_cell in cells:
                for cell in cells:
                    if cell.position == new_cell.position:
                        interface.collect_item(self, map.items_list)
                self.position = new_pos
                return self.position
            else:
                return self.position
                
    def move_down(self, map):
        '''
        Changement de position du héros lors d'un déplacement vers le bas
        '''
        new_pos = (self.position[0], self.position[1] + CELL_SIZE)
        new_cell = Cell(int(new_pos[0] / CELL_SIZE), int(new_pos[1] / CELL_SIZE), LANE_CELL)
        cells = list(map.all_cells)
        if self.position[1] < MAP_SIZE[1] - CELL_SIZE:
            if new_cell in cells:
                for cell in cells:
                    if cell.position == new_cell.position:
                        interface.collect_item(self, map.items_list)
                self.position = new_pos
                return self.position
            else:
                return self.position
