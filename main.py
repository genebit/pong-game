import pygame
import sys
import random 
import time

# Adjustable Parameters
FPS = 60
WINDOW_WIDTH, WINDOW_HEIGHT = (600, 400)
WHITE = (255, 255, 255)

PLAYER_SPEED = 5
PLAYER_SIZE = (15, 50)
P1_VELOCITY = [0, PLAYER_SPEED]
P2_VELOCITY = [0, PLAYER_SPEED]

BALL_SPEED = [8, 8]

pygame.init()

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Pong Game')

# Game Objects...
BOARD = pygame.image.load('./sprites/board.png')

PLAYER1 = pygame.Rect(0, 0, PLAYER_SIZE)
PLAYER1.center = (50, WINDOW_HEIGHT/2)

PLAYER2 = pygame.Rect(0, 0, PLAYER_SIZE)
PLAYER2.center = (550, WINDOW_HEIGHT/2)

BALL = pygame.Rect(0, 0, 15, 15)
BALL.center = (WINDOW_WIDTH/2, random.randint(50, 350))


def p1_movement_input(player1):
    global PLAYER_SPEED, P1_VELOCITY
    
    keypressed = pygame.key.get_pressed()

    if keypressed[pygame.K_w] and not keypressed[pygame.K_s]:
        P1_VELOCITY = [0, -PLAYER_SPEED] if player1.top > 0 else [0, 0]
    elif keypressed[pygame.K_s] and not keypressed[pygame.K_w]:
        P1_VELOCITY = [0, PLAYER_SPEED] if player1.bottom < WINDOW_HEIGHT else [0, 0]        
    else:
        P1_VELOCITY = [0, 0]
    return P1_VELOCITY

def p2_movement_input(player2):
    global PLAYER_SPEED, P2_VELOCITY

    keypressed = pygame.key.get_pressed()

    if keypressed[pygame.K_UP] and not keypressed[pygame.K_DOWN]:
        P2_VELOCITY = [0, -PLAYER_SPEED] if player2.top > 0 else [0, 0]
    elif keypressed[pygame.K_DOWN] and not keypressed[pygame.K_UP]:
        P2_VELOCITY = [0, PLAYER_SPEED] if player2.bottom < WINDOW_HEIGHT else [0, 0]        
    else:
        P2_VELOCITY = [0, 0]
    return P2_VELOCITY

CLOCK = pygame.time.Clock()
# Main Loop...
while True:
    CLOCK.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Quit Handler...
            sys.exit()

    # Draw Here...
    WINDOW.blit(BOARD, (0, 0))

# region ball
    BALL = BALL.move(BALL_SPEED)

    P1_COLLIDED = BALL.colliderect(PLAYER1)
    P2_COLLIDED = BALL.colliderect(PLAYER2)

    # Checks if the collider hits the border
    # Converts the speed to move negative to bounce back
    if BALL.left < 0 or BALL.right > WINDOW_WIDTH or P1_COLLIDED or P2_COLLIDED: 
        BALL_SPEED[0] = -BALL_SPEED[0] 
    if BALL.top < 0 or BALL.bottom > WINDOW_HEIGHT or P1_COLLIDED or P2_COLLIDED:
        BALL_SPEED[1] = -BALL_SPEED[1]

    # region Verdict
    p1_hitbounds = BALL.left < 0
    p2_hitbounds = BALL.right > WINDOW_WIDTH
    
    if p1_hitbounds:
        BALL.center = (WINDOW_WIDTH/2, random.randint(20, 380))
        # time.sleep(1)
    elif p2_hitbounds:
        BALL.center = (WINDOW_WIDTH/2, random.randint(20, 380))
        # time.sleep(1)
    # endregion
    pygame.draw.rect(WINDOW, WHITE, BALL)
# endregion
    
    # Players
    P1_VELOCITY = p1_movement_input(PLAYER1)
    P2_VELOCITY = p2_movement_input(PLAYER2)
    
    PLAYER1 = PLAYER1.move(P1_VELOCITY)
    pygame.draw.rect(WINDOW, WHITE, PLAYER1)

    PLAYER2 = PLAYER2.move(P2_VELOCITY)
    pygame.draw.rect(WINDOW, WHITE, PLAYER2)


    pygame.display.update()