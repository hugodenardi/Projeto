import random 
from code.Background import Background
from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Player import Player
from code.Fuel import Fuel

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level1Bg{i}', position=(0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', position=(WIN_WIDTH, 0)))
                return list_bg
            
            case 'Player':
                return Player(name='Player', position=(10, WIN_HEIGHT // 2))
                
            # --- NOVO CASE ---
            case 'Fuel':
                # Aparece no final da tela (direita) em uma altura aleatória
                random_y = random.randint(30, WIN_HEIGHT - 30)
                return Fuel(name='Fuel', position=(WIN_WIDTH, random_y))
