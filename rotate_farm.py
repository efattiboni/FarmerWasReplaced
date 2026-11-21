def traversal(func):
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			func()
			move(North)
		incr_counter()
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
	if counter == 0:
		hay()
	elif counter == 1:
		wood()
	else:
		carrot()
	incr_counter()

def incr_counter():
	global counter
	counter = (counter + 1) % 3

def main():
	clear()
	global counter
	counter = 0
	change_hat(Hats.Wizard_Hat)
	while True:
		traversal(rotate_plant)

if __name__ == "__main__":
	main()