import pygame


class Display:

    white = (255, 255, 255)
    yellow = (255, 255, 102)
    green = (0, 255, 0)
    black = (0, 0, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    main_font = pygame.font.SysFont("bahnschrift", 30)
    score_font = pygame.font.SysFont("calibri", 25)

    def __init__(self, display_width, display_height):
        self.display_width = display_width
        self.display_height = display_height
        self.screen = pygame.display.set_mode((display_width, display_height))

    def message(self, msg, color):
        msg = self.main_font.render(msg, True, color)
        msg_rect = msg.get_rect(
            center=(self.display_width/2, self.display_height/2))
        self.screen.blit(msg, msg_rect)

    def score(self, score):
        score_msg = self.score_font.render(
            f"Your score: {score}", True, self.black)
        self.screen.blit(
            score_msg, [self.display_width-self.display_width/5, 0])

    def game_over(self):
        self.message(
            "Game over! Press Escape to quit or Enter to play again.", self.red)

    def draw_rect(self, color, x_pos, y_pos, x_size, y_size):
        pygame.draw.rect(self.screen, color, [x_pos, y_pos, x_size, y_size])

    def update(self):
        pygame.display.update()
