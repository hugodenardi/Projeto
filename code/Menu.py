import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_RED, WIN_WIDTH, C_ORANGE, MENU_OPTION, C_WHITE, C_YELLOW, WIN_HEIGHT


class Menu:
    def __init__(self, window):
        self.window = window
        img_original = pygame.image.load('./asset/MenuBg.png')
        self.surf = pygame.transform.scale(img_original, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            # Initialize the menu background
            self.window.blit(source=self.surf, dest=self.rect)
            
            # Title and subtitle of the game
            self.menu_text(60, "CITY", C_RED, ((WIN_WIDTH / 2), 45), font_name="Arial Black", draw_border=True)
            self.menu_text(60, "FLY", C_RED, ((WIN_WIDTH / 2), 100), font_name="Arial Black", draw_border=True)
            self.menu_text(16, "Não deixe seu avião ficar sem combustível", C_ORANGE, ((WIN_WIDTH / 2), 160), font_name="Arial Black", draw_border=True)

            # Menu options (Começar, Sair)
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(22, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 195 + 25 * i), font_name="Arial Black", draw_border=True)
                else:
                    self.menu_text(22, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 195 + 25 * i), font_name="Arial Black", draw_border=True)

            # Left Bottom Corner: Game Objective
            self.menu_text(20, "Vença voando", C_WHITE, (15, WIN_HEIGHT - 35), font_name="Lucida Sans Typewriter", draw_border=True, align="left")
            self.menu_text(20, "por 1 minuto", C_WHITE, (15, WIN_HEIGHT - 20), font_name="Lucida Sans Typewriter", draw_border=True, align="left")

            # Right Bottom Corner: Game Controls
            self.menu_text(20, "Comandos:", C_WHITE, (WIN_WIDTH - 15, WIN_HEIGHT - 35), font_name="Lucida Sans Typewriter", draw_border=True, align="right")
            self.menu_text(20, "Setas do Teclado", C_YELLOW, (WIN_WIDTH - 15, WIN_HEIGHT - 20), font_name="Lucida Sans Typewriter", draw_border=True, align="right")

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # ENTER
                        return MENU_OPTION[menu_option]
                    

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple, font_name="Lucida Sans Typewriter", draw_border=False, align="center"):
        text_font: Font = pygame.font.SysFont(name=font_name, size=text_size)
        
        # Create a helper function to get the rect based on alignment
        def get_rect_by_align(surf, pos):
            if align == "left":
                return surf.get_rect(left=pos[0], centery=pos[1])
            elif align == "right":
                return surf.get_rect(right=pos[0], centery=pos[1])
            else:
                return surf.get_rect(center=pos)

        if draw_border:
            border_surf: Surface = text_font.render(text, True, (0, 0, 0)).convert_alpha()
            for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2), (-2, -2), (2, -2), (-2, 2), (2, 2)]:
                # Apply the border offset to the base position
                shifted_pos = (text_pos[0] + dx, text_pos[1] + dy)
                border_rect = get_rect_by_align(border_surf, shifted_pos)
                self.window.blit(source=border_surf, dest=border_rect)

        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = get_rect_by_align(text_surf, text_pos)
        self.window.blit(source=text_surf, dest=text_rect)
