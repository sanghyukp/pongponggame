import pygame

pygame.init() # initialize

# set the size of screen

screen_width = 480 # width size
screen_height = 640 # height size
pygame.display.set_mode((screen_width, screen_height))

# set the title of game
pygame.display.set_caption("Nado Game") # game title

# even loop
running = True
while running:
    for event in pygame.event.get(): # which event raise?
        if event.type == pygame.QUIT: # The event which close windows raise
            running = False


# pygame exit
pygame.quit()   