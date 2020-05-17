import pygame


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

running = True
while running:
    dt = clock.tick(60)  # 30 frame per 1 second
    # 2. handing with evnets (keyboard, mouse)
    for evnet in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 3. cope with character position
    

    # 4. process collision
    
    # 5. draw screen
    

    pygame.display.update()  # redrawing

# posed the game
pygame.time.delay(2000)

# pygame exit
pygame.quit()
