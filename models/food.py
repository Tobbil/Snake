import random

import pygame


class Food:

    def __init__(self):
        self.x_pos = None
        self.y_pos = None

    def generate(self, display_width, display_height, snake_size):
        self.x_pos = round(random.randrange(
            0, display_width - snake_size, snake_size))
        self.y_pos = round(random.randrange(
            0, display_height - snake_size, snake_size))

    def render(self, screen, snake_size, color):
        pygame.draw.rect(
            screen, color, [self.x_pos, self.y_pos, snake_size, snake_size])
