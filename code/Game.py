from code.Const import MENU_OPTION, WIN_WIDTH, WIN_HEIGHT
from code.Level import Level
from code.Menu import Menu

import pygame

class Game:
    
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))


    def run(self):
    
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()
            
            if menu_return == MENU_OPTION[0]:  # Start
                level = Level(self.window, 'Level 1', menu_return)
                level_return = level.run()

            elif menu_return == MENU_OPTION[2]:  # Options
                pygame.quit()
                quit()

            else:
                pass    
            


        # while True:
        #     # Check for all events
        #     for event in pygame.event.get():
        #         # If the event is a quit event, exit the loop
        #         if event.type == pygame.QUIT:
        #             pygame.quit()
        #             quit()
