# -*- coding: utf-8 -*-

import pygame

from cell import Cell
from configs import CELL_SIZE


class Hero(Cell):
    '''
    Classe gérant le héros du jeu
    '''
        
    def __init__(self, x, y, image, type_of_cell='LANE'):
        Cell.__init__(self, x, y, image, type_of_cell)
        self.name = 'MacGyver'
        # self.image = pygame.image.load("img/", image).convert_alpha()
        # self.position = self.image.get_rect().move(start_position)
            
    def move_up(self):
        if self.position[1] > 0:
            new_rect = self.rect.move_ip(0, -CELL_SIZE)
            self.position = (self.position[0], self.position[1] - CELL_SIZE)
        
            return new_rect
    
    def move_down(self):
        if self.position[1] < 700:
            new_rect = self.rect.move_ip(0, CELL_SIZE)
            self.position = (self.position[0], self.position[1] + CELL_SIZE)
            
            return new_rect
    
    def move_left(self):
        if self.position[0] > 0:
            new_rect = self.rect.move_ip(-CELL_SIZE, 0)
            self.position = (self.position[0] - CELL_SIZE, self.position[1])
        
            return new_rect
    
    def move_right(self):
        if self.position[0] < 700:
            new_rect = self.rect.move_ip(CELL_SIZE, 0)
            self.position = (self.position[0] + CELL_SIZE, self.position[1])
            
            return new_rect
