while ((get_x() != get_target_x()) or (get_y() != get_target_y())):

    steps_count = 0

    if can_move():
        while can_move() and not is_in_front_of_enemy() and not is_on_target():
            move()
            steps_count += 1
    else:
        orientation_visited = False
        if get_x() == get_target_x():
            turn_y = ""
            dy = 0
            if get_y() < get_target_y():
                if get_direction() != SOUTH:
                    turn_y = "turn_left"
                    for o in [WEST, NORTH, EAST]:
                        if o != get_direction() and not orientation_visited:
                            dy += 1
                        else:
                            orientation_visited = True
            elif get_y() > get_target_y():
                if get_direction() != NORTH:
                    turn_y = "turn_right"
                    for o in [WEST, SOUTH, EAST]:
                        if o != get_direction() and not orientation_visited:
                            dy += 1
                        else:
                            orientation_visited = True
            else:
                if not is_in_front_of_enemy() and can_move():
                    move()
                    steps_count += 1
            if turn_y == "turn_left":
                for y in range(dy):
                    turn_left()
            else:
                for y in range(dy):
                    turn_right()
        else:
            turn_x = ""
            dx = 0
            if get_x() < get_target_x():
                if get_direction() != EAST:
                    turn_x = "turn_left"
                    for o in [NORTH, WEST, SOUTH]:
                        if o != get_direction() and not orientation_visited:
                            dx += 1
                        else:
                            orientation_visited = True
            elif get_x() > get_target_x():
                if get_direction() != WEST:
                    turn_x = "turn_left"
                    for o in [NORTH, EAST, SOUTH]:
                        if o != get_direction() and not orientation_visited:
                            dx += 1
                        else:
                            orientation_visited = True
            else:
                if not is_in_front_of_enemy() and can_move():
                    move()
                    steps_count += 1
            if turn_x == "turn_left":
                for x in range(dx):
                    turn_left()
            else:
                for x in range(dx):
                    turn_right()

destroy_dark_force()