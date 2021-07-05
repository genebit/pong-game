
import pygame

# TODO: Colliders

def draw_objects(window):
    img = pygame.image.load('./test/img/happy.png')

    img_rect = img.get_rect()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    img_rect.center = (mouse_x, mouse_y)

    window.blit(img, img_rect)

    RED = (250, 54, 40)
    pygame.draw.rect(window, RED, img_rect, 2)

    
def main():
    
    WINDOW = pygame.display.set_mode((500, 400))

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Draw Here
        BLACK = (26, 26, 26)
        WINDOW.fill(BLACK)

        draw_objects(WINDOW)
        pygame.display.update()

if __name__ == '__main__':
    print('Running Test')
    main()