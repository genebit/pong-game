
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

class PongGame:

    def __init__(self, width, height, fps):
        pygame.init()

        # Set the Window Properties
        self.WINDOW = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Classic Pong Game')

        # Load the Images
        board = pygame.image.load(SPRITES['board'])
        self.player1 = pygame.image.load(SPRITES['player'])
        self.player2 = pygame.image.load(SPRITES['player'])
        self.ball = pygame.image.load(SPRITES['ball'])
        
        # Game Loop
        running = True

        clock = pygame.time.Clock()
        while running:
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Draw Here
            self.WINDOW.blit(board, (0, 0))
            
            self.player1.center = (50, self.WINDOW.get_height()/2)

            pygame.display.update()
    
    def player1_properties(self, position_x, position_y, speed):
        self.player1 = pygame.get_rect()
        self.player1.center = (50, self.WINDOW.get_height()/2)
        
        
if __name__ == '__main__':
    FPS = 60
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 400
    
    PongGame(WINDOW_WIDTH, WINDOW_HEIGHT, FPS)