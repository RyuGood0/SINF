from APP0 import *

if get_x() > get_target_x():
    while get_direction != "WEST":
        turn_right()
elif get_x() < get_target_x():
    while get_direction != "EAST":
        turn_right()
elif get_y() > get_target_y():
    while get_direction() != "NORTH":
        turn_right()
else:
    while get_direction() != "SOUTH":
        turn_right()
while not is_on_target():
    if get_y() == get_target_y():
        if get_x()>get_target_x():
            while get_direction() != "WEST":
                turn_right()
        else:
            while get_direction() != "EAST":
                turn_right()

    if get_x() == get_target_x():
        if get_y()>get_target_y():
            while get_direction() != "NORTH":
                turn_right()
        else:
            while get_direction() != "SOUTH":
                turn_right()
    if can_move() and not is_in_front_of_enemy():
        move()
    else:
        if get_direction == "EAST" or get_direction() == "WEST":
            while get_direction() != "SOUTH":
                turn_left()
        elif get_direction == "NORTH" or get_direction() == "SOUTH":
            while get_direction() != "EAST":
                turn_left()
        while can_move():
            move()
            turn_left()
            if can_move() and not is_in_front_of_enemy():
                move()
                if get_x() == get_target_x() or get_y() == get_target_y():
                    break
                move()
                turn_left()
                break
