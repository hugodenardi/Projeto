import pygame

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity

class Background(Entity):
    # Agora o construtor aceita o nome e a posição (com (0,0) como padrão)
    def __init__(self, name: str, position=(0, 0)):
        super().__init__(name=name, position=position)
        
        

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
        
