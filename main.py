import pygame
from block import Block
from figure import Figure
from init import WINDOW_SIZE, PLACE_SPACE_POS, PLACE_SPACE_SIZE, ALL_FIGURES


pygame.init()

def main():

    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    run = True
    placeSpace = pygame.Rect(PLACE_SPACE_POS, PLACE_SPACE_SIZE)

    a = 0

    form = [["_", "X", "_"],
            ["X", "X", "X"],
            ["_", "_", "_"]]

    figure = Figure(0, 0,(255, 255, 255), ALL_FIGURES[1])
    figure2 = Figure(0, 0,(0, 0, 255), ALL_FIGURES[0])

    while run:
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (30, 30, 30), placeSpace)
        figure.update(screen)

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
                if pressed == pygame.K_KP0:
                    figure.rotate()
        a += 1
        if a >= 100:
            figure.gravity()
            a = 0

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()