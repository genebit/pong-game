import pygame

class Player1:
    
    player1 = None

    def __init__(self, window):
        self.player1 = pygame.Rect(0, 0, 20, 60)
        self.player1.center = (50, window.get_height()/2)

    def draw(self, window, p1velo):
        self.player1 = self.player1.move(p1velo)
        pygame.draw.rect(window, (255, 255, 255), self.player1, 3)

class Player2:
    
    player2 = None

    def __init__(self, window):
        self.player2 = pygame.Rect(0, 0, 20, 60)
        self.player2.center = (550, window.get_height()/2)

    def draw(self, window, p2velo):
        self.player2 = self.player2.move(p2velo)
        pygame.draw.rect(window, (255, 255, 255), self.player2, 3)