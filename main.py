import pygame
from block import Block
from figure import Figure


pygame.init()

def main():

    screen = pygame.display.set_mode((800, 720))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    run = True

    block = Block(100, 60, (255, 255, 255))

    form = [["_", "X", "_"],
            ["X", "X", "X"],
            ["_", "_", "_"]]

    figure = Figure(0, 0,(255, 255, 255), form)

    while run:
        screen.fill((0, 0, 0))
        figure.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]:
            run = False
        if pressed[pygame.K_LEFT]:
            block.left()
        if pressed[pygame.K_RIGHT]:
            block.right()
        if pressed[pygame.K_UP]:
            block.top()
        if pressed[pygame.K_DOWN]:
            block.down()


        pygame.display.flip()
        clock.tick(100)

if __name__ == '__main__':
    main()