# -*- coding: utf-8 -*-

from cell import Cell
from game_map import GameMap as gmap
import interface
from configs import CELL_SIZE, SCREEN_SIZE


class Hero(Cell):
    '''
    Classe gérant le héros du jeu
    '''
        
    def __init__(self, x, y):
        Cell.__init__(self, x, y)
        self.name = 'MacGyver'
        self.repr = interface.display_hero(self)
            
    def move_up(self, df):
        '''
        Changement de position du héros lors d'un déplacement vers le haut
        '''
        new_pos = (self.position[0], self.position[1] - CELL_SIZE)
        if self.position[1] > 0:
            df_pos = df.iat[int(new_pos[1]/CELL_SIZE), int(new_pos[0]/CELL_SIZE)]
            if df_pos == 'L' or df_pos == 'S':
                self.position = new_pos
                return self.position
            elif df_pos == 'W':
                return self.position
    
    def move_down(self, df):
        '''
        Changement de position du héros lors d'un déplacement vers le bas
        '''
        new_pos = (self.position[0], self.position[1] + CELL_SIZE)
        if self.position[1] < SCREEN_SIZE[1] - CELL_SIZE:
            df_pos = df.iat[int(new_pos[1]/CELL_SIZE), int(new_pos[0]/CELL_SIZE)]
            if df_pos == 'L' or df_pos == 'S':
                self.position = new_pos
                return self.position
            elif df_pos == 'W':
                return self.position
    
    def move_left(self, df):
        '''
        Changement de position du héros lors d'un déplacement vers la gauche
        '''
        new_pos = (self.position[0] - CELL_SIZE, self.position[1])
        if self.position[0] > 0:
            df_pos = df.iat[int(new_pos[1]/CELL_SIZE), int(new_pos[0]/CELL_SIZE)]
            if df_pos == 'L' or df_pos == 'S':
                self.position = new_pos
                return self.position
            elif df_pos == 'W':
                return self.position
    
    def move_right(self, df):
        '''
        Changement de position du héros lors d'un déplacement vers la droite
        '''
        new_pos = (self.position[0] + CELL_SIZE, self.position[1])
        if self.position[0] < SCREEN_SIZE[0] - CELL_SIZE:
            df_pos = df.iat[int(new_pos[1]/CELL_SIZE), int(new_pos[0]/CELL_SIZE)]
            if df_pos == 'L' or df_pos == 'S':
                self.position = new_pos
                return self.position
            elif df_pos == 'W':
                return self.position
