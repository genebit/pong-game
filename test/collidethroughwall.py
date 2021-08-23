
import pygame
import sys

# --------------------

FPS = 60
WINDOW_SIZE = (400, 300)
# --------------------
pygame.init()

box = pygame.Rect(0, 0, 100, 100)
wall = pygame.Rect(0, 0, 5, 200)

def main():
    WINDOW = pygame.display.set_mode(WINDOW_SIZE)
    
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        WINDOW.fill((26, 26, 26))
        
        # Draw here...
        box.center = (pygame.mouse.get_pos())
        pygame.draw.rect(WINDOW, (255, 255, 255), box, 4)
        
        wall.center = (50, WINDOW.get_height()/2)
        pygame.draw.rect(WINDOW, (255, 255, 255), wall)
        
        collide = wall.colliderect(box)

        if collide:
            print('Something hit')
        else:
            print('No Collision Detected')

        pygame.display.update()

if __name__ == '__main__':
    main()