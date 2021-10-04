import pygame, random
import numpy as np
import pygame_widgets
from pygame_widgets.button import Button

width, height = 16, 16
square_size = 40
obstacles = 20
background_colour = (50, 50, 50)

map = np.zeros((height, height))

def get_valid_point(map):
    x = random.randint(0, width-1)
    y = random.randint(0, height-1)

    #while map[x][y] == 1 or map[x-1][y] == 1 or map[x+1][y] == 1 or map[x][y-1] == 1 or map[x][y+1] == 1 or map[x-1][y-1] == 1 or map[x-1][y+1] == 1 or map[x+1][y-1] == 1 or map[x+1][y-1] == 1:
    while True:
        if map[y][x] == 0 and map[min(y+1, height-1)][x] == 0 and map[max(y-1, 0)][x] == 0 and map[min(y+1, height-1)][min(width-1, x+1)] == 0 and map[min(y+1, height-1)][max(0, x-1)] == 0:
            if map[max(y-1, 0)][min(x+1, width-1)] == 0 and map[max(y-1, 0)][max(x-1, 0)] == 0 and map[y][max(x-1, 0)] == 0 and map[y][min(x+1, width-1)] == 0:
                return x, y

        x = random.randint(0, width-1)
        y = random.randint(0, height-1)

for _ in range(obstacles):
    x, y = get_valid_point(map)
    map[y][x] = 1

xh, yh = get_valid_point(map)
xt, yt = get_valid_point(map)

while xh >= xt:
    xh, yh = get_valid_point(map)
    xt, yt = get_valid_point(map)

map[yh][xh] = 2
map[yt][xt] = 3

directions = ["EAST", "NORTH", "SOUTH", "WEST"]
direction = random.choice(directions)

paused = False

def draw_map():
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == 1:
                pygame.draw.rect(screen, (255, 255, 255), (x*square_size, y*square_size, square_size, square_size))
            elif map[y][x] == 0:
                pygame.draw.rect(screen, (50, 50, 50), (x*square_size, y*square_size, square_size, square_size))
            elif map[y][x] == 2:
                pygame.draw.rect(screen, (0, 0, 255), (x*square_size, y*square_size, square_size, square_size))
            elif map[y][x] == 3:
                pygame.draw.rect(screen, (0, 255, 0), (x*square_size, y*square_size, square_size, square_size))

def move():
    if can_move():
        x = get_x()
        y = get_y()
        if direction=="EAST":
            map[y][x] = 0
            map[y][x+1] = 2
        if direction=="NORTH":
            map[y][x] = 0
            map[y+1][x] = 2
        if direction=="WEST":
            map[y][x] = 0
            map[y][x-1] = 2
        if direction=="SOUTH":
            map[y][x] = 0
            map[y-1][x] = 2
    
    if is_on_target():
        print("Well done!")
        paused = True

def turn_right():
    global direction
    if direction == "EAST":
        direction = "NORTH"
    elif direction == "NORTH":
        direction = "WEST"
    elif direction == "WEST":
        direction = "SOUTH"
    else:
        direction = "EAST"

def turn_left():
    global direction
    if direction == "EAST":
        direction = "SOUTH"
    elif direction == "SOUTH":
        direction = "WEST"
    elif direction == "WEST":
        direction = "NORTH"
    else:
        direction = "EAST"

def can_move():
    y, x = np.where(map==2)
    y, x = y[0], x[0]
    if direction == "EAST":
        if x == width-1:
            return False
        if map[y][x+1] != 1:
            return True
    if direction == "NORTH":
        if y == 0:
            return False
        if map[y+1][x] != 1:
            return True
    if direction == "WEST":
        if x == 0:
            return False
        if map[y][x-1] != 1:
            return True
    if direction == "SOUTH":
        if y == height-1:
            return False
        if map[y-1][x] != 1:
            return True
    return False

def is_in_front_of_enemy():
    y, x = np.where(map==2)
    y, x = y[0], x[0]
    if direction == "EAST":
        if x == width-1:
            return False
        if map[y][x+1] == 4:
            return True
    if direction == "NORTH":
        if y == 0:
            return False
        if map[y+1][x] == 4:
            return True
    if direction == "WEST":
        if x == 0:
            return False
        if map[y][x-1] == 4:
            return True
    if direction == "SOUTH":
        if y == height-1:
            return False
        if map[y-1][x] == 4:
            return True
    return False

def is_on_target():
    return not any(3 in a for a in map)

def destroy_dark_force():
    if is_on_target():
        print("Force obscure detruite!")
    else:
        print("Vous n'êtes pas sur la force obscure")

def get_direction():
    return direction

def get_x():
    y, x = np.where(map==2)
    y, x = y[0], x[0]
    return x

def get_y():
    y, x = np.where(map==2)
    y, x = y[0], x[0]
    return y

def get_target_x():
    y, x = np.where(map==3)
    y, x = y[0], x[0]
    return x

def get_target_y():
    y, x = np.where(map==3)
    y, x = y[0], x[0]
    return y

pygame.init()
screen = pygame.display.set_mode((width*square_size, height*square_size+50))
screen.fill(background_colour)

movebtn = Button(
    screen, 0, height*square_size, 100, 50, text='Move',
    fontSize=30, margin=20,
    inactiveColour=(150, 150, 150),
    pressedColour=(0, 0, 0), radius=3,
    onClick=move
)

turnlbtn = Button(
    screen, 105, height*square_size, 100, 50, text='Turn Left',
    fontSize=30, margin=20,
    inactiveColour=(150, 150, 150),
    pressedColour=(0, 0, 0), radius=3,
    onClick=turn_left
)

turnrbtn = Button(
    screen, 210, height*square_size, 100, 50, text='Turn Right',
    fontSize=30, margin=20,
    inactiveColour=(150, 150, 150),
    pressedColour=(0, 0, 0), radius=3,
    onClick=turn_right
)

pygame.display.set_caption('Hawwy Potteur')
draw_map()
pygame.display.flip()

running = True

while running and not paused:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    pygame_widgets.update(events)
    draw_map()
    pygame.display.update()