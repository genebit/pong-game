
import pygame

# TODO: Colliders to not go out of bounds and bounce the ball

FPS = 60
WIDTH = 350
HEIGHT = 300

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))

# Sprites
ball = pygame.image.load('./img/ball.png')
position = ball.get_rect()
position.center = (window.get_width()/2, window.get_height()/2)

bounds = pygame.Rect(0, 0, 300, 250)
bounds.center = (window.get_width()/2, window.get_height()/2)

# Main loop
clock = pygame.time.Clock()
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    
    window.fill((26, 26, 26)) # Fill to black

    pygame.draw.rect(window, (245, 72, 66), bounds, 3)
    
    window.blit(ball, position)
    pygame.display.update()