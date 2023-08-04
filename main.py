import sys

import pygame

from models.snake import Snake
from models.game import Game
from models.display import Display
from models.food import Food

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
display = Display(DISPLAY_WIDTH, DISPLAY_HEIGHT)


def game_loop():
    food = Food()
    snake = Snake(DISPLAY_WIDTH, DISPLAY_HEIGHT)
    game = Game()
    clock = pygame.time.Clock()

    difficulty = display.check_event_difficulty()
    game.set_difficulty(difficulty)
    food.generate(DISPLAY_WIDTH, DISPLAY_HEIGHT, snake.size)

    while not game.is_over:
        while game.end_screen:
            display.screen.fill(display.white)
            display.message(
                "Game over! Press Escape to quit or Enter to play again.", display.red)
            display.score(snake.length-1)
            display.update()

            if game.keep_playing():
                game_loop()

        game.check_events_in_game(snake)
        snake.update_position(snake.x_pos_change, snake.y_pos_change)

        if display.border_hit(snake.x_pos, snake.y_pos):
            game.end_screen = True

        display.screen.fill(display.white)

        if snake.hit_self():
            game.end_screen = True

        food.render(display.screen, snake.size, color=display.blue)
        snake.render(display.screen, color=display.black)

        display.score(snake.length-1)

        display.update()

        if food.hit(snake.x_pos, snake.y_pos):
            food.generate(DISPLAY_WIDTH, DISPLAY_HEIGHT, snake.size)
            snake.grow()

        clock.tick(game.speed)

    pygame.quit()
    sys.exit()


game_loop()
