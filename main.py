import sys

import pygame

from models.snake import Snake
from models.game import Game
from models.display import Display
from models.food import Food

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
display = Display(DISPLAY_WIDTH, DISPLAY_HEIGHT)


def game_on():
    food = Food()
    snake = Snake(DISPLAY_WIDTH, DISPLAY_HEIGHT)
    game = Game()
    clock = pygame.time.Clock()

    difficulty = game.check_event_difficulty(display)
    game.set_difficulty(difficulty)
    food.generate(DISPLAY_WIDTH, DISPLAY_HEIGHT, snake.size)

    while not game.is_over:
        while game.end_screen:
            display.screen.fill(display.white)
            display.game_over()
            display.score(snake.length-1)
            display.update()

            if game.keep_playing():
                game_on()

        game.check_event_in_game(snake)
        snake.update_position()

        if snake.hit_border():
            game.end_screen = True

        display.screen.fill(display.white)

        if snake.hit_self():
            game.end_screen = True

        food.render(display.screen, snake.size, color=display.blue)
        snake.render(display.screen, color=display.black)

        display.score(snake.length-1)

        display.update()

        if snake.hit_food(food.x_pos, food.y_pos):
            food.generate(DISPLAY_WIDTH, DISPLAY_HEIGHT, snake.size)
            snake.grow()

        clock.tick(game.speed)

    pygame.quit()
    sys.exit()


game_on()
