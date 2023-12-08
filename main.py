import pygame

from game import Game
from init import WINDOW_SIZE,BLOCK_SIZE, PLACE_SPACE_POS, PLACE_SPACE_SIZE, ALL_FIGURES, NUMBER_BLOCK_LINE

pygame.init()


def main():

    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    run = True
    placeSpace = pygame.Rect(PLACE_SPACE_POS, PLACE_SPACE_SIZE)
    game = Game(screen)

    while run:
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (30, 30, 30), placeSpace)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                game.addInput(event.key)

        game.update()

        pygame.display.flip()
        clock.tick(60)

        """if currentFigure.stun:
            destroy = False

            for block in currentFigure.group:
                allBlocks.append(block)


            for i in range(int(PLACE_SPACE_SIZE[1] / BLOCK_SIZE), 0, -1):
                blockLine = 0
                blocks = []
                for figure in all_figures:
                    if len(figure.group) == 0:
                        all_figures.remove(figure)

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
            nextFigure = Figure(0, 0, (0, 0, 255), choice(ALL_FIGURES))"""


if __name__ == '__main__':
    main()