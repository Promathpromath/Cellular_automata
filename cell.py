import pygame

class Cell():
    def __init__(self, x, y, size, is_life):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, size, size)
        self.is_life = is_life


    def draw(self, surface):
        if self.is_life:
            pygame.draw.rect(surface, (0, 255, 0), self.rect)
        else:
            pygame.draw.rect(surface, (0, 0 , 0), self.rect)

