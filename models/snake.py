import pygame


class Snake:

    def __init__(self, display_width, display_height):
        self.display_width = display_width
        self.display_height = display_height
        self.snake_list = []
        self.length = 1
        self.direction = None
        self.size = 10
        self.x_pos = display_width/2
        self.y_pos = display_height/2
        self.x_pos_change = 0
        self.y_pos_change = 0
        self.snake_head = []

    def update_position(self):
        self.x_pos += self.x_pos_change
        self.y_pos += self.y_pos_change

    def hit_self(self):
        self.snake_head = []
        self.snake_head.append(self.x_pos)
        self.snake_head.append(self.y_pos)
        self.snake_list.append(self.snake_head)

        if len(self.snake_list) > self.length:
            del self.snake_list[0]

        for x in self.snake_list[:-1]:
            if x == self.snake_head:
                return True

        return False

    def hit_border(self):
        if any((self.x_pos >= self.display_width, self.x_pos < 0, self.y_pos >= self.display_height, self.y_pos < 0)):
            return True

    def hit_food(self, food_x_pos, food_y_pos):
        return (self.x_pos == food_x_pos and self.y_pos == food_y_pos)

    def render(self, screen, color):
        for x in self.snake_list:
            pygame.draw.rect(screen, color, [
                x[0], x[1], self.size, self.size])

    def grow(self):
        self.length += 1
