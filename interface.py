# -*- coding: utf-8 -*-

import os
import sys

import pygame as pyg

from configs import CELL_SIZE, SCREEN_SIZE, MAP_SIZE, LANE_CELL, WALL_CELL, START_CELL, EXIT_CELL 
from map import Map
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
    path_to_file = os.path.join(directory, "img", img) # On va dans le dossier "maps" et on récupère le fichier image.
    cell_img = pyg.image.load(path_to_file).convert_alpha()
    
    return cell_img

def display_rect(cell_img, x, y):
    '''
    Création d'un objet rect
    '''  
    cell_img_rect = cell_img.get_rect(left=x, top=y)
    
    return cell_img_rect

def display_map(map):
    '''
    Affichage du fond du jeu
    ''' 
    wall_img = display_img('wall.png')
    for wa in map.wall:
        wall_rect = display_rect(wall_img, wa.position[0], wa.position[1])
        screen.blit(wall_img, wall_rect)
    
    lane_img = display_img('lane.png')
    for la in map.lane:
        lane_rect = display_rect(lane_img, la.position[0], la.position[1])
        screen.blit(lane_img, lane_rect)
    
    guard_img = display_img('guard.png')
    for ex in map.exit:
        guard_rect = display_rect(guard_img, ex.position[0], ex.position[1])
        screen.blit(guard_img, guard_rect)
    
    pyg.display.flip()
        
def display_items(map):
    '''
    Affichage des 3 items que doit récupérer le héros
    '''
    item1_img = display_img('item1.png')
    item2_img = display_img('item2.png')
    item3_img = display_img('item3.png')
    all_items_img = display_img('all_items.png')
    
    item1_rect = display_rect(item1_img, 0, 0)
    item2_rect = display_rect(item2_img, 0, 0)
    item3_rect = display_rect(item3_img, 0, 0)
    
    items_repr = [[item1_img, item1_rect], [item2_img, item2_rect], [item3_img, item3_rect]]

    i = 0
    while i < len(items_repr):
        for it in map.items_list:
            items_repr[i][1] = items_repr[i][1].move(it.position[0], it.position[1])
            screen.blit(items_repr[i][0], items_repr[i][1])
            pyg.display.update()
            i += 1
       
    return items_repr

def display_hero(hero):
    '''
    Affichage du héros
    '''
    hero_img = display_img('hero.png')
    hero_rect = display_rect(hero_img, hero.position[0], hero.position[1])
    screen.blit(hero_img, hero_rect)
    pyg.display.update()
    
    return hero_img, hero_rect

def collect_item(hero, items):
    '''
    Rammassage des items par le héros
    '''    
    for it in items:
        if hero.colliderect(it): # si le héro se place sur un item
            pass
            
def pyg_events(hero, map):
    '''
    Gestion des évènements Pygame
    '''
    df = map.create_dataframe()
    hero_pos = hero.position
    lane_img = display_img('lane.png')

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            sys.exit()
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_ESCAPE:
                raise SystemExit
            if event.key == pyg.K_LEFT:
                hero.move_left(df)
                screen.blit(lane_img, hero_pos)
            elif event.key == pyg.K_UP:           
                hero.move_up(df)
                screen.blit(lane_img, hero_pos)
            elif event.key == pyg.K_RIGHT:
                hero.move_right(df)
                screen.blit(lane_img, hero_pos)
            elif event.key == pyg.K_DOWN:
                hero.move_down(df)
                screen.blit(lane_img, hero_pos)
        
        hero.repr[1].move_ip(hero.position[0], hero.position[1])
        screen.blit(hero.repr[0], hero.repr[1])
