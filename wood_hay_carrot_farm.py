import utils
import sunflower_farm

def single_run():
	for i in range(utils.world_size):
		for j in range(utils.world_size):
			if get_entity_type() == Entities.Sunflower:
				sunflower_farm.check_sunflower()
			else:
				rotate_plant()
			move(North)
			incr_index()
		incr_index()
		move(East)

def hay():
	if get_ground_type() != Grounds.Grassland:
		till()
	if can_harvest():
		harvest()

def wood():
	if get_ground_type() != Grounds.Grassland:
		till()
	if get_entity_type() != Entities.Tree:
		plant(Entities.Tree)
	if can_harvest():
		harvest()
		plant(Entities.Tree)

def carrot():
	if get_ground_type() != Grounds.Soil:
		till()
	if get_entity_type() != Entities.Carrot:
		plant(Entities.Carrot)
	if can_harvest():
		harvest()
		plant(Entities.Carrot)

def rotate_plant():
	if plant_index == 0:
		hay()
	elif plant_index == 1:
		wood()
	else:
		carrot()

def incr_index():
	global plant_index
	plant_index = (plant_index + 1) % 3

def main():
	clear()
	change_hat(Hats.Tree_Hat)
	global plant_index
	sunflower_farm.plant_run()
	while True:
		plant_index = 0
		single_run()

if __name__ == "__main__":
	main()