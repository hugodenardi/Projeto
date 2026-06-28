import random
from code.Background import Background
from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Player import Player
from code.Fuel import Fuel
from code.Enemy import Enemy

class EntityFactory:

    # Static method to get an entity based on its name and position
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg': # Create a list of background entities for Level 1
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level1Bg{i}', position=(0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', position=(WIN_WIDTH, 0)))
                return list_bg
            
            # Create a player entity at a specific position
            case 'Player':
                return Player(name='Player', position=(10, WIN_HEIGHT // 2))

            # Create a fuel entity at a random vertical position on the right edge of the screen    
            case 'Fuel':
                random_y = random.randint(30, WIN_HEIGHT - 30)
                return Fuel(name='Fuel', position=(WIN_WIDTH, random_y))

            # Create enemy entities at a random vertical position on the right edge of the screen    
            case 'Enemy1':
                random_y = random.randint(30, WIN_HEIGHT - 30)
                return Enemy(name='Enemy1', position=(WIN_WIDTH, random_y))
                
            case 'Enemy2':
                random_y = random.randint(30, WIN_HEIGHT - 30)
                return Enemy(name='Enemy2', position=(WIN_WIDTH, random_y))
            