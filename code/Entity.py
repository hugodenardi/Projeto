from abc import ABC, abstractmethod

import pygame

# Entity class serves as a base class for all game entities (Player, Enemy, Background, Fuel, etc.)
class Entity(ABC):
    def __init__(self, name: str, position: tuple, size: tuple = None):
        self.name = name
        original_surf = pygame.image.load('./asset/' + name + '.png').convert_alpha() # Load the image for the entity and convert it for better performance
        if size:
            self.surf = pygame.transform.scale(original_surf, size) # Scale the image to the specified size if provided
        else:
            self.surf = original_surf
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
    
    # Abstract method to be implemented by subclasses for moving the entity
    @abstractmethod
    def move(self, ):
        pass