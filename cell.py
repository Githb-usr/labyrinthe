# -*- coding: utf-8 -*-

import os

import pygame

from configs import CELL_SIZE 


class Cell:
    '''
    Classe représentant la position de chacun des 225 éléments du jeu, fixes ou mobiles
    '''
    
    def __init__(self, x, y, image, type_of_cell):
        directory = os.path.dirname(__file__) # On prend le bon chemin
        path_to_file = os.path.join(directory, "img", image) # On va dans le dossier "map" et on récupère le fichier.
        # self.surface = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.cell_img = pygame.image.load(path_to_file).convert_alpha()
        self.position = (x*CELL_SIZE, y*CELL_SIZE)
        self.rect = self.cell_img.get_rect().move(self.position)
        self.type_of_cell = type_of_cell
        
    def __repr__(self):
        return str(self.position)
