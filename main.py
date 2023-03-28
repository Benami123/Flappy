import pygame
import obstacle
from obstacle import Obstacle

pygame.init()
from constans1 import *

img = pygame.image.load("images/flappy-bird-nitzanim.png")
img = pygame.transform.scale(img, (width_img, height_img))

screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(screen_size)

isFalling = True
isPlaying = True
obstacle_list = [Obstacle(1000, 0, 50, 300), Obstacle(2000, 700, 50, 100)]
while isPlaying:
    isFalling = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isPlaying = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            y_pos_img -= 70
            isFalling = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_pos_img -= 20
            if event.key == pygame.K_RIGHT:
                x_pos_img += 20

    screen.fill((0, 0, 0))
    if isFalling:
        y_pos_img += 2
    bird_object = pygame.Rect(x_pos_img, y_pos_img, width_img,
                              height_img)
    for obstacle in obstacle_list:
        obstacle.move_left()
        obstacle.draw(screen)
        if pygame.Rect.colliderect(bird_object, obstacle.get_rect()):
            isPlaying = False
        if obstacle.x <= 0:
            obstacle.reset_x()

    screen.blit(img, (x_pos_img, y_pos_img))
    pygame.display.update()
    pygame.time.delay(10)

pygame.quit()
