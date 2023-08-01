import time

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

x1 = display_width/2
y1 = display_height/2
snake_block = 10
x1_change = 0
y1_change = 0

clock = pygame.time.Clock()
snake_speed = 30

font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
    msg = font_style.render(msg, True, color)
    msg_rect = msg.get_rect(center=(display_width/2, display_height/2))
    display.blit(msg, msg_rect)


def border_hit(x1, y1):
    if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
        return True


while not game_over:
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
        game_over = True

    x1 += x1_change
    y1 += y1_change
    display.fill(white)
    pygame.draw.rect(display, blue, [x1, y1, 10, 10])
    pygame.display.update()

    clock.tick(snake_speed)

message("GAME OVER", color=red)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()
