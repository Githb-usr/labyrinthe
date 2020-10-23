# -*- coding: utf-8 -*-

import pygame as pyg

import interface
from hero import Hero
from map import Map
from configs import SCREEN_SIZE, HERO_CELL, CELL_SIZE


class Game:
    '''
    Classe créant le jeu
    '''
    
    def new_game(self):
        '''
        Mise en place des éléments du jeu
        '''
        labyrinthe = Map()
        labyrinthe.load_map_data('map.csv')
        labyrinthe.items_random_position()
        mcgyver = Hero(int(labyrinthe.start[0].position[0]/CELL_SIZE), int(labyrinthe.start[0].position[1]/CELL_SIZE), HERO_CELL)
        interface.display_map(labyrinthe)
        interface.display_items(labyrinthe)
        
        running = True        
        while running:
            interface.display_hero(mcgyver)
            interface.pyg_events(mcgyver, labyrinthe)
