import pygame
from block import Block
from init import BLOCK_SIZE, WINDOW_SIZE, PLACE_SPACE_POS, PLACE_SPACE_SIZE


class Figure:

    def __init__(self, x, y, color, images={}):
        self.color = color
        self.x = (x + PLACE_SPACE_POS[0]) % PLACE_SPACE_SIZE[0]
        self.y = (y + PLACE_SPACE_POS[1]) % PLACE_SPACE_SIZE[1]

        self.images = images
        self.currentIndexImage = 0
        self.stun = False

        self.pressed = []

        self.init()

    def update(self, screen):
        self.draw(screen)

    def draw(self, screen):
        for block in self.group:
            block.draw(screen)

    def collide(self, figure):
        for block in self.group:
            for blockTarget in figure:
                if block.sideCollide(blockTarget) and block.bottomCollide(blockTarget):
                    return True
        return False

    def init(self):
        self.currentIndexImage = self.currentIndexImage % 4 +1
        self.currentImage = self.images[self.currentIndexImage]
        self.group = []

        for y, list in enumerate(self.currentImage):
            for x, char in enumerate(list):
                if char == "X":
                    self.group.append(Block(self.x+x*BLOCK_SIZE, self.y+y*BLOCK_SIZE, self.color))

        """if self.sideBorder() or self.y + self.size[1] > PLACE_SPACE_POS[1] + PLACE_SPACE_SIZE[1] or self.collide(blocks):
            self.currentIndexImage -= 2
            self.rotate([])"""

    def left(self):
        self.x -= BLOCK_SIZE
        for block in self.group:
            block.left()

    def right(self):
        self.x += BLOCK_SIZE
        for block in self.group:
            block.right()

    def up(self):
        self.y -= BLOCK_SIZE
        for block in self.group:
            block.up()

    def down(self):
        self.gravity()
        for block in self.group:
            block.down()

    def gravity(self):
        self.y += BLOCK_SIZE
        for block in self.group:
            block.down()