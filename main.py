import pygame

pygame.init()

def main():

    screen = pygame.display.set_mode((800, 720))
    pygame.display.set_caption("Tetris")

    run = True

    while run:
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]:
            run = False

if __name__ == '__main__':
    main()