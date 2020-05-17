import pygame
import random

##########################################
# Initialize settings of game

pygame.init()  # initialize

# set the size of screen

screen_width = 480  # width size
screen_height = 640  # height size
screen = pygame.display.set_mode((screen_width, screen_height))

# set the title of game
pygame.display.set_caption("Pong Pong")  # game title

# FPS
clock = pygame.time.Clock()
##########################################

# 1. user game initialization (background, images, position, font, speed, and so on)

# background
background = pygame.image.load(
    r"C:\Users\user01\python\nadocoding\game\background.png")

# character
character = pygame.image.load(
    r"C:\Users\user01\python\nadocoding\game\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height



# move position
to_x = 0

character_speed = 10

# enemy
enemy = pygame.image.load(r"C:\Users\user01\python\nadocoding\game\enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 10

running = True
while running:
    dt = clock.tick(30)  # 30 frame per 1 second
    # 2. handing with events (keyboard, mouse)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. cope with character position
    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    # 4. process collision
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    if character_rect.colliderect(enemy_rect):
        print("collision occurs")
        running = False
    
    # 5. draw screen
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update()  # redrawing

# posed the game
pygame.time.delay(2000)

# pygame exit
pygame.quit()
