import pygame




class Score:
    def __init__(self):
        self.x_pos_score = 750
        self.y_pos_score = 50
        self.font = pygame.font.SysFont('Aharoni', 30)
        self.score = 0
        self.color = (255, 255, 255)

    def increase_score(self):
        self.score +=1

    def get_score(self):
        return self.score




