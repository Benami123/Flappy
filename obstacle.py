import pygame


class Obstacle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (255, 255, 255)
        self.init_x = x

    def move_left(self):
        self.x -= 5

    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, rect)

    def get_rect(self):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return rect

    def reset_x(self):
        self.x = self.init_x