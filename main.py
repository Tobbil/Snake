import random

import pygame

from models.snake import Snake
from models.game import Game

game = Game()
snake = Snake()


white = (255, 255, 255)
yellow = (255, 255, 102)
green = (0, 255, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))
game_over = False

snake_speed = 20

clock = pygame.time.Clock()


def message(msg, color):
    msg = game.main_font.render(msg, True, color)
    msg_rect = msg.get_rect(center=(display_width/2, display_height/2))
    screen.blit(msg, msg_rect)


def display_score(score):
    score_msg = game.score_font.render(
        f"Your score: {score}", True, black)
    screen.blit(score_msg, [display_width-display_width/3, 0])


def border_hit(x1, y1):
    if any((x1 >= display_width, x1 < 0, y1 >= display_height, y1 < 0)):
        return True


def game_loop():
    game_over = False
    game_close = False

    x1 = display_width/2
    y1 = display_height/2
    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1
    direction = None

    food_x = round(random.randrange(
        0, display_width - snake.size, snake.size))
    print(food_x)
    food_y = round(random.randrange(
        0, display_height - snake.size, snake.size))
    print(food_y)
    while not game_over:

        while game_close is True:
            screen.fill(white)
            message(
                "Game over! Press Escape to quit or Enter to play again.", red)
            display_score(snake_length-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            game_over = True
                            game_close = False
                        case pygame.K_RETURN:
                            game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_LEFT:
                        if direction != "right":
                            x1_change = -snake.size
                            y1_change = 0
                            direction = "left"
                    case pygame.K_RIGHT:
                        if direction != "left":
                            x1_change = snake.size
                            y1_change = 0
                            direction = "right"
                    case pygame.K_UP:
                        if direction != "down":
                            x1_change = 0
                            y1_change = -snake.size
                            direction = "up"
                    case pygame.K_DOWN:
                        if direction != "up":
                            x1_change = 0
                            y1_change = snake.size
                            direction = "down"

        if border_hit(x1, y1):
            game_close = True

        x1 += x1_change
        y1 += y1_change
        print(x1, y1)
        screen.fill(white)
        pygame.draw.rect(screen, blue, [
                         x1, y1, snake.size, snake.size])
        pygame.draw.rect(screen, blue, [
                         food_x, food_y, snake.size, snake.size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        snake.render(screen, snake_list, color=black)
        display_score(snake_length-1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(
                0, display_width - snake.size, snake.size))
            print(food_x)
            food_y = round(random.randrange(
                0, display_height - snake.size, snake.size))
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
