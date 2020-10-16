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
        
        mg = Hero()
        labyrinthe = GameMap()
        labyrinthe.load_map_data('map.csv')
        running = True
        
        while running:
            for event in pygame.event.get():
                for w in labyrinthe.wall:
                    print(w[0])
                    screen.blit(labyrinthe.wall_img, labyrinthe.wall_pos.move(w[0], w[1]))
                if event == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        raise SystemExit
                    if event.key == pygame.K_LEFT:
                        mg.move_left()
                        screen.blit(mg.image, mg.pos, mg.pos)
                    elif event.key == pygame.K_UP:
                        mg.move_up()
                        screen.blit(mg.image, mg.pos, mg.pos)
                    elif event.key == pygame.K_RIGHT:
                        mg.move_right()
                        screen.blit(mg.image, mg.pos, mg.pos)
                    elif event.key == pygame.K_DOWN:
                        mg.move_down()
                        screen.blit(mg.image, mg.pos, mg.pos)
            # print(labyrinthe.wall)
            # screen.fill(BLACK)
            
            screen.blit(mg.image, mg.pos)
            pygame.display.flip() # Actualisation pour afficher l'image
