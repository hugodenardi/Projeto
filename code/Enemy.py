import pygame

from code.Const import ENTITY_SPEED
from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        # Apply the same 50x50 size conversion as the Player
        super().__init__(name, position, size=(50, 50))
        
        # Flip the image horizontally (x-axis) so it faces left
        self.surf = pygame.transform.flip(self.surf, True, False)

    def move(self):
        # Move the enemy from right to left
        self.rect.centerx -= ENTITY_SPEED[self.name]
        