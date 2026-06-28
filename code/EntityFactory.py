from code.Background import Background
from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Player import Player


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
            
