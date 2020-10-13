# -*- coding: utf-8 -*-

import sys
import os

import pygame
import pandas as pd

LANE_POINT = 'c'
WALL_POINT = '#'
START_POINT = 'S'
EXIT_POINT = 'E'


class Point():
    '''
    Classe représentant la position de chacun des 225 éléments du jeu, fixes ou mobiles
    '''
    
    def __init__(self, x, y, type_of_point):
        self.x = x
        self.y = y
        self.position = (x, y)
        self.type_of_point = type_of_point
            
    def __repr__(self):
        return str(self.position)
    
    def move_up(self):
        if self.type == 'Hero':
            return Point(self.x-1, self.y)
    
    def move_down(self):
        if self.type == 'Hero':
            return Point(self.x+1, self.y)
    
    def move_left(self):
        if self.type == 'Hero':
            return Point(self.x, self.y-1)
    
    def move_right(self):
        if self.type == 'Hero':
            return Point(self.x, self.y+1)

   
class GameMap():
    '''
    Classe gérant le labyrinthe
    '''
    
    def __init__(self):
        self.name = 'Labyrinthe'
        self.lane = set() # Les points couloirs
        self.wall = set() # Les points murs
        self.start = set() # Le point de départ, occupé initialement par le héro
        self.exit = set() # Le point d'arrivée, occupé par le gardien
        
        
    def load_map_data(self, map_file):
        directory = os.path.dirname(__file__) # On prend le bon chemin
        path_to_file = os.path.join(directory, "map", map_file) # On va dans le dossier "map" et on récupère le fichier.
        dataframe_index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        map_dataframe = pd.read_csv(path_to_file, sep=",")
        
        # for row in map_dataframe.iterrows():
        #     x = row[0]
        #     char = row[1]
        # i = 0
        # while i < 15:
        #     for row in map_dataframe.iterrows():
        #         x = row[0]
        #         y = i
        #         char = row[1][1]
        #         i = i + 1
        #         print('La position de {} est ({}, {})'.format(char, x, y))
      

            #point = 
        # with open(path_to_file, 'r') as laby:
        #     for x, line in enumerate(laby):
        #         for y, col in enumerate(line):
        #             if col == LANE_POINT:
        #                 self.lane.add(Point(x, y, 'Lane'))
        #             elif col == WALL_POINT:
        #                 self.wall.add(Point(x, y, 'Wall'))
        #             elif col == START_POINT:
        #                 self.start.add(Point(x, y, 'Lane'))
        #             elif col == EXIT_POINT:
        #                 self.exit.add(Point(x, y, 'Lane'))
        #             else:
        #                 pass
        
        return map_dataframe
                 
                          
class Hero():
    '''
    Classe gérant le héro du jeu
    '''
        
    def __init__(self):
        self.name = 'MacGyver'
        self.position = ()
        
    def move_hero_up(self):
        pass
    
    def move_hero_down(self):
        pass
    
    def move_hero_left(self):
        pass

    def move_hero_right(self):
        pass      
    
    
def draw_screen():
    
    pygame.display.init()
    screen_size = (750, 750)
    screen = pygame.display.set_mode(screen_size)
    size = width, height = 32, 43
    speed = [2, 2]
    black = 0, 0, 0
    clock = pygame.time.Clock()
    FPS = 60  # Frames per second.
    pygame.display.set_caption("Aidez MacGyver à s'échapper du labyrinthe !")
    
    laby_lane = pygame.image.load("img/lane.png").convert()
    laby_wall = pygame.image.load("img/MacGyver.png").convert()
    laby_guard = pygame.image.load("img/gardien.png").convert()
    laby_item1 = pygame.image.load("img/tube.png").convert()
    laby_item2 = pygame.image.load("img/aiguille.png").convert()
    laby_item3 = pygame.image.load("img/ether.png").convert()
    laby_item_complete = pygame.image.load("img/seringue.png").convert()
    
    mcgyver = pygame.image.load("img/macgyver.png").convert() # Charger l'image de MacGyver à partir d'un fichier
    mcgyverrect = mcgyver.get_rect()
    
    while 1:
        laby_map = GameMap()
        laby_map_data = laby_map.load_map_data('map.csv')
        # for point in laby_map_data.lane:
        #     screen.blit(laby_wall, point.position)
        
        for event in pygame.event.get():
            if event == pygame.QUIT:
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    raise SystemExit
                elif event.key == pygame.K_UP:
                    mcgyverrect = mcgyverrect.move(speed)
                    if mcgyverrect.left < 0 or mcgyverrect.right > width:
                        speed[0] = -speed[0]
                    if mcgyverrect.top < 0 or mcgyverrect.bottom > height:
                        speed[1] = -speed[1]
                    print("Player moved up!")
                elif event.key == pygame.K_LEFT:
                    print("Player moved left!")
                elif event.key == pygame.K_DOWN:
                    mcgyverrect = mcgyverrect.move(speed)
                    if mcgyverrect.left < 0 or mcgyverrect.right > width:
                        speed[0] = -speed[0]
                    if mcgyverrect.top < 0 or mcgyverrect.bottom > height:
                        speed[1] = -speed[1]
                    print("Player moved down!")
                elif event.key == pygame.K_RIGHT:
                    print("Player moved right!")
        #screen.blit(mcgyver, (50,100)) # Ajouter l'image de MacGyver sur l'écran
        screen.fill(black)
        screen.blit(mcgyver, mcgyverrect)
        pygame.display.flip() # Actualisation pour afficher l'image


# Garder la fenêtre de jeu ouverte
if __name__ == "__main__":
    draw_screen()