#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config.configs import CELL_SIZE, SCREEN_SIZE, MAP_SIZE, LANE_CELL, LANE_CELLS
from models.cell import Cell
from models.map import Map
import views.interface as interface


class Hero(Cell):
    '''
    Class managing the hero of the game
    '''
        
    def __init__(self, x, y, type_of_cell):
        Cell.__init__(self, x, y, type_of_cell)
        self.name = 'MacGyver'
        self.repr = interface.display_hero(self)

    def move_left(self, map):
        '''
        Changing the hero's position when moving to the left
        :param map: the map object (the maze), to access its attributes
        '''
        # The new position
        new_pos = (self.position[0] - CELL_SIZE, self.position[1])
        # The virtual new cell with the new position, which must be a lane
        new_cell = Cell(int(new_pos[0] / CELL_SIZE), int(new_pos[1] / CELL_SIZE), LANE_CELL)
        # List of all cells of the game
        cells = list(map.all_cells)
        
        # The hero is not allowed to leave the frame of the game.
        if self.position[0] > 0:
            # The new position must be a lane
            if new_cell in cells:
                for cell in cells:
                    # If we find a lane cell with the same position as the virtual cell, we check that there is not an item to pick up.
                    if cell.position == new_cell.position:
                        interface.collect_item(self, map.items_list)
                # We update the position of the hero
                self.position = new_pos
                return self.position
            else:
                # If it's not a lane, the hero doesn't move.
                return self.position
                        
    def move_up(self, map):
        '''
        Changing the hero's position when moving upwards
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
        Changing the position of the hero when moving to the right
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
        Changing the hero's position when moving downwards
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
