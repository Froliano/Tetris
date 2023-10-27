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

        self.rotate()

    def update(self, screen):
        for i, block in enumerate(self.group):
            block.update(self.x + self.blocksPlaces[i][0], self.y + self.blocksPlaces[i][1])
        self.draw(screen)

    def draw(self, screen):
        for block in self.group:
            block.draw(screen)

    def collide(self, figure):
        for block in self.group:
            for blockTarget in figure.group:
                if block.collide(blockTarget):
                    return True
        return False

    def sideBorder(self):
        if self.x < PLACE_SPACE_POS[0] or self.x + self.size[0] > PLACE_SPACE_SIZE[0]+ PLACE_SPACE_POS[0]:
            return True
        return False

    def rotate(self):
        self.currentIndexImage = self.currentIndexImage % 4 +1
        self.currentImage = self.images[self.currentIndexImage]
        self.group = pygame.sprite.Group()
        self.blocksPlaces = []
        self.size = [0, 0]

        for y, list in enumerate(self.currentImage):
            for x, char in enumerate(list):
                if char == "X":
                    self.blocksPlaces.append((x*BLOCK_SIZE, y*BLOCK_SIZE))
                    self.group.add(Block(self.x+x*BLOCK_SIZE, self.y+y*BLOCK_SIZE, self.color))

                    if self.size[0] < (x+1)*BLOCK_SIZE:
                        self.size[0] = (x+1)*BLOCK_SIZE

                    if self.size[1] < (y+1)*BLOCK_SIZE:
                        self.size[1] = (y+1)*BLOCK_SIZE
        if self.sideBorder() or self.y + self.size[1] > PLACE_SPACE_POS[1] + PLACE_SPACE_SIZE[1]:
            self.currentIndexImage -= 2
            self.rotate()


    def left(self):
        x, y = self.x, self.y
        self.x -= BLOCK_SIZE
        if self.sideBorder():
            self.x, self.y = x, y

    def right(self):
        x, y = self.x, self.y
        self.x += BLOCK_SIZE
        if self.sideBorder():
            self.x, self.y = x, y

    def up(self):
        self.y -= BLOCK_SIZE

    def down(self):
        if self.y + self.size[1] < PLACE_SPACE_POS[1] + PLACE_SPACE_SIZE[1]:
            self.y += BLOCK_SIZE

    def gravity(self):
        if self.y + self.size[1] < PLACE_SPACE_POS[1] + PLACE_SPACE_SIZE[1]:
            self.down()