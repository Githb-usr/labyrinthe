# -*- coding: utf-8 -*-


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
