import pygame

class Input:

    def p1_movement(window, player1, keypressed, p1velo, playerspeed):
        
        if keypressed[pygame.K_w] and not keypressed[pygame.K_s]:
            p1velo = [0, -playerspeed] if player1.top > 0 else [0, 0]
        elif keypressed[pygame.K_s] and not keypressed[pygame.K_w]:
            p1velo = [0, playerspeed] if player1.bottom < window.get_height() else [0, 0]        
        else:
            p1velo = [0, 0]
        return p1velo

    def p2_movement(window, player2, keypressed, p2velo, playerspeed):

        if keypressed[pygame.K_UP] and not keypressed[pygame.K_DOWN]:
            p2velo = [0, -playerspeed] if player2.top > 0 else [0, 0]
        elif keypressed[pygame.K_DOWN] and not keypressed[pygame.K_UP]:
            p2velo = [0, playerspeed] if player2.bottom < window.get_height() else [0, 0]        
        else:
            p2velo = [0, 0]
        return p2velo