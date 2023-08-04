import random

import pygame

from models.snake import Snake
from models.game import Game
from models.display import Display
from models.food import Food

display_width = 800
display_height = 600
display = Display(display_width, display_height)


def game_loop():

    food = Food()
    snake = Snake(display_width, display_height)
    game = Game()
    clock = pygame.time.Clock()
    food.generate(display_width, display_height, snake.size)

    while not game.is_over:
        while game.end_screen:
            display.screen.fill(display.white)
            display.message(
                "Game over! Press Escape to quit or Enter to play again.", display.red)
            display.score(snake.length-1)
            display.update()

            if game.keep_playing():
                game_loop()
            else:
                game.is_over = True
                game.end_screen = False

        game.check_events_in_game(snake)
        snake.update_position(snake.x_pos_change, snake.y_pos_change)

        if display.border_hit(snake.x_pos, snake.y_pos):
            game.end_screen = True

        display.screen.fill(display.white)

        snake.render(display.screen, color=display.black)
        food.render(display.screen, snake.size, color=display.blue)

        if snake.hit_self():
            game.end_screen = True

        snake.update(display.screen, color=display.black)
        display.score(snake.length-1)

        display.update()

        if food.hit(snake.x_pos, snake.y_pos):
            food.generate(display_width, display_height, snake.size)
            snake.grow()

        clock.tick(game.speed)

    pygame.quit()
    quit()


game_loop()
