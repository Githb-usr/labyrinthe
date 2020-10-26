# -*- coding: utf-8 -*-

import os
import csv
import random

import numpy as np
import pandas as pd

from configs import CELL_SIZE, SCREEN_SIZE, MAP_SIZE, LANE_CELL, WALL_CELL, START_CELL, EXIT_CELL, ITEM_CELL
from cell import Cell
from item import Item


class Map:
    '''
    Classe gérant le labyrinthe
    '''
    
    def __init__(self):
        """
        Constructeur
        """
        self.name = 'Labyrinthe'
        self.matrix = [] # matrice avec tous les lettres représentant chaque cellule
        self.wall = set() # Les cellules murs
        self.lane = set() # Les cellules couloirs sans Start et Exit
        self.start = set() # La cellule de départ, occupé initialement par le héro
        self.exit = set() # La cellule d'arrivée, occupé par le gardien
        self.items_list = set() # Les cellules aléatoires occupées par les 3 items à récupérer par le héros
        self.all_cells = set()
        
    def load_map_data(self, map_file):
        """
        Récupération des données du labyrinthe
        :map_file
        """
        directory = os.path.dirname(__file__) # On prend le bon chemin
        path_to_file = os.path.join(directory, "maps", map_file) # On va dans le dossier "map" et on récupère le fichier.
       
        with open(path_to_file, newline='') as labycsv:
            reader = csv.reader(labycsv)                
            for row in reader:
                self.matrix.append(row)
                
        self.cells_lists()

    def cells_lists(self):
        """
        xxx
        """
        df = self.create_dataframe()
        y = 0
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
        
        self.all_cells = self.all_cells.union(self.wall, self.lane, self.start, self.exit)

    def items_random_position(self):
        """
        On génère des positions élatoires pour les 3 items que doit récupérer le héros
        """
        items_img = ['item1.png', 'item2.png','item3.png']
        items_positions = random.sample(self.lane, k=3)
        for it in items_positions:
            select_img = random.choice(items_img)
            self.items_list.add(Item(int(it.position[0] / CELL_SIZE), int(it.position[1] / CELL_SIZE), select_img))
            items_img.remove(select_img)
            
        self.all_cells = self.all_cells.union(self.items_list)

    def create_dataframe(self):
        """
        On créé un DataFrame Pandas
        """
        matrix_np = np.array(self.matrix)
        matrix_df = pd.DataFrame(matrix_np)
        
        return matrix_df
