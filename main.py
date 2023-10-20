import pygame
from block import Block


pygame.init()

def main():

    screen = pygame.display.set_mode((800, 720))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    run = True

    block = Block(100, 60, (255, 255, 255))
    block2 = Block(10, 10, (255, 0, 0))


    group = pygame.sprite.Group()
    group.add(block)
    group.add(block2)

    while run:
        screen.fill((0, 0, 0))
        block.draw(screen)
        block2.draw(screen)
        if not block.collide(block2):
            print("ok")


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]:
            run = False
        if pressed[pygame.K_LEFT]:
            block2.left()
        if pressed[pygame.K_RIGHT]:
            block2.right()
        if pressed[pygame.K_UP]:
            block2.top()
        if pressed[pygame.K_DOWN]:
            block2.down()


        pygame.display.flip()
        clock.tick(100)

if __name__ == '__main__':
    main()