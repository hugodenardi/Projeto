# Import necessary constants and modules for the game
from code.Const import MENU_OPTION, WIN_WIDTH, WIN_HEIGHT
from code.Level import Level
from code.Menu import Menu

# Import the pygame library
import pygame

class Game:
    
    def __init__(self):
        # Initialize all imported pygame modules
        pygame.init()

        # Set up the main display window using the imported width and height constants
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))


    def run(self):
    
        # Main game loop that keeps the application running continuously
        while True:
            # Instantiate the main menu, passing the game window as a reference
            menu = Menu(self.window)
            
            # Run the menu and store the user's selected option
            menu_return = menu.run()
            
            # Check if the user selected the first option to start the game
            if menu_return == MENU_OPTION[0]:  # Start
                # Instantiate and run the first level
                level = Level(self.window, 'Level 1', menu_return)
                level_return = level.run()

            # Check if the user selected the third option to exit the game
            elif menu_return == MENU_OPTION[2]:  # Options
                # Uninitialize all pygame modules and terminate the program
                pygame.quit()
                quit()

            # Handle any other unmapped menu options
            else:
                pass
            