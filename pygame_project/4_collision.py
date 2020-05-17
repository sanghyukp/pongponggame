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

# get current directory path including the current file
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

# Background
background = pygame.image.load(os.path.join(image_path, "background.png"))

# Stage
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]  # limit  objects of game to inner frame

# Character
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - (character_height + stage_height)


# Character move direction
character_to_x = 0

# Character speed
character_speed = 5

# weapon
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# at a time, be able to shoot multiple times
weapons = []

# weapon speed
weapon_speed = 10

# creating weapon (4)
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))
]

# initial speed based on ball size
ball_speed_y = [-18, -15, -12, -9]  # index 0,1,2,3 에 해당하는 값

# ball info

balls = []

# init ball append
balls.append({
    "pos_x": 50,  # ball's x
    "pos_y": 50,  # ball's y
    "img_idx": 0,  # ball's image index
    "to_x": 3,  # move based x axis
    "to_y": -6,  # move based y asix
    "init_spd_y": ball_speed_y[0]  # y speed
})

# removing weapon, ball info
weapon_to_remove = -1
ball_to_remove = -1

running = True
while running:
    dt = clock.tick(60)  # 30 frame per 1 second
    # 2. handing with evnets (keyboard, mouse)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # move character on the left
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + \
                    (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
    # 3. cope with character position
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # weapon adjust positions
    # 100, 200 -> 180, 160, 140, ...
    # 500, 200 -> 180, 160, 140, ...
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]  # get weapons up

    # remove the weapon when it reach ceil
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

    # set position ball
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # reach the wall, change ball position
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1

        # vertical position
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else: # anything else, reduce the speed of y
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

    # 4. process collision

    # get rect info of character
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        # update ball_rect info       
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        # handle with collistion between character, ball
        if character_rect.colliderect(ball_rect):
            running = False
            break
        
        # hanle with collision between ball and weapon 
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_x_pos = weapon_val[0]
            weapon_y_pos = weapon_val[1]

            # updating weapon rect
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_x_pos
            weapon_rect.top = weapon_y_pos

            # check collision
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx # set idx to remove weapon
                ball_to_remove = ball_idx # set idx to remove ball
                break
    
    # to remove ball and weapon
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    # 5. draw screen
    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()  # redrawing

# posed the game
pygame.time.delay(2000)

# pygame exit
pygame.quit()
