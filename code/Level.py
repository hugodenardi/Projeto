from curses import COLOR_WHITE
import sys
from tkinter.font import Font

import pygame

from code.Const import C_WHITE, WIN_HEIGHT
from code.Entity import Entity
from code.EntityFactory import EntityFactory

class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 3000
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        

    def run(self):
        pygame.mixer_music.load('./asset/plane.ogg')  # Carrega o arquivo de música
        pygame.mixer_music.play(-1)  # Reproduz em loop
        clock = pygame.time.Clock() # controle de FPS
        
        while True:
            # Controla a velocidade do jogo
            clock.tick(60)
            self.window.fill((0, 0, 0)) 
            
            
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.level_text(20, f'fps: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(20, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))
            self.level_text(20, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', C_WHITE, (10, 5))
            
            
            pygame.display.flip()
        pass
            
            

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
