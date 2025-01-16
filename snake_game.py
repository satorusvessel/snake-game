import pygame
import random
import sys

def snake_game():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    snake = [(100, 50), (90, 50), (80, 50)]
    direction = "RIGHT"
    food = (random.randint(0, 39) * 10, random.randint(0, 29) * 10)
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and direction != "DOWN":
            direction = "UP"
        if keys[pygame.K_DOWN] and direction != "UP":
            direction = "DOWN"
        if keys[pygame.K_LEFT] and direction != "RIGHT":
            direction = "LEFT"
        if keys[pygame.K_RIGHT] and direction != "LEFT":
            direction = "RIGHT"

        head = snake[0]
        if direction == "UP":
            new_head = (head[0], head[1] - 10)
        elif direction == "DOWN":
            new_head = (head[0], head[1] + 10)
        elif direction == "LEFT":
            new_head = (head[0] - 10, head[1])
        elif direction == "RIGHT":
            new_head = (head[0] + 10, head[1])

        snake.insert(0, new_head)
        if new_head == food:
            food = (random.randint(0, 39) * 10, random.randint(0, 29) * 10)
        else:
            snake.pop()

        if (
            new_head[0] < 0 or new_head[1] < 0 or
            new_head[0] >= 400 or new_head[1] >= 300 or
            new_head in snake[1:]
        ):
            game_over = True

        screen.fill((0, 0, 0))
        for segment in snake:
            pygame.draw.rect(screen, (0, 255, 0), (*segment, 10, 10))
        pygame.draw.rect(screen, (255, 0, 0), (*food, 10, 10))
        pygame.display.flip()
        clock.tick(15)

    pygame.quit()

if __name__ == "__main__":
    snake_game()
