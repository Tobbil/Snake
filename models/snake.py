import pygame


class Snake:

    def __init__(self, display):
        self.display = display
        self.size = 10
        self.length = 1
        self.direction = None
        self.x_pos = display.display_width/2
        self.y_pos = display.display_height/2
        self.x_pos_change = 0
        self.y_pos_change = 0

    def render(self, display, snake_list, color):
        for x in snake_list:
            pygame.draw.rect(display, color, [
                x[0], x[1], self.size, self.size])

    def set_starting_position(self):
        self.x_pos = self.display.display_width/2
        self.y_pos = self.display.display_height/2

    def update_position(self, x_change, y_change):
        self.x_pos += x_change
        self.y_pos += y_change
