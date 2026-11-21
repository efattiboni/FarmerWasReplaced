def move_to_origin():
	world_size = get_world_size()

	y = get_pos_x()
	if y >= world_size / 2:
		for i in range(world_size - y):
			move(North)
	else:
		for i in range(y):
			move(South)

	x = get_pos_x()
	if x >= world_size / 2:
		for i in range(world_size - x):
			move(East)
	else:
		for i in range(x):
			move(West)