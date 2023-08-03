import pygame


class Snake:

    def __init__(self):
        self.size = 10

    def render(self, display, snake_list, color):
        for x in snake_list:
            pygame.draw.rect(display, color, [
                x[0], x[1], self.size, self.size])
