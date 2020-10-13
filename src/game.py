# -*- coding: utf-8 -*-

import pygame

from src import Hero, Point, GameMap
from config.configs import SCREEN_SIZE, CELL_SIZE, BLACK, LANE_POINT, WALL_POINT, START_POINT, EXIT_POINT


class Game():
    '''
    Classe créant le jeu
    '''
    
    def draw_screen(self):
        
        pygame.display.init()
        screen = pygame.display.set_mode(SCREEN_SIZE)
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
        
        mg = Hero()
        labyrinthe = GameMap()
        labyrinthe.load_map_data('map.csv')
        running = True
        
        while running:
            for event in pygame.event.get():
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
                        
            screen.fill(BLACK)
            screen.blit(mg.image, mg.rect)
            pygame.display.flip() # Actualisation pour afficher l'image
