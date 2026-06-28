# code/Level.py
from curses import COLOR_WHITE
import sys
from tkinter.font import Font

import pygame

from code.Const import C_WHITE, WIN_HEIGHT, WIN_WIDTH, C_RED # Importe WIN_WIDTH e C_RED (adicione C_RED = (255,0,0) no Const.py se não tiver)
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
        
        # Variáveis do desafio
        self.game_time = 120 * 60  # 2 minutos (120 seg) a 60 FPS
        self.spawn_timer = 0       # Cronômetro para nascer combustível

    def run(self):
        pygame.mixer_music.load('./asset/plane.ogg')  
        pygame.mixer_music.play(-1)  
        clock = pygame.time.Clock() 
        
        while True:
            clock.tick(60)
            self.window.fill((0, 0, 0)) 
            
            # Encontra o Player na lista
            player = next((ent for ent in self.entity_list if ent.name == 'Player'), None)
            
            # Lógica do Jogo
            if player:
                if not player.is_falling and self.game_time > 0:
                    self.game_time -= 1
                    player.fuel -= 1
                    self.spawn_timer += 1
                    
                    # Verifica se ficou sem combustível
                    if player.fuel <= 0:
                        player.fuel = 0
                        player.is_falling = True
                    
                    # Spawn de combustível a cada 5 segundos (300 frames)
                    if self.spawn_timer >= 5 * 60:
                        self.spawn_timer = 0
                        self.entity_list.append(EntityFactory.get_entity('Fuel'))
                
                # Colisão e limpeza (verificando a lista reversa ou copiando com [:])
                for ent in self.entity_list[:]:
                    if ent.name == 'Fuel':
                        # Se colidiu com jogador
                        if not player.is_falling and player.rect.colliderect(ent.rect):
                            player.fuel = player.max_fuel # Enche o tanque
                            self.entity_list.remove(ent)
                        # Se saiu da tela pela esquerda
                        elif ent.rect.right < 0:
                            self.entity_list.remove(ent)
            
            # Atualiza movimento e desenha todas as entidades
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # --- Textos UI Antigos ---
            self.level_text(20, f'fps: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(20, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))
            
            # --- Textos Novos: Relógio e Combustível ---
            # Tempo de jogo em minutos e segundos
            seconds_left = max(0, self.game_time // 60)
            mins = seconds_left // 60
            secs = seconds_left % 60
            self.level_text(25, f'{mins:02d}:{secs:02d}', C_WHITE, (WIN_WIDTH - 60, 20))
            
            if player:
                # Combustível em %
                fuel_pct = (player.fuel / player.max_fuel) * 100
                self.level_text(20, f'Combustivel: {fuel_pct:.0f}%', C_WHITE, (WIN_WIDTH - 90, 50))
                
                # Tela de Derrota
                if player.is_falling:
                    self.level_text(40, 'GAME OVER', (255, 0, 0), (WIN_WIDTH // 2, WIN_HEIGHT // 2))
                    if player.rect.top > WIN_HEIGHT: # Opcional: Se quiser fechar o jogo quando ele cair da tela
                        pass 
                
                # Tela de Vitória
                if self.game_time <= 0 and not player.is_falling:
                    self.level_text(40, 'VITORIA!', (0, 255, 0), (WIN_WIDTH // 2, WIN_HEIGHT // 2))
            
            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        # Modifiquei ligeiramente para usar 'text_center_pos' mas sem o centerx ser o ponto central absoluto nas margens para alinhar melhor se quiser depois.
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
        