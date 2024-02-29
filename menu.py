import pygame

class Menu():
    def __init__(self, color_fill, color_button):
        self.color_screen = color_fill
        self.color_button = color_button
        self.width_button = 300
        self.screen = pygame.Rect(0, 0, 1000, 1000)
        self.buttons = []

    def buttons_fill(self):
        y = 50
        for _ in range(5):
            button = pygame.Rect(650, y, self.width_button, 100)
            self.buttons.append(button)
            y += 200

    def screen_draw(self, surface):
        pygame.draw.rect(surface, self.color_screen, self.screen)

    def buttons_draw(self, surface):
        font_style = pygame.font.SysFont('arial', 40, True, True)
        i = 0
        for button in self.buttons:
            pygame.draw.rect(surface, self.color_button, button)
            if i == 0:
                text = 'LIFE'
            elif i == 1:
                text = 'DAY & NIGHT'
            else:
                text = ''
            title = font_style.render(text, True, self.color_screen)
            shift_x = (self.width_button - len(text) * 20) / 2
            surface.blit(title, (button.x + shift_x, button.y + 30))
            i += 1



