#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import csv
import random

import numpy as np
import pandas as pd

from config.configs import CELL_SIZE, SCREEN_SIZE, MAP_SIZE, LANE_CELL, WALL_CELL, START_CELL, EXIT_CELL, ITEM_CELL
from models.cell import Cell
from models.item import Item


class Map:
    '''
    Class managing the labyrinth
    '''
    def __init__(self):
        self.name = 'Labyrinthe'
        self.matrix = [] # Matrix with all the letters representing each cell
        self.wall = set() # The wall cells
        self.lane = set() # Lane cells without Start and Exit
        self.start = set() # The starting cell, initially occupied by the hero
        self.exit = set() # The arrival cell, occupied by the guard
        self.items_list = set() # The random cells occupied by the 3 items to be retrieved by the hero
        self.all_cells = set() # All the cells of the game
        
    def load_map_data(self, map_file):
        """
        Data recovery from the maze
        :param map_file: the CSV file containing the structure of the maze
        """
        # We're going the right way
        directory = os.path.dirname(os.path.dirname(__file__))
        # We go to the "map" folder and retrieve the file.
        path_to_file = os.path.join(directory, ".\maps", map_file)
       
        with open(path_to_file, newline='') as labycsv:
            reader = csv.reader(labycsv)
            for row in reader:
                # We retrieve the structure of the maze in the matrix attribute
                self.matrix.append(row)
                
        # The cells corresponding to the structure of the labyrinth are created.
        self.cells_lists()

    def cells_lists(self):
        """
        Creating Cell objects from the structure of the maze
        """
        # A dataFrame is created to facilitate the browsing of the data.
        df = self.create_dataframe()
        y = 0
        # We run through the DataFrame and create each cell with the recovered coordinates.
        for y in df.index:                
            x = 0
            while x < len(df):
                if df[x][y] == WALL_CELL:
                    self.wall.add(Cell(x, y, WALL_CELL))
                elif df[x][y] == LANE_CELL:
                    self.lane.add(Cell(x, y, LANE_CELL))
                elif df[x][y] == START_CELL:
                    self.start.add(Cell(x, y, START_CELL))
                elif df[x][y] == EXIT_CELL:
                    self.exit.add(Cell(x, y, EXIT_CELL))
                else:
                    pass
                x += 1
            y += 1
        
        # We place the objects created in the all_cells attribute
        self.all_cells = self.all_cells.union(self.wall, self.lane, self.start, self.exit)

    def items_random_position(self):
        """
        Random positions are generated for the items to be collected by the hero.
        """
        # List of item image file names
        items_img = ['item1.png', 'item2.png','item3.png']
        # As an item can only be found in a lane, 3 lane cells are chosen at random.
        items_positions = random.sample(self.lane, k=3)
        for it in items_positions:
            # Each cell is assigned an image from the tems_img list.
            select_img = random.choice(items_img)
            # We create item objects and place them in the items_list attribute
            self.items_list.add(Item(int(it.position[0] / CELL_SIZE), int(it.position[1] / CELL_SIZE), select_img))
            # The assigned image is removed from the list to prevent it from being reassigned.
            items_img.remove(select_img)
        
        # We place the objects created in the all_cells attribute    
        self.all_cells = self.all_cells.union(self.items_list)

    def create_dataframe(self):
        """
        A DataFrame Pandas is created from the matrix attribute
        """
        matrix_np = np.array(self.matrix)
        matrix_df = pd.DataFrame(matrix_np)
        
        return matrix_df
