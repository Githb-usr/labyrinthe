# -*- coding: utf-8 -*-

import os
import csv

from config.configs import LANE_POINT, WALL_POINT, START_POINT, EXIT_POINT 
from .point import Point


class GameMap():
    '''
    Classe gérant le labyrinthe
    '''
    
    def __init__(self):
        self.name = 'Labyrinthe'
        self.lane = set() # Les points couloirs
        self.wall = set() # Les points murs
        self.start = set() # Le point de départ, occupé initialement par le héro
        self.exit = set() # Le point d'arrivée, occupé par le gardien
        
        
    def load_map_data(self, map_file):
        directory = os.path.dirname(__file__) # On prend le bon chemin
        path_to_file = os.path.join(directory, "..", "map", map_file) # On va dans le dossier "map" et on récupère le fichier.
       
        with open(path_to_file, newline='') as labycsv:
            reader = csv.reader(labycsv)
            y = 0
            for row in reader:
                x = 0
                while x < 15:
                    if row[x] == LANE_POINT:
                        self.lane.add(Point(x, y, 'LANE'))
                    elif row[x] == WALL_POINT:
                        self.wall.add(Point(x, y, 'WALL'))
                    elif row[x] == START_POINT:
                        self.start.add(Point(x, y, 'LANE'))
                    elif row[x] == EXIT_POINT:
                        self.exit.add(Point(x, y, 'LANE'))
                    else:
                        pass
                    x += 1
                y += 1
