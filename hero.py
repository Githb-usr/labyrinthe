# -*- coding: utf-8 -*-

import pygame

from configs import CELL_SIZE


class Hero:
    '''
    Classe gérant le héros du jeu
    '''
        
    def __init__(self):
        super().__init__()
        self.name = 'MacGyver'
        self.image = pygame.image.load("img/macgyver.png").convert_alpha()
        self.pos = self.image.get_rect().move(50, 50)
          
    def __repr__(self):
        return str(self.position)
        
    def update(self):
        pass
    
    def move_up(self):
        return self.pos.move_ip(0, -CELL_SIZE)
    
    def move_down(self):
        return self.pos.move_ip(0, CELL_SIZE)
    
    def move_left(self):
        return self.pos.move_ip(-CELL_SIZE, 0)
    
    def move_right(self):
        return self.pos.move_ip(CELL_SIZE, 0)
