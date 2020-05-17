import pygame

pygame.init()  # initialize

# set the size of screen

screen_width = 480  # width size
screen_height = 640  # height size
screen = pygame.display.set_mode((screen_width, screen_height))

# set the title of game
pygame.display.set_caption("Nado Game")  # game title

# FPS
clock = pygame.time.Clock()

# Loading the background image
background = pygame.image.load(
    r"C:\Users\user01\python\nadocoding\game\background.png")

# loading characters
character = pygame.image.load(
    r"C:\Users\user01\python\nadocoding\game\character.png")
character_size = character.get_rect().size  # get the image size
character_width = character_size[0]  # character's width
character_height = character_size[1]  # characeter's height
character_x_pos = (screen_width / 2) - (character_width /
                   2)  # the middle of screen width
character_y_pos = screen_height - character_height  # the bottom of screen heigth

# move position
to_x = 0
to_y = 0

# move speed
charactr_speed = 0.6


# enemy
enemy = pygame.image.load(r"C:\Users\user01\python\nadocoding\game\enemy.png")
enemy_size = enemy.get_rect().size  # get the image size
enemy_width = enemy_size[0]  # character's width
enemy_height = enemy_size[1]  # characeter's height
# the middle of screen width
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)  # the bottom of screen heigth


# even loop
running=True
while running:
    dt=clock.tick(60)  # 30 frame per 1 second

# conditions
# character can move in 100 pixel
# 10 fps : 10 * 10 = 100
# 20 fps : 20 * 5 = 100

    for event in pygame.event.get():  # which event raise?
        if event.type == pygame.QUIT:  # The event which close windows raise
            running=False

        if event.type == pygame.KEYDOWN:  # check if key is pressed.
            if event.key == pygame.K_LEFT:
                to_x -= charactr_speed
            elif event.key == pygame.K_RIGHT:
                to_x += charactr_speed
            elif event.key == pygame.K_UP:
                to_y -= charactr_speed
            elif event.key == pygame.K_DOWN:
                to_y += charactr_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x=0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y=0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # width boundary limit
    if character_x_pos < 0:
        character_x_pos=0
    elif character_x_pos > screen_width - character_width:
        character_x_pos=screen_width - character_width

    if character_y_pos < 0:
        character_y_pos=0
    elif character_y_pos > screen_height - character_height:
        character_y_pos=screen_height - character_height

    # collision for updating positions
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # check if the collision occurs
    if character_rect.colliderect(enemy_rect):
        print("the collision occurs")
        running = False
    
    # screen.fill((0,0,255))
    screen.blit(background, (0, 0))  # draw the background

    screen.blit(character, (character_x_pos, character_y_pos))

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update()  # redrawing

# pygame exit
pygame.quit()
