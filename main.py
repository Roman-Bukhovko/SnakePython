import pygame as pygame
from random import randrange

WINDOW = 1000
TILE_SIZE = 50
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
get_random_postion = lambda: [randrange(*RANGE), randrange(*RANGE)]
snake = pygame.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = get_random_postion()
length = 1
segments = [snake.copy()]
snake_dir = (0, 0)
time, time_step = 0, 110
food = snake.copy()
food.center = get_random_postion()
screen = pygame.display.set_mode([WINDOW] * 2)
clock = pygame.time.Clock()
dirs = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 1}

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                snake_dir = (0, -TILE_SIZE)
                dirs = {pygame.K_w: 1, pygame.K_s: 0, pygame.K_a: 1, pygame.K_d: 1}
            if event.key == pygame.K_s: 
                snake_dir = (0, TILE_SIZE)    
                dirs = {pygame.K_w: 0, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 1}
            if event.key == pygame.K_a:
                snake_dir = (-TILE_SIZE, 0)
                dirs = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 0}
            if event.key == pygame.K_d: 
                snake_dir = (TILE_SIZE, 0)   
                dirs = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 0, pygame.K_d: 1}
    screen.fill('black')
    self_eating = pygame.Rect.collidelist(snake, segments[:-1]) != -1 
    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
        snake.center, food.center = get_random_postion(), get_random_postion()
        length, snake_dir = 1, (0, 0)
        segements = [snake.copy()]
    if snake.center == food.center:
        food.center = get_random_postion()
        length += 1
    pygame.draw.rect(screen, 'red', food)
    [pygame.draw.rect(screen, 'blue', segment) for segment in segments]
    time_now = pygame.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]
    pygame.display.flip()
    clock.tick(60)
