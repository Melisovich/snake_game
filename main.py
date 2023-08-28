import pygame
import random
import time

pygame.init()


window_width, window_height = 200, 200
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Змейка')


white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)


class Snake:
    def __init__(self):
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = 'RIGHT'
        self.change_to = self.direction

    def change_direction(self, new_direction):
        if new_direction == 'RIGHT' and not self.direction == 'LEFT':
            self.change_to = 'RIGHT'
        if new_direction == 'LEFT' and not self.direction == 'RIGHT':
            self.change_to = 'LEFT'
        if new_direction == 'UP' and not self.direction == 'DOWN':
            self.change_to = 'UP'
        if new_direction == 'DOWN' and not self.direction == 'UP':
            self.change_to = 'DOWN'

    def move(self, food_pos):
        if self.change_to == 'RIGHT':
            self.position[0] += 10
        if self.change_to == 'LEFT':
            self.position[0] -= 10
        if self.change_to == 'UP':
            self.position[1] -= 10
        if self.change_to == 'DOWN':
            self.position[1] += 10
        self.direction = self.change_to

        self.position[0] = self.position[0] % window_width
        self.position[1] = self.position[1] % window_height

        self.body.insert(0, list(self.position))
        if self.position == food_pos:
            return True
        else:
            self.body.pop()
            return False

    def check_collision(self):
        for segment in self.body[1:]:
            if segment == self.position:
                return True
        return False

    def get_head_position(self):
        return self.position

    def get_body(self):
        return self.body


def draw_snake(snake_body):
    for segment in snake_body:
        pygame.draw.rect(window, green, pygame.Rect(segment[0], segment[1], 10, 10))


def draw_food(food_position):
    pygame.draw.rect(window, red, pygame.Rect(food_position[0], food_position[1], 10, 10))


def show_game_over():
    font = pygame.font.SysFont('Arial', 36)
    game_over_text = font.render('Game Over', True, white)
    window.blit(game_over_text, (window_width // 2 - game_over_text.get_width() // 2,
                                 window_height // 2 - game_over_text.get_height() // 2))
    pygame.display.update()


def main():
    pygame.display.set_caption('Змейка')
    game_over = False
    snake = Snake()
    food = [random.randrange(1, (window_width // 10)) * 10,
            random.randrange(1, (window_height // 10)) * 10]

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.change_direction('LEFT')
                if event.key == pygame.K_RIGHT:
                    snake.change_direction('RIGHT')
                if event.key == pygame.K_UP:
                    snake.change_direction('UP')
                if event.key == pygame.K_DOWN:
                    snake.change_direction('DOWN')

        food_pos = food
        if snake.move(food_pos):
            food = [random.randrange(1, (window_width // 10)) * 10,
                    random.randrange(1, (window_height // 10)) * 10]

        if snake.check_collision():
            show_game_over()
            time.sleep(2)
            return

        window.fill(black)
        draw_snake(snake.get_body())
        draw_food(food)
        pygame.display.update()
        time.sleep(0.1)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
