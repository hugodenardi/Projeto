from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu

import pygame

class Game:
    
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))


    def run(self):
    
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
      
        # while True:
        #     # Check for all events
        #     for event in pygame.event.get():
        #         # If the event is a quit event, exit the loop
        #         if event.type == pygame.QUIT:
        #             pygame.quit()
        #             quit()
