import pygame
import obstacle
from obstacle import Obstacle

from score import Score
import random

pygame.init()
from constans1 import *

#הגדרת התמונה
img = pygame.image.load("images/flappy-bird-nitzanim.png")
img = pygame.transform.scale(img, (width_img, height_img))

#הגדרת מסך
screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(screen_size)

obstacle_list = []
for i in range(3, 100):
    upper = Obstacle(500*i, 0, 50, random.randint(50, 100), True)
    lower = Obstacle(500 * i, random.randint(400, 500), 50, 500, False)
    obstacle_list.append(upper)
    obstacle_list.append(lower)


#רשימת צינורות
# obstacle_list = [Obstacle(1000, 0, 50, 200), Obstacle(1500, 0, 50, 100),
#                  Obstacle(1000, 400, 50, 200), Obstacle(1500, 400, 50, 500),
#                  Obstacle(2000, 400, 50, 500), Obstacle(2000, 400, 50, 100)
#                  ]

#יצירת משתנה של ניקוד
player_score = Score()
time_delay = 10

#משתנים בוליאניים של המשחק
isFalling = True
isPlaying = True

#לולאת המשחק
while isPlaying:
    isFalling = True
    #בדיקת לחיצות על מקשים
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isPlaying = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            y_pos_img -= 70
            isFalling = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y_pos_img -= 70
                isFalling = False

    screen.fill((0, 0, 0))

#יצירת מונה הניקוד על המסך
    font = pygame.font.SysFont('Aharoni', 30)
    text = font.render(str(player_score.get_score()), True, color)
    screen.blit(text, [player_score.x_pos_score, player_score.y_pos_score])

    if isFalling:
        y_pos_img += 2
    bird_object = pygame.Rect(x_pos_img, y_pos_img, width_img,
                              height_img)
    if y_pos_img == WINDOW_HEIGHT:
        isPlaying = False
    if x_pos_img == WINDOW_WIDTH:
        isPlaying = False

    # if player_score.get_score() % 10 == 1:
    #     time_delay = int(time_delay * 0.9)

    for obstacle in obstacle_list:
        obstacle.move_left()
        obstacle.draw(screen)
        if pygame.Rect.colliderect(bird_object, obstacle.get_rect()):
            isPlaying = False
        # if obstacle.x <= 0:
        #     obstacle.reset_x()
        if x_pos_img > obstacle.x + 50:
            if not obstacle.given_score:
                obstacle.given_score = True
                player_score.increase_score()

    screen.blit(img, (x_pos_img, y_pos_img))
    pygame.display.update()
    pygame.time.delay(time_delay)

pygame.quit()
