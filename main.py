
import pygame
import sys

from pygame.image import load

GAME_SPRITES = {
    'ball': './sprites/ball/ball.png',
    'board': './sprites/board/board.png',
    'player': './sprites/player/player.png',
    'ui': './sprites/ui/'
}

FPS = 60
WIDTH = 693  
HEIGHT = 364
SPEED = 5

class PongGame:
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Pong Game')
        
        WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

        BOARD = pygame.image.load(GAME_SPRITES['board'])

        # Player 1 
        PLAYER1, player1_position = self.player1_properties()

        # Player 2
        PLAYER2, player2_position = self.player2_properties()

        # Game Loop
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(FPS)
            for event in pygame.event.get():
                # Quit Handler
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()

                # Player 1 Movement Input
                key_pressed = pygame.key.get_pressed()
                self.player1_movement_input(player1_position, key_pressed)
                self.player2_movement_input(player2_position, key_pressed)

            # Draw Objects here...
            WINDOW.blit(BOARD, (0, 0)) # Draw the Board

            # Draw Player1
            WINDOW.blit(PLAYER1, player1_position)
            WINDOW.blit(PLAYER2, player2_position)
            pygame.display.update()

    def player1_properties(self):
        PLAYER1 = pygame.image.load(GAME_SPRITES['player'])
        PLAYER1_START_POS_X = 70
        PLAYER1_START_POS_y = HEIGHT/2

        player1_position = pygame.image.load(GAME_SPRITES['player']).get_rect()
        player1_position.center = (PLAYER1_START_POS_X, PLAYER1_START_POS_y)
        return PLAYER1,player1_position

    def player2_properties(self):
        PLAYER2 = pygame.image.load(GAME_SPRITES['player'])
        PLAYER2_START_POS_X = 623
        PLAYER2_START_POS_y = HEIGHT/2

        player2_position = pygame.image.load(GAME_SPRITES['player']).get_rect()
        player2_position.center = (PLAYER2_START_POS_X, PLAYER2_START_POS_y)
        return PLAYER2,player2_position

    def player1_movement_input(self, player1_position, key_pressed):
        if key_pressed[pygame.K_w]:
            player1_position.y -= SPEED
        if key_pressed[pygame.K_s]:
            player1_position.y += SPEED

    def player2_movement_input(self, player2_position, key_pressed):
        if key_pressed[pygame.K_o]:
            player2_position.y -= SPEED
        if key_pressed[pygame.K_l]:
            player2_position.y += SPEED

if __name__ == '__main__':
    PongGame()
    