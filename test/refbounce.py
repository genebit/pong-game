import sys, pygame
import random

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 400
speed = [random.randint(5, 15), random.randint(5, 15)]

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

ball = pygame.image.load("./img/ball.png")
ballrect = ball.get_rect()
print(ballrect)
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ballrect = ballrect.move(speed)

    if ballrect.left < 0 or ballrect.right > WINDOW_WIDTH: # Checks if the collider hits the window border
        speed[0] = -speed[0] # Converts the speed to move negative to bounce back

    if ballrect.top < 0 or ballrect.bottom > WINDOW_HEIGHT:
        speed[1] = -speed[1]

    WINDOW.fill((26, 26, 26))
    WINDOW.blit(ball, ballrect)
    
    pygame.display.update()