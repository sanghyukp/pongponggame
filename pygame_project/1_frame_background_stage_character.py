import pygame
import os


##########################################
# Initialize settings of game

pygame.init()  # initialize

# set the size of screen

screen_width = 640  # width size
screen_height = 480  # height size
screen = pygame.display.set_mode((screen_width, screen_height))

# set the title of game
pygame.display.set_caption("Nado Pong")  # game title

# FPS
clock = pygame.time.Clock()
##########################################

# 1. user game initialization (background, images, position, font, speed, and so on)

current_path = os.path.dirname(__file__) # get current directory path including the current file
image_path = os.path.join(current_path, "images")

# Background
background = pygame.image.load(os.path.join(image_path, "background.png"))

# Stage
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # limit  objects of game to inner frame 

# Character
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - (character_height + stage_height)


running = True
while running:
    dt = clock.tick(60)  # 30 frame per 1 second
    # 2. handing with evnets (keyboard, mouse)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 3. cope with character position
    

    # 4. process collision
    
    # 5. draw screen
    screen.blit(background, (0,0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    

    pygame.display.update()  # redrawing

# posed the game
pygame.time.delay(2000)

# pygame exit
pygame.quit()
