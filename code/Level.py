# code/Level.py
import sys
import math
import random
import pygame
from tkinter.font import Font

from code.Const import C_WHITE, C_YELLOW, C_RED, C_BLACK, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity
from code.EntityFactory import EntityFactory

class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.reset_level() 

    def reset_level(self):
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        
        # 1 minute timer (60 seconds * 60 FPS)
        self.game_time = 60 * 60  
        self.spawn_timer = 0       
        self.enemy_spawn_timer = 0

        self.item_sound = pygame.mixer.Sound('./asset/item.wav')
        
        self.game_over = False
        self.victory = False
        self.menu_option = 0 
        
        pygame.mixer_music.load('./asset/plane.ogg')  
        pygame.mixer_music.play(-1)  

    def run(self):
        clock = pygame.time.Clock() 
        
        while True:
            clock.tick(60)
            self.window.fill((0, 0, 0)) 
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if self.game_over or self.victory:
                        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                            self.menu_option = 1 if self.menu_option == 0 else 0 
                        if event.key == pygame.K_RETURN:
                            if self.menu_option == 0:
                                self.reset_level() 
                            elif self.menu_option == 1:
                                pygame.mixer_music.stop()
                                return # Returns to the main menu instead of closing the game window

            # Fetch the player entity after the event loop to ensure a fresh reference if reset_level was triggered
            player = next((ent for ent in self.entity_list if ent.name == 'Player'), None)

            if player and not (self.game_over or self.victory):
                if not player.is_falling and self.game_time > 0:
                    self.game_time -= 1
                    player.fuel -= 1
                    self.spawn_timer += 1
                    self.enemy_spawn_timer += 1
                    
                    if player.fuel <= 0:
                        player.fuel = 0
                        player.is_falling = True
                        pygame.mixer_music.stop() 
                    
                    # Spawn fuel every 3 seconds (180 frames)
                    if self.spawn_timer >= 3 * 60:
                        self.spawn_timer = 0
                        self.entity_list.append(EntityFactory.get_entity('Fuel'))

                    # Spawn enemies randomly between 1 and 2.5 seconds
                    if self.enemy_spawn_timer >= random.randint(60, 150):
                        self.enemy_spawn_timer = 0
                        enemy_type = random.choice(['Enemy1', 'Enemy2'])
                        self.entity_list.append(EntityFactory.get_entity(enemy_type))
                
                for ent in self.entity_list[:]:
                    if ent.name == 'Fuel':
                        if not player.is_falling and player.rect.colliderect(ent.rect):
                            player.fuel = player.max_fuel 
                            self.item_sound.play()
                            self.entity_list.remove(ent)
                        elif ent.rect.right < 0:
                            self.entity_list.remove(ent)

                    elif ent.name in ['Enemy1', 'Enemy2']:
                        player_hitbox = player.rect.inflate(-20, -20)
                        enemy_hitbox = ent.rect.inflate(-20, -20)
                        
                        if not player.is_falling and player_hitbox.colliderect(enemy_hitbox):
                            player.is_falling = True
                            player.fuel = 0 
                            pygame.mixer_music.stop()
                        elif ent.rect.right < 0:
                            self.entity_list.remove(ent)
            
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                
                if not (self.game_over or self.victory):
                    ent.move()
                elif player and player.is_falling and ent.name == 'Player' and not self.game_over:
                    ent.move()
            
            seconds_left = max(0, self.game_time // 60)
            mins = seconds_left // 60
            secs = seconds_left % 60
            
            # Calculate zoom effect for the last 10 seconds
            time_zoom = 1.0
            if self.game_time <= 10 * 60 and self.game_time > 0 and not player.is_falling:
                time_zoom = 1.0 + abs(math.sin(pygame.time.get_ticks() / 150.0)) * 0.3

            self.level_text(35, f'{mins:02d}:{secs:02d}', C_YELLOW, (WIN_WIDTH - 70, 30), zoom=time_zoom)
            
            if player:
                fuel_pct = (player.fuel / player.max_fuel) * 100
                self.level_text(25, f'Combustivel: {fuel_pct:.0f}%', C_YELLOW, (WIN_WIDTH - 100, 70))
                
                if player.is_falling and player.rect.top >= WIN_HEIGHT:
                    self.game_over = True
                
                if self.game_time <= 0 and not player.is_falling:
                    self.victory = True
                    pygame.mixer_music.stop() 
            
            if self.game_over:
                self.level_text(40, 'GAME OVER', C_RED, (WIN_WIDTH // 2, WIN_HEIGHT // 2 - 40))
                self.draw_end_menu()
                
            elif self.victory:
                self.level_text(40, 'VITORIA!', (0, 255, 0), (WIN_WIDTH // 2, WIN_HEIGHT // 2 - 40))
                self.draw_end_menu()
            
            pygame.display.flip()

    def draw_end_menu(self):
        color_recomecar = C_YELLOW if self.menu_option == 0 else C_WHITE
        color_sair = C_YELLOW if self.menu_option == 1 else C_WHITE
        
        self.level_text(30, 'Recomeçar', color_recomecar, (WIN_WIDTH // 2, WIN_HEIGHT // 2 + 10))
        self.level_text(30, 'Sair', color_sair, (WIN_WIDTH // 2, WIN_HEIGHT // 2 + 50))

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, zoom: float = 1.0):
        text_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size, bold=True)
        
        main_surf = text_font.render(text, True, text_color).convert_alpha()
        outline_surf = text_font.render(text, True, C_BLACK).convert_alpha()
        
        if zoom != 1.0:
            new_width = int(main_surf.get_width() * zoom)
            new_height = int(main_surf.get_height() * zoom)
            main_surf = pygame.transform.scale(main_surf, (new_width, new_height))
            outline_surf = pygame.transform.scale(outline_surf, (new_width, new_height))
            
        for dx, dy in [(-2,-2), (2,-2), (-2,2), (2,2), (-2,0), (2,0), (0,-2), (0,2)]:
            outline_rect = outline_surf.get_rect(center=(text_center_pos[0] + dx, text_center_pos[1] + dy))
            self.window.blit(outline_surf, outline_rect)
            
        text_rect = main_surf.get_rect(center=text_center_pos)
        self.window.blit(main_surf, text_rect)
        