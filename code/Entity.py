from abc import ABC, abstractmethod

import pygame


class Entity(ABC):
    def __init__(self, name: str, position: tuple, size: tuple = None):
        self.name = name
        original_surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        if size:
            self.surf = pygame.transform.scale(original_surf, size)
        else:
            self.surf = original_surf
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod

    def move(self, ):
        pass