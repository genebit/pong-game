
import pygame

pygame.init()
assets = {
    'ball': './sprites/ball/ball.png'
}

FPS = 60
WIDTH = 400
HEIGHT = 400
BLACK = (26, 26, 26)

SPEED = 5

class Game:
    def __init__(self, width, height):
        WINDOW = pygame.display.set_mode((width, height))

        # Sprite Properties
        BALL = pygame.image.load(assets['ball'])
        BALL_START_POS_X = WINDOW.get_width()/2
        BALL_START_POS_Y = WINDOW.get_height()/2
        
        position = pygame.Rect(BALL_START_POS_X, BALL_START_POS_Y, BALL.get_width(), BALL.get_height())

        # Game Loop
        clock = pygame.time.Clock()
        while True:
            clock.tick(FPS)
            for event in pygame.event.get():
                # Quit Handler
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
            # Key Input...
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_d]:
                position.x += SPEED
            if key_pressed[pygame.K_a]:
                position.x -= SPEED
            if key_pressed[pygame.K_w]:
                position.y -= SPEED
            if key_pressed[pygame.K_s]:
                position.y += SPEED
                
            # Background
            WINDOW.fill(BLACK)

            # Objects
            WINDOW.blit(BALL, (position.x, position.y))
            pygame.display.update()

if __name__ == '__main__':
    Game(WIDTH, HEIGHT)