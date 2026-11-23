import utils
import sunflower_farm

def traverse(func):
	for i in range(utils.world_size):
		for j in range(utils.world_size):
			if get_entity_type() == Entities.Sunflower:
				sunflower_farm.check_sunflower()
			else:
				func()
			move(North)
		move(East)

def measure_cactus(direction):
	if get_entity_type(direction) != Entities.Cactus:
		return False
	return measure(direction)


def plant_cactus():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Cactus)
	sorted = False
	while not sorted:
		sorted = True
		size_curr = measure()
		size_south = measure_cactus(South)
		if size_south != False and size_curr < size_south:
			sorted = True
			swap(South)
			size_curr = size_south
		size_west = measure_cactus(West)
		if size_west != False and size_curr < size_west:
			sorted = True
			swap(West)
			size_curr = size_west

def check_cactus():
	global ready
	sorted = False
	while not sorted:
		sorted = True
	size_curr = measure()
	size_north = measure_cactus(North)
	if size_north != False and size_curr > size_north:
		ready = False
		sorted = False
		swap(North)
		size_curr = size_north
	size_east = measure_cactus(East)
	if size_east != False and size_curr > size_east:
		ready = False
		sorted = False
		swap(East)
		size_curr = size_east
	size_south = measure_cactus(South)
	if size_south != False and size_curr < size_south:
		ready = False
		sorted = False
		swap(South)
		size_curr = size_south
	size_west = measure_cactus(West)
	if size_west != False and size_curr < size_west:
		ready = False
		sorted = False
		swap(West)
		size_curr = size_west

def check_cactus_col():
	global col_sorted
	sorted = False
	while not sorted:
		sorted = True
	size_curr = measure()
	size_north = measure_cactus(North)
	if size_north != False and size_curr > size_north:
		col_sorted = False
		sorted = False
		swap(North)
		size_curr = size_north
	size_south = measure_cactus(South)
	if size_south != False and size_curr < size_south:
		col_sorted = False
		sorted = False
		swap(South)
		size_curr = size_south

def check_cactus_row():
	global row_sorted
	sorted = False
	while not sorted:
		sorted = True
	size_curr = measure()
	size_east = measure_cactus(East)
	if size_east != False and size_curr > size_east:
		row_sorted = False
		sorted = False
		swap(East)
		size_curr = size_east
	size_west = measure_cactus(West)
	if size_west != False and size_curr < size_west:
		row_sorted = False
		sorted = False
		swap(West)
		size_curr = size_west

def sort_columns():
	global col_sorted
	for i in range(utils.world_size):
		col_sorted = False
		while not col_sorted:
			col_sorted = True
			for j in range(utils.world_size):
				if get_entity_type() == Entities.Sunflower:
					sunflower_farm.check_sunflower()
				else:
					check_cactus_col()
				move(North)
		move(East)

def sort_rows():
	global row_sorted
	for j in range(utils.world_size):
		row_sorted = False
		while not row_sorted:
			row_sorted = True
			for i in range(utils.world_size):
				if get_entity_type() == Entities.Sunflower:
					sunflower_farm.check_sunflower()
				else:
					check_cactus_row()
				move(East)
		move(North)

def single_run():
	utils.move_to_origin()
	traverse(plant_cactus)
	global ready
	ready = False
	for i in range(2): # num of standard passes
		ready = True
		traverse(check_cactus)
		if ready:
			break
	if not ready:
		ready = True
		sort_rows()
		sort_columns()
	move(East)
	harvest()




def main():
	clear()
	change_hat(Hats.Cactus_Hat)
	sunflower_farm.plant_run()
	while True:
		single_run()
		
if __name__ == "__main__":
	main()
