import utils

petals_list = []

def traverse_outer(func):
	world_size = get_world_size()
	for i in range(world_size - 1):
		func()
		move(North)
	for i in range(world_size):
		func()
		move(East)

def plant_sunflower():
	global petals_list
	if get_ground_type() != Grounds.Soil:
		till()
	if get_entity_type() != Entities.Sunflower:
		plant(Entities.Sunflower)
		petals_list.append(measure())

def plant_run():
	utils.move_to_origin()
	traverse_outer(plant_sunflower)
	utils.move_to_origin()

def check_sunflower():
	reps = 0
	petals = measure()
	while petals == 15 or max(petals_list) <= petals and reps < 5:
		while not can_harvest():
			use_item(Items.Fertilizer)
		harvest()
		plant(Entities.Sunflower)
		petals_list.remove(petals)
		petals = measure()
		petals_list.append(petals)
		reps += 1

def check_sunflower_waiting():
	petals = measure()
	while petals == 15 or max(petals_list) <= petals:
		while not can_harvest():
			use_item(Items.Fertilizer)
		harvest()
		plant(Entities.Sunflower)
		petals_list.remove(petals)
		petals = measure()
		petals_list.append(petals)

def check_sunflower_quick():
	if can_harvest():
		petals = measure()
		if petals == 15 or max(petals_list) <= petals:
			harvest()
			plant(Entities.Sunflower)
			petals_list.remove(petals)
			petals = measure()
			petals_list.append(petals)
	
def outer_run():
	utils.move_to_origin()
	traverse_outer(check_sunflower)

def main():
	clear()
	change_hat(Hats.Sunflower_Hat)
	plant_run()
	while True:
		outer_run()

if __name__ == "__main__":
	main()
