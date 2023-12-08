import pygame
from random import choice
from figure import Figure
from init import ALL_FIGURES

class Game:

    def __init__(self, screen):
        self.screen = screen

        self.clock = 20

        self.pressed = []
        self.allblocks = []
        self.currentFigure = Figure(0, 0, (255, 255, 255), choice(ALL_FIGURES))
        self.nextFigure = Figure(0, 0, (0, 0, 255), choice(ALL_FIGURES))

    def update(self):
        self.input()

        self.currentFigure.update(self.screen)
        for block in self.allblocks:
            block.draw(self.screen)

        if self.clock == 100:
            self.currentFigure.gravity()
            self.clock = 0
        self.clock += 1

    def input(self):
        if pygame.K_LEFT in self.pressed:
            self.currentFigure.left()
        if pygame.K_RIGHT in self.pressed:
            self.currentFigure.right()
        if pygame.K_UP in self.pressed:
            self.currentFigure.up()
        if pygame.K_DOWN in self.pressed:
            self.currentFigure.down()
        """if pygame.K_KP0 in self.pressed:
            self.rotate()"""

    def addInput(self, input):
        self.pressed.append(input)
        print(self.pressed)
