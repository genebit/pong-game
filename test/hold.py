import pygame

pygame.init()
pygame.display.set_mode((500, 500))

holding_up = False
holding_down = False

while True:
    
    for e in pygame.event.get(): # Detect Events

        # Hold Key
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                holding_up = True
            if e.key == pygame.K_DOWN:
                holding_down = True
            
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_UP:
                holding_up = False
                print('Stopped')
            if e.key == pygame.K_DOWN:
                holding_down = False
                print('Stopped')
            
        # Quit Handler
        if e.type == pygame.QUIT:
            pygame.quit()

    if holding_up:
        print('Holding UP')
    if holding_down:
        print('Holding DOWN')            
