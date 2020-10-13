# -*- coding: utf-8 -*-

import pygame

from config.configs import CELL_SIZE


class Hero(pygame.sprite.Sprite):
    '''
    Classe gérant le héro du jeu
    '''
        
    def __init__(self):
        super().__init__()
        self.name = 'MacGyver'
        self.size = (32, 43)
        self.position = (1, 1)
        self.image = pygame.image.load("img/macgyver.png").convert()
        self.image = pygame.transform.scale(self.image, (CELL_SIZE, CELL_SIZE))
        self.rect = self.image.get_rect()
          
    def __repr__(self):
        return str(self.position)
        
    def update(self):
        pass
    
    def move_up(self):
        return self.rect.move_ip(0, -CELL_SIZE)
    
    def move_down(self):
        return self.rect.move_ip(0, CELL_SIZE)
    
    def move_left(self):
        return self.rect.move_ip(-CELL_SIZE, 0)
    
    def move_right(self):
        return self.rect.move_ip(CELL_SIZE, 0)
