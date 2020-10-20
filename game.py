# -*- coding: utf-8 -*-

import interface
from hero import Hero
from game_map import GameMap


class Game:
    '''
    Classe créant le jeu
    '''
    
    def draw_laby(self):
        '''
        Mise en place des éléments du jeu
        '''
        labyrinthe = GameMap()
        labyrinthe.load_map_data('map.csv')
        map_df = labyrinthe.create_dataframe()
        labyrinthe.items_random_position()
        hero = Hero(labyrinthe.start[0][0], labyrinthe.start[0][1])
        
        running = True        
        while running:
            interface.display_map(labyrinthe, map_df)
            interface.display_items(labyrinthe)
            interface.display_hero(hero)
            interface.pyg_events(hero, labyrinthe)
