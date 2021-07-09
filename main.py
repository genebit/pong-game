
# TODO:
'''
    move the players
    add constraints to the movement
    add the ball
'''

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

pygame.init()

# Load Images...
BOARD = pygame.image.load(SPRITES['board'])
PLAYER1 = pygame.image.load(SPRITES['player'])

def draw_objects(window):
    window.blit(BOARD, (0, 0))

    PLAYER1_RECT = PLAYER1.get_rect()
    PLAYER1_RECT.center = (60, window.get_height()/2)
    
    window.blit(PLAYER1, PLAYER1_RECT)

def main():
    # Where The main loop, main properties...
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Pong Game')
    
    # Main Loop...
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Quit Handler...
                sys.exit()

        # Draw Here...
        draw_objects(WINDOW)

        pygame.display.update()

if __name__ == '__main__':
    main()