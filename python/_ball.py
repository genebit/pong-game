import pygame

import soundmanager

sound_manager = soundmanager.SoundManager()

class Ball:

    ball = None
    window = None

    def __init__(self, window):
        self.window = window
        self.ball = pygame.Rect(0, 0, 30, 30)
        self.ball.center = (window.get_width()/2, window.get_height()/2)

    def draw(self, ballspeed, p1, p2):
        self.ball = self.ball.move(ballspeed)

        P1_COLLIDED = self.ball.colliderect(p1)
        P2_COLLIDED = self.ball.colliderect(p2)

        # Checks if the collider hits the border
        # Converts the speed to move negative to bounce back
        if self.ball.left < 0 or self.ball.right > self.window.get_width(): 
            ballspeed[0] = -ballspeed[0] 
            sound_manager.play('hit')

        if self.ball.top < 0 or self.ball.bottom > self.window.get_height():
            ballspeed[1] = -ballspeed[1]
            sound_manager.play('hit')
        
        # Player Paddle Collide
        if P1_COLLIDED or P2_COLLIDED:
            ballspeed[0] = -ballspeed[0] + ballspeed[1]
            ballspeed[1] = -ballspeed[1] + ballspeed[0]
            sound_manager.play('paddle')

        pygame.draw.rect(self.window, (255, 255, 255), self.ball, 3)
