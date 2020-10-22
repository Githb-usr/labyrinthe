# -*- coding: utf-8 -*-

import os
import csv
import random

import numpy as np
import pandas as pd

from configs import SCREEN_SIZE, LANE_CELL, WALL_CELL, START_CELL, EXIT_CELL 
from cell import Cell


class GameMap:
    '''
    Classe gérant le labyrinthe
    '''
    
    def __init__(self):
        """
        Constructeur
        """
        self.name = 'Labyrinthe'
        self.matrix = [] # matrice avec tous les lettres représentant chaque cellule
        self.lane = [] # Les cellules couloirs sans Start et Exit
        self.start = [] # La cellule de départ, occupé initialement par le héro
        self.exit = [] # La cellule d'arrivée, occupé par le gardien
        self.items_list = [] # Les cellules occupées par les 32 items à récupérer par le héros
        
    def load_map_data(self, map_file):
        """
        Récupération des données du labyrinthe
        """
        directory = os.path.dirname(__file__) # On prend le bon chemin
        path_to_file = os.path.join(directory, "map", map_file) # On va dans le dossier "map" et on récupère le fichier.
       
        with open(path_to_file, newline='') as labycsv:
            reader = csv.reader(labycsv)                
            y = 0
            for row in reader:
                self.matrix.append(row)
                    
                x = 0
                while x < 15:
                    if row[x] == LANE_CELL:
                        self.lane.append((x, y, LANE_CELL))
                    elif row[x] == START_CELL:
                        self.start.append((x, y, LANE_CELL))
                    elif row[x] == EXIT_CELL:
                        self.exit.append((x, y, LANE_CELL))
                    else:
                        pass
                    x += 1
                y += 1

    def items_random_position(self):
        """
        On génère des positions élatoires pour les 3 items que doit récupérer le héros
        """
        items_positions = random.sample(self.lane, k=3)
        for it in items_positions:
            self.items_list.append(it)

    def create_dataframe(self):
        """
        On créé un DataFrame Pandas
        """
        matrix_np = np.array(self.matrix)
        matrix_df = pd.DataFrame(matrix_np)
        
        return matrix_df
