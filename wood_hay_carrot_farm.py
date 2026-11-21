def traverse(func):
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			func()
			move(North)
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
	incr_index()

def incr_index():
	global plant_index
	plant_index = (plant_index + 1) % 3

def main():
	clear()
	change_hat(Hats.Tree_Hat)
	global plant_index
	while True:
		plant_index = 0
		traverse(rotate_plant)

if __name__ == "__main__":
	main()