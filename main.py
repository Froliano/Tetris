import pygame
from block import Block

pygame.init()

def main():

    screen = pygame.display.set_mode((800, 720))
    pygame.display.set_caption("Tetris")
    group = pygame.sprite.Group()
    run = True
    block = Block(10, 10, (255, 255, 255))
    block2 = Block(500, 10, (255, 0, 0))
    group.add(block)
    group.add(block2)

    while run:
        screen.fill((0, 0, 0))
        block.draw(screen)
        block2.draw(screen)


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


        pygame.display.flip()

if __name__ == '__main__':
    main()