import pygame

pygame.init() # initialize

# set the size of screen

screen_width = 480 # width size
screen_height = 640 # height size
screen = pygame.display.set_mode((screen_width, screen_height))

# set the title of game
pygame.display.set_caption("Nado Game") # game title

# Loading the background image
# background = pygame.image.load(r"C:\Users\user01\python\nadocoding\game\background.png")

# even loop
running = True
while running:
    for event in pygame.event.get(): # which event raise?
        if event.type == pygame.QUIT: # The event which close windows raise
            running = False

    screen.fill((0,0,255))
    #screen.blit(background, (0,0)) # draw the background

    pygame.display.update() # redrawing 


# pygame exit
pygame.quit()   