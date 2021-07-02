
import pygame

FPS = 120

WIDTH = 500
HEIGHT = 500
GREEN = (95, 255, 89)

pygame.init()
CAT_PATH = pygame.image.load('./test/cat.png') # Convert it to Surface

WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Set the Window Size

cat = pygame.Rect(10, 10, 150, 150)


clock = pygame.time.Clock()
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # Draw Game Objects here...
    WIN.fill(GREEN)
    WIN.blit(CAT_PATH, (cat.x, cat.y))
    cat.y += 1
    pygame.display.update()