#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame as pyg

from config.configs import HERO_CELL, CELL_SIZE
from models.hero import Hero
from models.map import Map
import views.interface as interface


class Game:
    '''
    Game creation class
    '''
    
    def new_game(self):
        '''
        Setting up the elements of the game
        '''
        # We set up all the elements
        labyrinthe = Map()
        labyrinthe.load_map_data('map.csv')
        df = labyrinthe.create_dataframe()
        labyrinthe.items_random_position()
        start = list(labyrinthe.start)
        mcgyver = Hero(int(start[0].position[0]/CELL_SIZE), int(start[0].position[1]/CELL_SIZE), HERO_CELL)
        interface.display_map(labyrinthe)
        interface.display_items(labyrinthe)
        interface.display_text_zone1()
        
        # We bring the hero to life
        running = True        
        while running:
            interface.display_hero(mcgyver)
            interface.pyg_events(mcgyver, labyrinthe)
