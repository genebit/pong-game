import pygame
import sys
import random 
import time

import soundmanager
import texts
import players
import movements
import _ball

FPS = 60
WINDOW_WIDTH, WINDOW_HEIGHT = (600, 400)
WHITE = (255, 255, 255)
BLACK = (20, 20, 20)

PLAYERSPEED = 8
p1_velo = [0, PLAYERSPEED]
p2_velo = [0, PLAYERSPEED]

BALLSPEED = [random.randint(3, 5), random.randint(3, 5)]

pygame.init()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Pong Game')

sound_manager = soundmanager.SoundManager()
text_display = texts.Text(window)

_player1 = players.Player1(window)
_player2 = players.Player2(window)

_ball = _ball.Ball(window)

clock = pygame.time.Clock()
gameover = False 

def reset_game(window, _player1, _player2, ball):

    ball.center = (window.get_width()/2, window.get_height()/2)
    _player1.center = (50, window.get_height()/2)
    _player2.center = (550, window.get_height()/2)
    
    picker = random.randint(0, 1)
    
    global BALLSPEED
    if picker == 0:
        BALLSPEED = [-random.randint(3, 5), random.randint(3, 5)]
    elif picker == 1:
        BALLSPEED = [random.randint(3, 5), random.randint(3, 5)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Quit Handler...
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYUP: # Game Over Handler...
            if event.key == pygame.K_r:
                if gameover:
                    gameover = False
                    reset_game(window, _player1.player1, _player2.player2, _ball.ball)

                    sound_manager.play('paddle')
                    time.sleep(0.5)
                else:
                    gameover = True

    # Draw Here...
    window.fill(BLACK)

    if not gameover:

        if _ball.ball.left < 0 or _ball.ball.right > WINDOW_WIDTH:
            gameover = True
            sound_manager.play('score')

        if _ball.ball.top < 0 or _ball.ball.bottom > WINDOW_HEIGHT:
            gameover = False
    
        keypressed = pygame.key.get_pressed()

        p1_velo = movements.Input.p1_movement(window, _player1.player1, keypressed, p1_velo, PLAYERSPEED)
        p2_velo = movements.Input.p2_movement(window, _player2.player2, keypressed, p2_velo, PLAYERSPEED)
        
        _player1.draw(window, p1_velo)
        _player2.draw(window, p2_velo)
        
        _ball.draw(BALLSPEED, _player1.player1, _player2.player2)
    else:
        text_display.show_gameover(window)

    clock.tick(FPS)
    pygame.display.update()