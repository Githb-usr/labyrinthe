#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import pygame as pyg

from config.configs import CELL_SIZE, SCREEN_SIZE, MAP_SIZE, BACKGROUND, LANE_CELL, WALL_CELL, START_CELL, EXIT_CELL, ITEM_TXTPOS1, ITEM_TXTPOS2, ITEM_TXTPOS3, ITEM_TXTPOS, ALL_ITEMS_POS
import models.cell
import models.hero
import models.map

pyg.display.init()
pyg.font.init()
# Setting fonts
font = pyg.font.SysFont('calibri', 17, bold=True)
font_small = pyg.font.SysFont('calibri', 15, bold=True)
font_big = pyg.font.SysFont('calibri', 32, bold=True)
screen = pyg.display.set_mode(SCREEN_SIZE)
screen.fill(BACKGROUND)
clock = pyg.time.Clock()
FPS = 60  # Frames per second.
pyg.display.set_caption("Aidez MacGyver à s'échapper du labyrinthe !")

def display_img(img):
    '''
    Display of each image of the game
    :param img: file name of the image to be imported
    :type img: JPG, PNG
    '''
    # We're going the right way
    directory = os.path.dirname(os.path.dirname(__file__))
    # We go to the "maps" folder and retrieve the image file.
    path_to_file = os.path.join(directory, "img", img)
    # We import the image, while preserving any transparency
    cell_img = pyg.image.load(path_to_file).convert_alpha()
    
    return cell_img

def display_rect(cell_img, x, y):
    '''
    Creating a rect object
    :param cell_img: imported image
    :param x: x-position of the rect
    :param y: y-position of the rect
    :type x: int
    :type y: int
    '''  
    cell_img_rect = cell_img.get_rect(left=x, top=y)
    
    return cell_img_rect

def display_map(map):
    '''
    Game background display
    :param map: the map object (the maze), to access its attributes
    ''' 
    # We import the images
    wall_img = display_img('wall.png')
    lane_img = display_img('lane.png')
    guard_img = display_img('guard.png')
    
    # The map is displayed from the position and type of each cell.
    for cell in map.all_cells:
        if cell.type_of_cell == WALL_CELL:
            wall_rect = display_rect(wall_img, cell.position[0], cell.position[1])
            screen.blit(wall_img, wall_rect)
        # The departure and arrival cells are also lanes.
        elif cell.type_of_cell == LANE_CELL or cell.type_of_cell == START_CELL or cell.type_of_cell == EXIT_CELL:
            lane_rect = display_rect(lane_img, cell.position[0], cell.position[1])
            screen.blit(lane_img, lane_rect)
            # We display the guard
            if cell.type_of_cell == EXIT_CELL:
                guard_rect = display_rect(guard_img, cell.position[0], cell.position[1])
                screen.blit(guard_img, guard_rect)
            
    pyg.display.flip()
        
def display_items(map):
    '''
    Display of the items that the hero must retrieve
    :param map: the map object (the maze), to access its attributes
    '''
    # The representation of the items (image and rect) is created.
    items_repr = []
    for it in map.items_list:
        item_img = display_img(it.image)
        item_rect = display_rect(item_img, 0, 0)
        items_repr.append([item_img, item_rect])
        
    i = 0
    while i < len(items_repr):
        # Items are displayed according to the position of the cells.
        for it in map.items_list:
            items_repr[i][1] = items_repr[i][1].move(it.position[0], it.position[1])
            screen.blit(items_repr[i][0], items_repr[i][1])
            pyg.display.update()
            i += 1
       
    return items_repr

def display_hero(hero):
    '''
    Hero display
    :param hero: hero object, to access its attributes
    '''
    hero_img = display_img('hero.png')
    hero_rect = display_rect(hero_img, hero.position[0], hero.position[1])
    screen.blit(hero_img, hero_rect)
    pyg.display.update()
    
    return hero_img, hero_rect

