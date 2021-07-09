import sys, pygame
import random

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 400
speed = [random.randint(5, 15), random.randint(5, 15)]

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

ball = pygame.Rect(0, 0, 50, 50)

clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ball = ball.move(speed)
    
    if ball.left < 0 or ball.right > WINDOW_WIDTH: # Checks if the collider hits the window border
        speed[0] = -speed[0] # Converts the speed to move negative to bounce back

    if ball.top < 0 or ball.bottom > WINDOW_HEIGHT:
        speed[1] = -speed[1]

    WINDOW.fill((26, 26, 26))
    pygame.draw.rect(WINDOW, (255, 255, 255), ball)
    
    pygame.display.update()