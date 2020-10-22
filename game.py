# -*- coding: utf-8 -*-

import interface
from hero import Hero
from map import Map
from configs import HERO_CELL


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
        print(labyrinthe.start)
        # map_df = labyrinthe.create_dataframe()
        # labyrinthe.items_random_position()
        # mcgyver = Hero(labyrinthe.start[0].position[0], labyrinthe.start[0].position[1], HERO_CELL)
        # print(mcgyver.position)
        
        running = True        
        while running:
            interface.display_map(labyrinthe)
            # interface.display_items(labyrinthe)
            # interface.display_hero(mcgyver)
            # interface.pyg_events(mcgyver, labyrinthe)
