import pygame


class Obstacle:
    def __init__(self, x, y, width, height, isupper):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (255, 255, 255, 128)
        self.init_x = x
        self.isupper = isupper
        if not isupper:
            self.given_score = True
        else:
            self.given_score = False
        down_obstacle_img = pygame.image.load("images/pipe-down-fixedddd.png")
        down_obstacle_img = pygame.transform.scale(down_obstacle_img, (self.width, self.height))
        self.down_obstacle_img = down_obstacle_img
        upper_obstacle_img = pygame.image.load("images/pipe-up-fixedddd.png")
        upper_obstacle_img = pygame.transform.scale(upper_obstacle_img,
                                              (self.width, self.height))
        self.upper_obstacle_img = upper_obstacle_img



    def move_left(self):
        self.x -= 5

    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, rect)
        if self.isupper:
            screen.blit(self.upper_obstacle_img, (self.x, self.y))
        else:
            screen.blit(self.down_obstacle_img, (self.x, self.y))

    def get_rect(self):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return rect

    def reset_x(self):
        self.x = self.init_x
        self.given_score = False