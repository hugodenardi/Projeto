import pygame

from code.Entity import Entity
from code.EntityFactory import EntityFactory

class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        

    def run(self):
        clock = pygame.time.Clock() # Dica extra: adicione um controle de FPS
        
        while True:
            # 1. Primeiro, limpa a tela (opcional, mas boa prática)
            self.window.fill((0, 0, 0)) 
            
            # 2. Desenha e move TODAS as entidades na memória
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            
            # 3. SÓ AGORA, depois de desenhar tudo, joga o resultado na tela!
            pygame.display.flip()
            
            # Controla a velocidade do jogo (ex: 60 quadros por segundo)
            clock.tick(60)
