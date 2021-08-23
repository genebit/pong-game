import pygame

class Text:
    
    gameover_txt = None
    gameover_rect = None
    info_txt = None
    info_rect = None

    def __init__(self, window):

        FONT = pygame.font.Font('./font/Welbut.ttf', 30)
        
        self.gameover_txt =  FONT.render('GAME OVER', True, (255, 255, 255))
        self.gameover_rect = self.gameover_txt.get_rect()
        self.gameover_rect.center = (window.get_width()/2, window.get_height()/2 -20)

        self.info_txt = FONT.render("Press 'R' to Restart", True, (255, 255, 255))
        self.info_rect = self.info_txt.get_rect()
        self.info_rect.center = (window.get_width()/2, self.gameover_rect.bottom +20)

    def show_gameover(self, window):
        
        window.blit(self.gameover_txt, self.gameover_rect)
        window.blit(self.info_txt, self.info_rect)