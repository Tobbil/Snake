import random

import pygame

from models.snake import Snake
from models.game import Game
from models.display import Display

display_width = 800
display_height = 600

game = Game()
display = Display(display_width, display_height)
snake = Snake(display)

clock = pygame.time.Clock()


def game_loop():
    game.is_over = False
    game.end_screen = False
    snake_list = []
    snake.length = 1
    snake.direction = None
    snake.set_starting_position()

    x_change = 0
    y_change = 0

    food_x = round(random.randrange(
        0, display_width - snake.size, snake.size))
    print(food_x)
    food_y = round(random.randrange(
        0, display_height - snake.size, snake.size))
    print(food_y)
    while not game.is_over:

        while game.end_screen is True:
            display.screen.fill(display.white)
            display.message(
                "Game over! Press Escape to quit or Enter to play again.", display.red)
            display.score(snake.length-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            game.is_over = True
                            game.end_screen = False
                        case pygame.K_RETURN:
                            game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.is_over = True
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_LEFT:
                        if snake.direction != "right":
                            x_change = -snake.size
                            y_change = 0
                            snake.direction = "left"
                    case pygame.K_RIGHT:
                        if snake.direction != "left":
                            x_change = snake.size
                            y_change = 0
                            snake.direction = "right"
                    case pygame.K_UP:
                        if snake.direction != "down":
                            x_change = 0
                            y_change = -snake.size
                            snake.direction = "up"
                    case pygame.K_DOWN:
                        if snake.direction != "up":
                            x_change = 0
                            y_change = snake.size
                            snake.direction = "down"

        snake.update_position(x_change, y_change)

        if display.border_hit(snake.x_pos, snake.y_pos):
            game.end_screen = True

        print(snake.x_pos, snake.y_pos)
        display.screen.fill(display.white)
        pygame.draw.rect(display.screen, display.blue, [
                         snake.x_pos, snake.y_pos, snake.size, snake.size])
        pygame.draw.rect(display.screen, display.blue, [
                         food_x, food_y, snake.size, snake.size])
        snake_head = []
        snake_head.append(snake.x_pos)
        snake_head.append(snake.y_pos)
        snake_list.append(snake_head)
        if len(snake_list) > snake.length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game.end_screen = True

        snake.render(display.screen, snake_list, color=display.black)
        display.score(snake.length-1)

        pygame.display.update()

        if snake.x_pos == food_x and snake.y_pos == food_y:
            food_x = round(random.randrange(
                0, display_width - snake.size, snake.size))
            print(food_x)
            food_y = round(random.randrange(
                0, display_height - snake.size, snake.size))
            snake.length += 1

        clock.tick(game.speed)

    pygame.quit()
    quit()


game_loop()
