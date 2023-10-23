import pygame
from block import Block


class Figure:

    def __init__(self, x, y, color, image=[]):
        self.group = pygame.sprite.Group()
        self.color = color
        self.x = x
        self.y = y

        for y, list in enumerate(image):
            for x, char in enumerate(list):
                if char == "X":
                    self.group.add(Block(self.x+x*64, self.y+y*64, self.color))

    def draw(self, screen):
        for block in self.group:
            block.draw(screen)

    def left(self):
        self.x -= 1
        for block in self.group:
            block.left()

    def right(self):
        self.x += 1
        for block in self.group:
            block.right()

    def up(self):
        self.y -= 1
        for block in self.group:
            block.up()

    def down(self):
        self.y += 1
        for block in self.group:
            block.down()

    def collide(self, figure):
        for block in self.group:
            for blockTarget in figure.group:
                if block.collide(blockTarget):
                    return True
        return False