import pygame
import sys
import random 
import time

# Adjustable Parameters
FPS = 60
WINDOW_WIDTH, WINDOW_HEIGHT = (600, 400)
WHITE = (255, 255, 255)

PLAYER_SPEED = 8
P1_VELOCITY = [0, PLAYER_SPEED]
P2_VELOCITY = [0, PLAYER_SPEED]

BALL_SPEED = [random.randint(3, 5), random.randint(3, 5)]

pygame.init()

# Sounds------------
PADDLE = pygame.mixer.Sound('./sound/Paddle.wav')
SCORE = pygame.mixer.Sound('./sound/Score.wav')
HIT = pygame.mixer.Sound('./sound/Hit.wav')

#-------------------
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Pong Game')

PLAYER1 = pygame.Rect(0, 0, 20, 60)
PLAYER1.center = (50, WINDOW_HEIGHT/2)

PLAYER2 = pygame.Rect(0, 0, 20, 60)
PLAYER2.center = (550, WINDOW_HEIGHT/2)

BALL = pygame.Rect(0, 0, 20, 20)
BALL.center = (WINDOW_WIDTH/2, random.randint(50, 350))

FONT = pygame.font.Font('./font/Welbut.ttf', 30)

game_over_txt = FONT.render('GAME OVER', True, (255, 255, 255))
game_over_rect = game_over_txt.get_rect()
game_over_rect.center = (WINDOW_WIDTH/2, (WINDOW_HEIGHT/2)-20)

notes = FONT.render("Press 'P' to Restart", True, (255, 255, 255))
notes_rect = notes.get_rect()
notes_rect.center = (WINDOW_WIDTH/2, game_over_rect.bottom+20)

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

paused = False 
# Main Loop...
while True:
    CLOCK.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Quit Handler...
            sys.exit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_p:
                if paused:
                    paused = False
                    # reset the positions here...
                    BALL.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
                    PLAYER1.center = (50, WINDOW_HEIGHT/2)
                    PLAYER2.center = (550, WINDOW_HEIGHT/2)

                    PADDLE.play()
                    time.sleep(0.5)
                else:
                    paused = True

    # Draw Here...
    WINDOW.fill((26, 26, 26))

# region ball
    if not paused:
            # Keep moving
        BALL = BALL.move(BALL_SPEED)
 
        P1_COLLIDED = BALL.colliderect(PLAYER1)
        P2_COLLIDED = BALL.colliderect(PLAYER2)

        # Checks if the collider hits the border
        # Converts the speed to move negative to bounce back
        if BALL.left < 0 or BALL.right > WINDOW_WIDTH: 
            BALL_SPEED[0] = -BALL_SPEED[0] 
            HIT.play()

        if BALL.top < 0 or BALL.bottom > WINDOW_HEIGHT:
            BALL_SPEED[1] = -BALL_SPEED[1]
            HIT.play()
        
        # Player Paddle Collide
        if P1_COLLIDED or P2_COLLIDED:
            BALL_SPEED[0] = -BALL_SPEED[0] + BALL_SPEED[1]
            BALL_SPEED[1] = -BALL_SPEED[1] + BALL_SPEED[0]
            PADDLE.play()

        # Game Over
        if BALL.left < 0 or BALL.right > WINDOW_WIDTH:
            paused = True
            SCORE.play()

        if BALL.top < 0 or BALL.bottom > WINDOW_HEIGHT:
            paused = False

        pygame.draw.rect(WINDOW, WHITE, BALL, 3)
    else:
        WINDOW.blit(game_over_txt, game_over_rect)
        WINDOW.blit(notes, notes_rect)
# endregion
    
    # Players
    P1_VELOCITY = p1_movement_input(PLAYER1)
    P2_VELOCITY = p2_movement_input(PLAYER2)
    
    PLAYER1 = PLAYER1.move(P1_VELOCITY)
    pygame.draw.rect(WINDOW, WHITE, PLAYER1, 3)

    PLAYER2 = PLAYER2.move(P2_VELOCITY)
    pygame.draw.rect(WINDOW, WHITE, PLAYER2, 3)

    pygame.display.update()