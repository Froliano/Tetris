import pygame.draw


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.bg = (130, 130, 130)

        self.size = 64
        self.offset = 4

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg, pygame.Rect(self.x, self.y, self.size, self.size))
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x+self.offset, self.y+self.offset, self.size-self.offset*2, self.size-self.offset*2))

    def collide(self, block):
        #verifier si le coin en bas à droite du block est dans le block self
        if self.x >= block.x and self.x <= block.x + block.size and self.y >= block.y and self.y <= block.y + block.size:
            return True

        # verifier si le coin en haut à droite du block est dans le block self
        if self.x >= block.x and self.x <= block.x + block.size and self.y + self.size >= block.y and self.y + self.size <= block.y + block.size:
            return True

        # verifier si le coin en bas à gauche du block est dans le block self
        if self.x + self.size >= block.x and self.x + self.size <= block.x + block.size and self.y >= block.y and self.y <= block.y + block.size:
            return True

        # verifier si le coin en haut à gauche du block est dans le block self
        if self.x + self.size >= block.x and self.x + self.size <= block.x + block.size and self.y + self.size >= block.y and self.y + self.size <= block.y + block.size:
            return True

        return False

    def left(self):
        self.x -= 1

    def right(self):
        self.x += 1

    def top(self):
        self.y -= 1

    def down(self):
        self.y += 1