def collect_item(hero, items):
    '''
    Pick-up of items by hero
    :param hero: hero object, to access its attributes
    :param items: corresponds to the map.items_list attribute 
    '''
    # List of item positions in zone 1
    items_textpos = [ITEM_TXTPOS1, ITEM_TXTPOS2, ITEM_TXTPOS3]
    for it in items:
        # If the hero is on an item, the item changes position according to its image (it goes from the map to zone 1).
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
    # We check if we have all the items, in order to display zone 2 if necessary. 
    display_text_zone2(items)
    
    pyg.display.update()
    
def check_all_items(items):
    '''
    Display of text field 2 (all items have been picked up)
    :param items: corresponds to the map.items_list attribute
    '''    
    # The positions of all the items are retrieved
    items_pos = []
    for it in items:
        items_pos.append(it.position)
    
    items_pos.sort()
    ITEM_TXTPOS.sort()
    if items_pos == ITEM_TXTPOS:
        return True
    else:
        return False
    
def display_text_zone1():
    '''
    Display of text field 1 (list of collected items)
    '''
    # Display of permanent texts
    text = font.render('Récupérez tous les objets !', False, (0, 0, 0))
    screen.blit(text, (25, 770))
    text = font.render('Ils apparaitront ci-dessous :', False, (0, 0, 0))
    screen.blit(text, (25, 790))
    # Display of items, if picked up
    text = font_small.render('Tube', False, (0, 0, 0))
    screen.blit(text, (32, 860))
    text = font_small.render('Aiguille', False, (0, 0, 0))
    screen.blit(text, (107, 860)) 
    text = font_small.render('Ether', False, (0, 0, 0))
    screen.blit(text, (182, 860))
    pyg.display.update()

def display_text_zone2(items):
    '''
    Display of text field 2 (all items have been picked up)
    :param items: corresponds to the map.items_list attribute
    '''

    # If all the items are in zone 1, then zone 2 is displayed.
    if check_all_items(items) == True:
        text = font.render("Bravo, vous avez réconstitué la seringue !", False, (0, 0, 0))
        screen.blit(text, (290, 770))
        text = font.render("Vous pouvez vous présenter devant le garde et l'endormir.", False, (0, 0, 0))
        screen.blit(text, (290, 790))
        syringe_img = display_img('all_items.png')
        syringe_rect = display_rect(syringe_img, ALL_ITEMS_POS[0], ALL_ITEMS_POS[1])
        screen.blit(syringe_img, syringe_rect)
    
    pyg.display.update()
    
def display_text_zone3(items):
    '''
    Display of text field 3 (Game won or lost)
    '''
    if check_all_items(items) == True:
        text = font_big.render('Bravo, vous avez gagné ! :o)', False, (22, 184, 78))
        text_rect = text.get_rect(center=(SCREEN_SIZE[0]/2, 925))
        screen.blit(text, text_rect)
    else:
        text = font_big.render('Oh non, vous avez perdu ! :(', False, (255, 0, 0))
        text_rect = text.get_rect(center=(SCREEN_SIZE[0]/2, 925))
        screen.blit(text, text_rect)        
            
def pyg_events(hero, map):
    '''
    Event management Pygame
    :param hero: hero object, to access its attributes
    :param map: map object, to pass it to a method
    '''
    hero_pos = hero.position
    lane_img = display_img('lane.png')
    keys = pyg.key.get_pressed()
    
    for event in pyg.event.get():
        # The game is closed with the cross in the window.
        if event.type == pyg.QUIT:
            pyg.quit()
            sys.exit()
        # The game is closed with the 'Escape' button on the keyboard.
        if keys[pyg.K_ESCAPE]:
            raise SystemExit
        if keys[pyg.K_LEFT]:
            # We change the position of the hero
            hero.move_left(map)
            # The image of the hero in his former position is erased.
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
        # The image of the hero is displayed in his new position.
        screen.blit(hero.repr[0], hero.repr[1])
