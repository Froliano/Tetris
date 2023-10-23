import pygame
from block import Block
from init import BLOCK_SIZE, WINDOW_SIZE


class Figure:

    def __init__(self, x, y, color, image=[]):
        self.group = pygame.sprite.Group()
        self.color = color
        self.x = x
        self.y = y
        self.size = [0, 0]
        self.placeBlocks = []

        for y, list in enumerate(image):
            for x, char in enumerate(list):
                if char == "X":
                    self.placeBlocks.append((x*BLOCK_SIZE, y*BLOCK_SIZE))
                    self.group.add(Block(self.x+x*BLOCK_SIZE, self.y+y*BLOCK_SIZE, self.color))

                    if self.size[0] < (x+1)*BLOCK_SIZE:
                        self.size[0] = (x+1)*BLOCK_SIZE

                    if self.size[1] < (y+1)*BLOCK_SIZE:
                        self.size[1] = (y+1)*BLOCK_SIZE

    def update(self, screen):
        for i, block in enumerate(self.group):
            block.update(self.x + self.placeBlocks[i][0], self.y + self.placeBlocks[i][1])
        self.draw(screen)

    def draw(self, screen):
        for block in self.group:
            block.draw(screen)

    def left(self):
        self.x -= BLOCK_SIZE

    def right(self):
        self.x += BLOCK_SIZE

    def up(self):
        self.y -= BLOCK_SIZE

    def down(self):
        self.y += BLOCK_SIZE

    def collide(self, figure):
        for block in self.group:
            for blockTarget in figure.group:
                if block.collide(blockTarget):
                    return True
        return False

    def sideBorder(self):
        if self.x <= 0 or self.x + self.size[0] >= WINDOW_SIZE[0]:
            return True
        return False

    def gravity(self):
        self.down()