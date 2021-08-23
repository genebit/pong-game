# Press P for pause

import pygame
import sys
import time

pygame.init()

width = 400
height = 300

window = pygame.display.set_mode((width, height))

ball = pygame.Rect(0, 0, 50, 50)
ball.center = (width/2, height/2)

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('PAUSED', True, (255, 255, 255))
text_rect = text.get_rect()
text_rect.center = (width/2, height/2)

speed = [0, 1]

paused = False
clock = pygame.time.Clock()

while True:
    window.fill((26, 26, 26))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_p:
                if paused:
                    paused = False
                    # reset the positions here...
                    ball.center = (width/2, height/2)
                    time.sleep(0.5)
                else:
                    paused = True

    if not paused:
        # Keep moving
        ball = ball.move(speed)
        
        if ball.top < 0 or ball.bottom > height:
            speed[1] = -speed[1]
            paused = True
    else:
        window.blit(text, text_rect)
        
    pygame.draw.rect(window, (255, 255, 255), ball, 3)

    pygame.display.update()
    clock.tick(60)

    