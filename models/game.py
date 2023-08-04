import pygame

pygame.init()
pygame.display.set_caption("Snake")


class Game:

    def __init__(self):
        self.is_over = False
        self.end_screen = False
        self.speed = 20

    def check_events_in_game(self, snake):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_over = True
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_LEFT:
                        if snake.direction != "right":
                            snake.x_pos_change = -snake.size
                            snake.y_pos_change = 0
                            snake.direction = "left"
                    case pygame.K_RIGHT:
                        if snake.direction != "left":
                            snake.x_pos_change = snake.size
                            snake.y_pos_change = 0
                            snake.direction = "right"
                    case pygame.K_UP:
                        if snake.direction != "down":
                            snake.x_pos_change = 0
                            snake.y_pos_change = -snake.size
                            snake.direction = "up"
                    case pygame.K_DOWN:
                        if snake.direction != "up":
                            snake.x_pos_change = 0
                            snake.y_pos_change = snake.size
                            snake.direction = "down"

    def keep_playing(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        return False
                    case pygame.K_RETURN:
                        return True
