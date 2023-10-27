import pygame
from random import choice

from block import Block
from figure import Figure
from init import WINDOW_SIZE,BLOCK_SIZE, PLACE_SPACE_POS, PLACE_SPACE_SIZE, ALL_FIGURES, NUMBER_BLOCK_LINE


pygame.init()

def main():

    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    run = True
    placeSpace = pygame.Rect(PLACE_SPACE_POS, PLACE_SPACE_SIZE)

    all_figures = []

    a = 0

    form = [["_", "X", "_"],
            ["X", "X", "X"],
            ["_", "_", "_"]]

    currentFigure = Figure(0, 0,(255, 255, 255), choice(ALL_FIGURES))
    nextFigure = Figure(0, 0,(0, 0, 255), choice(ALL_FIGURES))
    all_figures.append(currentFigure)

    while run:
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (30, 30, 30), placeSpace)
        for figure in all_figures:
            figure.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                pressed = event.key
                if pressed == pygame.K_ESCAPE:
                    run = False
                if pressed == pygame.K_LEFT:
                    currentFigure.left()
                if pressed == pygame.K_RIGHT:
                    currentFigure.right()
                if pressed == pygame.K_UP:
                    currentFigure.up()
                if pressed == pygame.K_DOWN:
                    currentFigure.down()
                if pressed == pygame.K_KP0:
                    currentFigure.rotate()
        a += 1
        if a == 50:
            currentFigure.gravity(all_figures)
            a = 0

        if currentFigure.stun:

            for i in range(int(PLACE_SPACE_SIZE[1] / BLOCK_SIZE)):
                blockLine = 0
                blocks = []
                for figure in all_figures:
                    if len(figure.group) == 0:
                        all_figures.remove(figure)

                    for block in figure.group:
                        if block.y - PLACE_SPACE_POS[1] == BLOCK_SIZE * i:
                            blockLine += 1
                            blocks.append(block)
                if blockLine == NUMBER_BLOCK_LINE:
                    for figure in all_figures:
                        for block in blocks:
                            if block in figure.group:
                                figure.group.remove(block)
                                figure.blocksPlaces.remove((block.x - figure.x, block.y - figure.y))


            currentFigure = nextFigure
            all_figures.append(currentFigure)
            nextFigure = Figure(0, 0,(0, 0, 255), choice(ALL_FIGURES))

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()