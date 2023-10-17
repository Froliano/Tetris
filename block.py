import pygame.draw


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.bg = (130, 130, 130)

        self.size = 32
        self.offset = 2

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg, pygame.Rect(self.x, self.y, self.size, self.size))
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x+self.offset, self.y+self.offset, self.size-self.offset*2, self.size-self.offset*2))

    def left(self):
        self.x -= 1

    def right(self):
        self.x += 1