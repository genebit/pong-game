

import pygame

pygame.init()

img = pygame.image.load('./test/cat.png')

while True:

    screen = pygame.display.set_mode((300, 300))

    rect = img.get_rect()
    rect.center = pygame.Vector2(0, 0)
    screen.blit(img, rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            print('Quit Program')
            pygame.quit()
            quit()

    pygame.display.update() 

