import pygame
import sys
import random

SPRITES = {
    "player": "./sprites/player/player.png",
    "ball": "./sprites/ball/ball.png",
    "board": "./sprites/board/board.png",
}

FPS = 60
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 400 

PLAYER_SPEED = [0, 0]
BALL_SPEED = [random.randint(5, 15), random.randint(5, 15)]

pygame.init()

# Where The main loop, main properties...
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Pong Game')

# Load Images...
PLAYER1 = pygame.Rect(0, 0, 15, 60)
PLAYER1.center = (50, WINDOW.get_height()/2)

BALL = pygame.Rect(0, 0, 20, 20)
BALL.center = (WINDOW.get_width()/2, random.randint(20, 380))

# Main Loop...
clock = pygame.time.Clock()

def p1_movement_input(window, player1):
    keypressed = pygame.key.get_pressed()
    if keypressed[pygame.K_w] and not keypressed[pygame.K_s]:
        PLAYER_SPEED = [0, -5] if player1.top > 0 else [0, 0]
    elif keypressed[pygame.K_s] and not keypressed[pygame.K_w]:
        PLAYER_SPEED = [0, 5] if player1.bottom < window.get_height() else [0, 0]        
    else:
        PLAYER_SPEED = [0, 0]
    return PLAYER_SPEED

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Quit Handler...
            sys.exit()

    # Draw Here...
    BLACK = (20, 20, 20)
    WHITE = (255, 255, 255)

    WINDOW.fill(BLACK)
    
    # Players
    PLAYER_SPEED = p1_movement_input(WINDOW, PLAYER1)
    # region ball
    BALL = BALL.move(BALL_SPEED)

    # endregion
    PLAYER1 = PLAYER1.move(PLAYER_SPEED)
    pygame.draw.rect(WINDOW, WHITE, PLAYER1, 3)

    pygame.draw.rect(WINDOW, WHITE, BALL, 3)

    pygame.display.update()
