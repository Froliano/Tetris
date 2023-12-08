import pygame.draw
from init import BLOCK_SIZE, PLACE_SPACE_POS, PLACE_SPACE_SIZE


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.bg = (130, 130, 130)

        self.size = BLOCK_SIZE
        self.offset = 4

    def update(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg, pygame.Rect(self.x, self.y, self.size, self.size))
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x+self.offset, self.y+self.offset, self.size-self.offset*2, self.size-self.offset*2))

    def sideCollide(self, block):
        if self.y == block.y:
            if self.x + self.size + 1 == block.x or self.x == block.x + block.size + 1:
                return True
        if self.x == PLACE_SPACE_POS[0] or self.x + self.size[0] == PLACE_SPACE_SIZE[0] + PLACE_SPACE_POS[0]:
            return True
        return False

    def bottomCollide(self, block):
        if self.x == block.x and self.y + self.size + 1 == block.y:
            return True
        if self.y + self.size == PLACE_SPACE_SIZE[1] + PLACE_SPACE_POS[1]:
            return True
        return False

    def left(self):
        self.x -= self.size

    def right(self):
        self.x += self.size

    def up(self):
        self.y -= self.size

    def down(self):
        self.y += self.size

    def fall(self, blocks):
        x, y = self.x, self.y
        if self.y + self.size < PLACE_SPACE_POS[1] + PLACE_SPACE_SIZE[1]:
            self.y += self.size
            for block in blocks:
                if self.collide(block) and not self == block:
                    self.x, self.y = x, y

