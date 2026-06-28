# code/Fuel.py
import pygame
from code.Const import ENTITY_SPEED, WIN_WIDTH
from code.Entity import Entity

class Fuel(Entity):
    def __init__(self, name: str, position: tuple):
        # Defina um tamanho para o ícone, ajustando o (30, 30) se necessário
        super().__init__(name, position, size=(30, 30))

    def move(self):
        # Move o combustível para a esquerda
        self.rect.centerx -= ENTITY_SPEED[self.name]
        