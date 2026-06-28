import pygame

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity

class Background(Entity):
    # Constructor for the Background class, which inherits from Entity
    def __init__(self, name: str, position=(0, 0)):
        super().__init__(name=name, position=position)
        
        
    # Move the background to the left based on its speed defined in ENTITY_SPEED
    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
        
