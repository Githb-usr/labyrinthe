# -*- coding: utf-8 -*-

import sys

import pygame

from hero import Hero
from cell import Cell
from game_map import GameMap
from configs import SCREEN_SIZE, CELL_SIZE, BLACK, LANE_CELL, WALL_CELL, START_CELL, EXIT_CELL


class Game:
    '''
    Classe créant le jeu
    '''
    
    def draw_screen(self):
        
        pygame.display.init()
        screen = pygame.display.set_mode(SCREEN_SIZE)
        clock = pygame.time.Clock()
        FPS = 60  # Frames per second.
        pygame.display.set_caption("Aidez MacGyver à s'échapper du labyrinthe !")
                    
        labyrinthe = GameMap()
        labyrinthe.load_map_data('map.csv')
        for s in labyrinthe.start:
            mg = Hero(s[0], s[1], 'macgyver.png')
            print(mg.rect[0])
        for e in labyrinthe.exit:
            guard_pos = (e[0]*50, e[1]*50)
        running = True
        
        while running:
            for event in pygame.event.get():
                for w in labyrinthe.wall:
                    screen.blit(labyrinthe.wall_img, labyrinthe.wall_pos.move((w[0]*50, w[1]*50)))
                for l in labyrinthe.lane:
                    screen.blit(labyrinthe.lane_img, labyrinthe.lane_pos.move((l[0]*50, l[1]*50)))
                if event == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        raise SystemExit
                    if event.key == pygame.K_LEFT:
                        mg.move_left()
                    elif event.key == pygame.K_UP:           
                        mg.move_up()
                    elif event.key == pygame.K_RIGHT:
                        mg.move_right()
                    elif event.key == pygame.K_DOWN:
                        mg.move_down()
                        
            screen.blit(mg.cell_img, mg.rect)
            screen.blit(labyrinthe.guard_img, guard_pos)
            pygame.display.flip() # Actualisation pour afficher l'image
