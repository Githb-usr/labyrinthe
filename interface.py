# -*- coding: utf-8 -*-

import os
import sys

import pygame as pyg

from configs import CELL_SIZE, SCREEN_SIZE, MAP_SIZE, BACKGROUND, LANE_CELL, WALL_CELL, START_CELL, EXIT_CELL, ITEM_TXTPOS1, ITEM_TXTPOS2, ITEM_TXTPOS3, ITEM_TXTPOS, ALL_ITEMS_POS
from map import Map
from hero import Hero
from cell import Cell

pyg.display.init()
screen = pyg.display.set_mode(SCREEN_SIZE)
screen.fill(BACKGROUND)
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
    lane_img = display_img('lane.png')    
    guard_img = display_img('guard.png')
    
    for cell in map.all_cells:
        if cell.type_of_cell == WALL_CELL:
            wall_rect = display_rect(wall_img, cell.position[0], cell.position[1])
            screen.blit(wall_img, wall_rect)
        elif cell.type_of_cell == LANE_CELL or cell.type_of_cell == START_CELL or cell.type_of_cell == EXIT_CELL:
            lane_rect = display_rect(lane_img, cell.position[0], cell.position[1])
            screen.blit(lane_img, lane_rect)        
            if cell.type_of_cell == EXIT_CELL:
                guard_rect = display_rect(guard_img, cell.position[0], cell.position[1])
                screen.blit(guard_img, guard_rect)            
            
    pyg.display.flip()
        
def display_items(map):
    '''
    Affichage des 3 items que doit récupérer le héros
    '''
    items_repr = []
    for it in map.items_list:
        item_img = display_img(it.image)
        item_rect = display_rect(item_img, 0, 0)
        items_repr.append([item_img, item_rect])
        
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
    items_textpos = [ITEM_TXTPOS1, ITEM_TXTPOS2, ITEM_TXTPOS3]
    for it in items:
        if (hero.position == it.position):
            if it.image == 'item1.png':
                it.position = items_textpos[0]
            elif it.image == 'item2.png':
                it.position = items_textpos[1]
            elif it.image == 'item3.png':
                it.position = items_textpos[2]
            image = display_img(it.image)
            pos = display_rect(image, it.position[0], it.position[1])
            screen.blit(image, pos)
    display_text_zone2(items)
    
    pyg.display.update()

def display_text_zone1(map):
    pyg.font.init()
    font = pyg.font.SysFont('calibri', 17, bold=True)
    font_small = pyg.font.SysFont('calibri', 15, bold=True)
    font_big = pyg.font.SysFont('cambria', 18, bold=True)
    text_surface = font.render('Récupérez tous les objets !', False, (0, 0, 0))
    screen.blit(text_surface, (25, 770))
    text_surface = font.render('Ils apparaitront ci-dessous :', False, (0, 0, 0))
    screen.blit(text_surface, (25, 790))
    text_surface = font_small.render('Tube', False, (0, 0, 0))
    screen.blit(text_surface, (32, 860))
    text_surface = font_small.render('Aiguille', False, (0, 0, 0))
    screen.blit(text_surface, (107, 860)) 
    text_surface = font_small.render('Ether', False, (0, 0, 0))
    screen.blit(text_surface, (182, 860))
    pyg.display.update()

def display_text_zone2(items):
    pyg.font.init()
    font = pyg.font.SysFont('calibri', 17, bold=True)
    font_small = pyg.font.SysFont('calibri', 15, bold=True)
    font_big = pyg.font.SysFont('cambria', 18, bold=True)
    items_pos = []
    for it in items:
        items_pos.append(it.position)
    
    items_pos.sort()
    ITEM_TXTPOS.sort()
    if items_pos == ITEM_TXTPOS:
        text_surface = font.render('Bravo, vous avez réconstitué la seringue !', False, (0, 0, 0))
        screen.blit(text_surface, (290, 770))
        text_surface = font.render('Vous pouvez vous présenter devant le gardien.', False, (0, 0, 0))
        screen.blit(text_surface, (290, 790))
        syringe_img = display_img('all_items.png')
        syringe_rect = display_rect(syringe_img, ALL_ITEMS_POS[0], ALL_ITEMS_POS[1])
        screen.blit(syringe_img, syringe_rect)
    
    pyg.display.update()
         
def pyg_events(hero, map):
    '''
    Gestion des évènements Pygame
    '''
    hero_pos = hero.position
    lane_img = display_img('lane.png')
    keys = pyg.key.get_pressed()
    
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit()
            sys.exit()
        if keys[pyg.K_ESCAPE]:
            raise SystemExit
        if keys[pyg.K_LEFT]:
            hero.move_left(map)
            screen.blit(lane_img, hero_pos)
        elif keys[pyg.K_UP]:
            hero.move_up(map)
            screen.blit(lane_img, hero_pos)
        elif keys[pyg.K_RIGHT]:
            hero.move_right(map)
            screen.blit(lane_img, hero_pos)
        elif keys[pyg.K_DOWN]:
            hero.move_down(map)
            screen.blit(lane_img, hero_pos)
        
        hero.repr[1].move_ip(hero.position[0], hero.position[1])
        screen.blit(hero.repr[0], hero.repr[1])
