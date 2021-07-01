from pygame import Vector2


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
    WIDTH = 693  
    HEIGHT = 364
    window_size = WIDTH, HEIGHT

    def __init__(self, pygame, sprites):
        self.pygame = pygame
        self.sprites = sprites
        
        # Window properties
        self.pygame.init()
        self.pygame.display.set_caption('Pong')

        # Sprites loaded
        board_img = self.pygame.image.load(self.sprites['board'])
        player1_img = self.pygame.image.load(self.sprites['player'])

        while True:
            
            # Show Game Here...
            self.screen = self.pygame.display.set_mode(self.window_size)
            self.show_board(board_img)
            self.show_player1(player1_img)
            
            player1_input = None
            for event in self.pygame.event.get():
                # Input Keys...
                if event.type == self.pygame.KEYDOWN: # This handles all the key pressed input
                    if event.key == self.pygame.K_w:
                        print('w pressed')
                    if event.key == self.pygame.K_s:
                        print('s pressed')
                
                if event.type == self.pygame.KEYUP: # This handles all the key released input
                    if event.key == self.pygame.K_w:
                        print('w released')
                    if event.key == self.pygame.K_s:
                        print('s released')
                        
                # Quit the program...   
                self.quit_handler(event)

            self.pygame.display.update() 

    def show_board(self, img):
        self.screen.blit(img, Vector2(0, 0))
        
    def show_player1(self, img):
        rect = img.get_rect()
        rect.center = pygame.Vector2(65, self.screen.get_height()/2)
        self.screen.blit(img, rect)

    def quit_handler(self, event):
        if event.type == self.pygame.QUIT: 
            print('Quit Program')
            self.pygame.quit()
            quit()

if __name__ == '__main__':
    Game(pygame, game_sprites)
    