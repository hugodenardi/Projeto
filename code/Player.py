# code/Player.py
import pygame

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position, size=(50, 50))
        self.max_fuel = 15 * 60 # 15 segundos (a 60 frames por segundo)
        self.fuel = self.max_fuel
        self.is_falling = False # Flag para quando o combustível acabar
        

    def move(self):
        # Se estiver sem combustível, o avião apenas cai
        if self.is_falling:
            self.rect.centery += 4 # Velocidade da queda
            return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if keys[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if keys[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
            