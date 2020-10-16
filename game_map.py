# -*- coding: utf-8 -*-

import os
import csv

import pygame

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
        self.lane = [] # Les cellules couloirs
        self.wall = [] # Les cellules murs
        self.start = [] # La cellule de départ, occupé initialement par le héro
        self.exit = [] # La cellule d'arrivée, occupé par le gardien
        self.lane_img = pygame.image.load("img/lane.png").convert_alpha()
        self.lane_pos = self.lane_img.get_rect()
        self.wall_img = pygame.image.load("img/wall.png").convert_alpha()
        self.wall_pos = self.wall_img.get_rect()
        self.guard_img = pygame.image.load("img/gardien.png").convert_alpha()
        self.guard_pos = self.guard_img.get_rect()
        self.item1_img = pygame.image.load("img/tube.png").convert_alpha()
        self.item1_post = self.item1_img.get_rect()
        self.item2_img = pygame.image.load("img/aiguille.png").convert_alpha()
        self.item2_pos = self.item2_img.get_rect()
        self.item3_img = pygame.image.load("img/ether.png").convert_alpha()
        self.item3_pos = self.item3_img.get_rect()
        self.item_complete_img = pygame.image.load("img/seringue.png").convert_alpha()
        self.item_complete_pos = self.item_complete_img.get_rect()
        
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
                x = 0
                while x < 15:
                    if row[x] == LANE_CELL:
                        self.lane.append((x, y, 'LANE'))
                    elif row[x] == WALL_CELL:
                        self.wall.append((x, y, 'WALL'))
                    elif row[x] == START_CELL:
                        self.start.append((x, y, 'LANE'))
                        self.lane.append((x, y, 'LANE'))
                    elif row[x] == EXIT_CELL:
                        self.exit.append((x, y, 'LANE'))
                        self.lane.append((x, y, 'LANE'))
                    else:
                        pass
                    x += 1
                y += 1
