from h_potter import *
import time, threading

move = app.player.move
turn_right = app.player.turn_right
turn_left = app.player.turn_left
can_move = app.player.canMove
get_x = app.player.getX
get_y = app.player.getY
get_target_x = app.map.getRelicPosX
get_target_y = app.map.getRelicPosY
is_on_target = app.player.isOnTarget
get_direction = app.player.getDir
is_in_front_of_enemy = app.player.is_ennemy_in_front
WEST = "WEST"
EAST = "EAST"
NORTH = "NORTH"
SOUTH = "SOUTH"
time.sleep(1)

print("Start algorithm")

def main():
	steps = 0
	print("SP1")
	# SP1 trouver une bordure
	while get_x() != 0 and get_x() != 9 and get_y() != 0 and get_y() != 9 and get_x() != get_target_x():
		while can_move() and not is_in_front_of_enemy() and get_x() != get_target_x():
			steps += 1
			move()

		while (not can_move() or is_in_front_of_enemy()) and (get_x() != 0 and get_x() != 9 and get_y() != 0 and get_y() != 9 and get_x() != get_target_x()):
			turn_left()
			steps += 1
			if can_move() and not is_in_front_of_enemy():
				move()
				turn_right()
				steps += 2	

	print("SP2")
	# SP2 suivre la bordure jusqu'au x
	if get_x() != get_target_x():
		# SP3 s'orienter vers la bordure
		if get_x() == 0:
			while get_direction() != WEST:
				steps += 1
				turn_left()
		elif get_x() == 9:
			while get_direction() != EAST:
				steps += 1
				turn_left()
		elif get_y() == 0:
			while get_direction() != NORTH:
				steps += 1
				turn_left()
		else:
			while get_direction() != SOUTH:
				steps += 1
				turn_left()
	else:
		if get_y() > get_target_y():
			while get_direction() != NORTH:
				steps += 1
				turn_left()
		elif get_y() < get_target_y():
			while get_direction() != SOUTH:
				steps += 1
				turn_right()

	print("SP3")
	while get_x() != get_target_x():
		while can_move() and not is_in_front_of_enemy() and get_x() != get_target_x():
			move()
			steps += 1
		while (not can_move() or is_in_front_of_enemy()) and get_x() != get_target_x():
			if (get_y() == 0 and get_direction() == NORTH) or (get_y() == 9 and get_direction() == SOUTH) or (get_x() == 0 and get_direction() == WEST) or (get_x() == 9 and get_direction() == EAST):
				turn_left()
				steps += 1
				while can_move() and not is_in_front_of_enemy() and get_x() != get_target_x():
					move()
					steps += 1
			else:
				turn_left()
				steps += 1
				if can_move() and not is_in_front_of_enemy() and get_x() != get_target_x():
					move()
					steps += 1
					turn_right()
					steps += 1
					if can_move() and not is_in_front_of_enemy() and get_x() != get_target_x():
						move()
						steps += 1
						turn_right()
						steps += 1

	if get_y() > get_target_y():
		while get_direction() != NORTH:
			turn_left()
			steps += 1
	elif get_y() < get_target_y():
		while get_direction() != SOUTH:
			turn_right()
			steps += 1

	print("SP4")
	while not is_on_target():
		if get_x() == get_target_x():
			if get_y() > get_target_y():
				while get_direction() != NORTH:
					turn_left()
					steps += 1
			elif get_y() < get_target_y():
				while get_direction() != SOUTH:
					turn_right()
					steps += 1
		while can_move() and not is_in_front_of_enemy() and not is_on_target():
			move()
			steps += 1
		if is_on_target():
			break

		
		while (not can_move() or is_in_front_of_enemy()) and get_x() == get_target_x():
			turn_left()
			if can_move() and not is_in_front_of_enemy():
				move()
				turn_right()
				steps += 2
				if can_move() and not is_in_front_of_enemy():
					move()
					turn_right()
					steps += 2

		while (not can_move() or is_in_front_of_enemy()) and get_x() != get_target_x():
			turn_left()
			steps += 1
			if can_move() and not is_in_front_of_enemy():
				move()
				turn_right()
				steps += 2
				if can_move() and not is_in_front_of_enemy():
					move()
					turn_right()
					steps += 2

	print(steps)

threading.Thread(target=main, daemon=True).start()