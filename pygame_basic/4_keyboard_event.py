import pygame

pygame.init() # initialize

# set the size of screen

screen_width = 480 # width size
screen_height = 640 # height size
screen = pygame.display.set_mode((screen_width, screen_height))

# set the title of game
pygame.display.set_caption("Nado Game") # game title

# Loading the background image
background = pygame.image.load(r"C:\Users\user01\python\nadocoding\game\background.png")

# loading characters
character = pygame.image.load(r"C:\Users\user01\python\nadocoding\game\character.png")
character_size = character.get_rect().size # get the image size
character_width = character_size[0] # character's width
character_height = character_size[1] # characeter's height
character_x_pos = (screen_width / 2) - (character_width / 2) # the middle of screen width
character_y_pos = screen_height - character_height # the bottom of screen heigth 

# move position
to_x = 0
to_y = 0

# even loop
running = True
while running:
    for event in pygame.event.get(): # which event raise?
        if event.type == pygame.QUIT: # The event which close windows raise
            running = False

        if event.type == pygame.KEYDOWN: # check if key is pressed.
            if event.key == pygame.K_LEFT:
                to_x -= 5 
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    # width boundary limit
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # screen.fill((0,0,255))
    screen.blit(background, (0,0)) # draw the background
    
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # redrawing 

# pygame exit
pygame.quit()
