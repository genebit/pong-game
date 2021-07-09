import pygame
import sys
import random 
import time

FPS = 60
WINDOW_WIDTH, WINDOW_HEIGHT = (600, 300 )
BLACK = (20, 20, 20)
WHITE = (255, 255, 255)

PLAYER_SPEED = 5
P1_VELOCITY = [0, PLAYER_SPEED]
BALL_SPEED = [8, 8]

pygame.init()

# Where The main loop, main properties...
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Pong Game')

# Load Images...
PLAYER1 = pygame.Rect(0, 0, 15, 50)
PLAYER1.center = (50, WINDOW_HEIGHT/2)

PLAYER2 = pygame.Rect(0, 0, 15, 50)
PLAYER2.center = (550, WINDOW_HEIGHT/2)

BALL = pygame.Rect(0, 0, 15, 15)
BALL.center = (WINDOW_WIDTH/2, random.randint(30, 370))

# Main Loop...
clock = pygame.time.Clock()

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
    global PLAYER_SPEED, P1_VELOCITY

    keypressed = pygame.key.get_pressed()

    if keypressed[pygame.K_UP] and not keypressed[pygame.K_DOWN]:
        P2_VELOCITY = [0, -PLAYER_SPEED] if player2.top > 0 else [0, 0]
    elif keypressed[pygame.K_DOWN] and not keypressed[pygame.K_UP]:
        P2_VELOCITY = [0, PLAYER_SPEED] if player2.bottom < WINDOW_HEIGHT else [0, 0]        
    else:
        P2_VELOCITY = [0, 0]
    return P2_VELOCITY

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Quit Handler...
            sys.exit()

    # Draw Here...
    WINDOW.fill(BLACK)
    
    # region ball
    BALL = BALL.move(BALL_SPEED)
    p1_collide = BALL.colliderect(PLAYER1)
    p2_collide = BALL.colliderect(PLAYER2)

    if BALL.left < 0 or BALL.right > WINDOW_WIDTH or p1_collide or p2_collide: # Checks if the collider hits the window border
        BALL_SPEED[0] = -BALL_SPEED[0] # Converts the speed to move negative to bounce back

    if BALL.top < 0 or BALL.bottom > WINDOW_HEIGHT or p1_collide or p2_collide:
        BALL_SPEED[1] = -BALL_SPEED[1]

    # Verdict
    if BALL.left < 0:
        BALL.center = (WINDOW_WIDTH/2, random.randint(20, 380))
        time.sleep(1)

    elif BALL.right > WINDOW_WIDTH:
        BALL.center = (WINDOW_WIDTH/2, random.randint(20, 380))
        time.sleep(1)
        
    pygame.draw.rect(WINDOW, WHITE, BALL, 3)
    # endregion

    # Players
    P1_VELOCITY = p1_movement_input(PLAYER1)
    P2_VELOCITY = p2_movement_input(PLAYER2)
    
    PLAYER1 = PLAYER1.move(P1_VELOCITY)
    pygame.draw.rect(WINDOW, WHITE, PLAYER1, 3)

    PLAYER2 = PLAYER2.move(P2_VELOCITY)
    pygame.draw.rect(WINDOW, WHITE, PLAYER2, 3)

    pygame.display.update()