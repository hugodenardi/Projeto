# code/Fuel.py
import pygame
from code.Const import ENTITY_SPEED, WIN_WIDTH
from code.Entity import Entity

class Fuel(Entity):
    def __init__(self, name: str, position: tuple):
        # Set the size of the fuel entity to 30x30 pixels
        super().__init__(name, position, size=(30, 30))

    def move(self):
        # Move the fuel to the left
        self.rect.centerx -= ENTITY_SPEED[self.name]
        