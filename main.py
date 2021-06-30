try:
    import pygame
except ImportError as err:
    print('Import Error occured. \n Error Log: {0}'.format(err))

game_sprites = {
    'ball': './sprites/ball/ball.png',
    'board': './sprites/board/board.png',
    'player': './sprites/player/player.png',
    'ui': './sprites/ui/'
}

class Game:
    WIDTH = 637  
    HEIGHT = 301
    window_size = WIDTH, HEIGHT

    def __init__(self, pygame, sprites):
        self.pygame = pygame
        self.sprites = sprites
        
        # Window properties
        self.pygame.init()
        self.pygame.display.set_caption('Pong')

        # Sprites loaded
        board_img = self.pygame.image.load(self.sprites['board'])
    
        while True:
            
            # Show Game Here...
            self.show_board(board_img)

            # Quit the program...
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT: 
                    print('Quit Program')
                    self.pygame.quit()
                    quit()

            self.pygame.display.update() 

    def show_board(self, board_img_path):
        screen = self.pygame.display.set_mode(self.window_size)
        screen.blit(board_img_path, (0, 0))

if __name__ == '__main__':
    Game(pygame, game_sprites)
    