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

    allBlocks = []

    a = 0

    currentFigure = Figure(0, 0,(255, 255, 255), choice(ALL_FIGURES))
    nextFigure = Figure(0, 0,(0, 0, 255), choice(ALL_FIGURES))

    while run:
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (30, 30, 30), placeSpace)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                pressed = event.key
                if pressed == pygame.K_ESCAPE:
                    run = False
                if pressed == pygame.K_LEFT:
                    currentFigure.left(allBlocks)
                if pressed == pygame.K_RIGHT:
                    currentFigure.right(allBlocks)
                if pressed == pygame.K_UP:
                    currentFigure.up()
                if pressed == pygame.K_DOWN:
                    currentFigure.down(allBlocks)
                if pressed == pygame.K_KP0:
                    currentFigure.rotate(allBlocks)

        currentFigure.update(screen)
        for block in allBlocks:
            block.draw(screen)


        if currentFigure.stun:
            destroy = False

            for block in currentFigure.group:
                allBlocks.append(block)


            for i in range(int(PLACE_SPACE_SIZE[1] / BLOCK_SIZE), 0, -1):
                blockLine = 0
                blocks = []
                """for figure in all_figures:
                    if len(figure.group) == 0:
                        all_figures.remove(figure)"""

                for block in allBlocks:
                    if block.y - PLACE_SPACE_POS[1] == BLOCK_SIZE * i:
                        blockLine += 1
                        blocks.append(block)
                if blockLine == NUMBER_BLOCK_LINE:
                    destroy = True
                    for block in blocks:
                        allBlocks.remove(block)

            if destroy:
                for i in range(int(PLACE_SPACE_SIZE[1] / BLOCK_SIZE), 0, -1):
                    for block in allBlocks:
                        if block.y - PLACE_SPACE_POS[1] == BLOCK_SIZE * i:
                            block.fall(allBlocks)


            currentFigure = nextFigure
            nextFigure = Figure(0, 0, (0, 0, 255), choice(ALL_FIGURES))

        if a == 12:
            currentFigure.gravity(allBlocks)
            a = 0
        a += 1

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()