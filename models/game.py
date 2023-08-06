import pygame

pygame.init()
pygame.display.set_caption("Snake")


class Game:

    def __init__(self):
        self.is_over = False
        self.end_screen = False
        self.speed = None

    def check_event_difficulty(self, display):
        display.screen.fill(display.white)
        display.message("Choose difficulty: 1) Easy 2) Normal 3) Hard 4) Ultra Hard",
                        display.black)
        display.update()
        choice = False
        while choice is False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    choice = True
                    return -1
                if event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_0:
                            choice = True
                            return -1
                        case pygame.K_1:
                            choice = True
                            return 1
                        case pygame.K_2:
                            choice = True
                            return 2
                        case pygame.K_3:
                            choice = True
                            return 3
                        case pygame.K_4:
                            choice = True
                            return 4

    def check_event_in_game(self, snake):
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
                        self.is_over = True
                        self.end_screen = False
                        return False
                    case pygame.K_RETURN:
                        return True

    def set_difficulty(self, difficulty):
        match difficulty:
            case -1:
                self.is_over = True
            case 1:
                self.speed = 20
            case 2:
                self.speed = 25
            case 3:
                self.speed = 35
            case 4:
                self.speed = 40
