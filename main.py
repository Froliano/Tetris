import pygame
from block import Block
from figure import Figure
from init import WINDOW_SIZE


pygame.init()

def main():

    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    run = True
    a = 0

    form = [["_", "X", "_"],
            ["X", "X", "X"],
            ["_", "_", "_"]]

    figure = Figure(0, 0,(255, 255, 255), form)
    figure2 = Figure(128, 128,(0, 0, 255), form)

    while run:
        screen.fill((0, 0, 0))
        figure.update(screen)
        figure2.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                pressed = event.key
                if pressed == pygame.K_ESCAPE:
                    run = False
                if pressed == pygame.K_LEFT:
                    figure.left()
                if pressed == pygame.K_RIGHT:
                    figure.right()
                if pressed == pygame.K_UP:
                    figure.up()
                if pressed == pygame.K_DOWN:
                    figure.down()
        a += 1
        if a >= 100:
            figure.gravity()
            a = 0

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()