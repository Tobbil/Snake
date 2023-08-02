import time
import random

import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake")
game_over = False

snake_block = 10
snake_speed = 10

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 25)


def message(msg, color):
    msg = font_style.render(msg, True, color)
    msg_rect = msg.get_rect(center=(display_width/2, display_height/2))
    display.blit(msg, msg_rect)


def border_hit(x1, y1):
    if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
        return True


def game_loop():
    game_over = False
    game_close = False

    x1 = display_width/2
    y1 = display_height/2
    x1_change = 0
    y1_change = 0

    food_x = round(random.randrange(
        0, display_width - snake_block, snake_block))
    print(food_x)
    food_y = round(random.randrange(
        0, display_height - snake_block, snake_block))
    print(food_y)
    while not game_over:

        while game_close is True:
            display.fill(white)
            message("Game over! Press Escape to quit or Enter to play again.", red)
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
                        x1_change = -snake_block
                        y1_change = 0
                    case pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    case pygame.K_UP:
                        x1_change = 0
                        y1_change = -snake_block
                    case pygame.K_DOWN:
                        x1_change = 0
                        y1_change = snake_block

        if border_hit(x1, y1):
            game_close = True

        x1 += x1_change
        y1 += y1_change
        print(x1, y1)
        display.fill(white)
        pygame.draw.rect(display, blue, [x1, y1, snake_block, snake_block])
        pygame.draw.rect(display, black, [
                         food_x, food_y, snake_block, snake_block])
        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            print("Yum!")

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
