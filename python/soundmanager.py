import pygame

pygame.init()

class SoundManager:
    def __init__(self):
        self.paddle = pygame.mixer.Sound('./sound/Paddle.wav')
        self.score = pygame.mixer.Sound('./sound/Score.wav')
        self.hit = pygame.mixer.Sound('./sound/Hit.wav')

    def play(self, sound):
        if sound == 'paddle':
            self.paddle.play()
        if sound == 'score':
            self.score.play()
        if sound == 'hit':
            self.hit.play()