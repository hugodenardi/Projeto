import pygame

from code.Const import ENTITY_SPEED
from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        # Maintain proportion based on original sizes:
        # Enemy1: 660x404 -> aspect ratio ~1.63
        # Enemy2: 1149x701 -> aspect ratio ~1.64
        # Target height = 50 (same as player). Target width = 50 * 1.64 = ~82
        super().__init__(name, position, size=(82, 50))
        
        # Flip the image horizontally (x-axis) so it faces left
        self.surf = pygame.transform.flip(self.surf, True, False)

    def move(self):
        # Move the enemy from right to left
        self.rect.centerx -= ENTITY_SPEED[self.name]
        