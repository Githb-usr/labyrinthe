# -*- coding: utf-8 -*-

import os
import sys

import pygame as pyg
import numpy as np
import pandas as pd

from configs import CELL_SIZE, SCREEN_SIZE, LANE_CELL, WALL_CELL, START_CELL, EXIT_CELL 
from game_map import GameMap
from hero import Hero
from cell import Cell

pyg.display.init()
screen = pyg.display.set_mode(SCREEN_SIZE)
clock = pyg.time.Clock()
FPS = 60  # Frames per second.
pyg.display.set_caption("Aidez MacGyver à s'échapper du labyrinthe !")

def display_img(img):
    '''
    Affichage de chaque image du jeu
    '''
    directory = os.path.dirname(__file__) # On prend le bon chemin
    path_to_file = os.path.join(directory, "img", img) # On va dans le dossier "map" et on récupère le fichier.
    cell_img = pyg.image.load(path_to_file).convert_alpha()
    
    return cell_img

def display_rect(cell_img):
    '''
    Création d'un objet rect
    '''  
    cell_img_rect = cell_img.get_rect()
    
    return cell_img_rect

def display_map(map, map_df):
    '''
    Affichage du fond du jeu
    ''' 
    wall_img = display_img('wall.png')
    lane_img = display_img('lane.png')
    guard_img = display_img('guard.png')
    
    for i in range(len(map_df)):
        j = 0
        while j < 15:
            if map_df.iloc[j][i] == 'W':
                Cell(i, j)
                wall_rect = display_rect(wall_img).move(i*CELL_SIZE, j*CELL_SIZE)
                screen.blit(wall_img, wall_rect)
                j += 1
            elif map_df.iloc[j][i] == 'L' or map_df.iloc[j][i] == 'S':
                lane_rect = display_rect(lane_img).move(i*CELL_SIZE, j*CELL_SIZE)
                screen.blit(lane_img, lane_rect)
                j += 1
            elif map_df.iloc[j][i] == 'E':
                guard_rect = display_rect(guard_img).move(i*CELL_SIZE, j*CELL_SIZE)
                screen.blit(guard_img, guard_rect)
                j += 1
    
def display_items(map):
    '''
    Affichage des 3 items que doit récupérer le héros
    '''
    item1_img = display_img('item1.png')
    item2_img = display_img('item2.png')
    item3_img = display_img('item3.png')
    all_items_img = display_img('all_items.png')
    
    item1_rect = display_rect(item1_img)
    item2_rect = display_rect(item2_img)
    item3_rect = display_rect(item3_img)
    
    items_repr = [[item1_img, item1_rect], [item2_img, item2_rect], [item3_img, item3_rect]]

    i = 0
    while i < len(items_repr):
        for it in map.items_list:
            items_repr[i][1] = items_repr[i][1].move(it[0]*CELL_SIZE, it[1]*CELL_SIZE)
            screen.blit(items_repr[i][0], items_repr[i][1])
            i += 1

def display_hero(hero):
    '''
    Affichage du héros
    '''
    hero_img = display_img('hero.png')
    hero_rect = display_rect(hero_img)
    hero_view = hero_rect.move(hero.position[0], hero.position[1])
    screen.blit(hero_img, hero_view)
    pyg.display.flip()
    
    return hero_img, hero_rect
            
def pyg_events(hero, gmap):
    '''
    Gestion des évènements Pygame
    '''
    df = gmap.create_dataframe()
    for event in pyg.event.get():
        if event == pyg.QUIT:
            pyg.quit()
            sys.exit()
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_ESCAPE:
                raise SystemExit
            if event.key == pyg.K_LEFT:
                hero.move_left(df)
            elif event.key == pyg.K_UP:           
                hero.move_up(df)
            elif event.key == pyg.K_RIGHT:
                hero.move_right(df)
            elif event.key == pyg.K_DOWN:
                hero.move_down(df)
        
        hero.repr[1].move_ip(hero.position[0], hero.position[1])
        screen.blit(hero.repr[0], hero.repr[1])
