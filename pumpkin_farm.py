import utils

def traverse(func):
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			func()
			move(North)
		move(East)

def plant_pumpkin():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Pumpkin)

def verify_quick():
	if get_entity_type() == Entities.Dead_Pumpkin:
		plant_pumpkin()
		global ready
		ready = False

def verify_waiting():
	while not can_harvest():
		if get_entity_type() == Entities.Dead_Pumpkin:
			plant_pumpkin()

def single_run():
	utils.move_to_origin()
	
	traverse(plant_pumpkin)
	global ready
	for i in range(2): # num of quick_verify runs
		ready = True
		traverse(verify_quick)
		if ready:
			break
	if not ready:
		traverse(verify_waiting)
	harvest()

def main():
	clear()
	change_hat(Hats.Pumpkin_Hat)
	while True:
		single_run()
		
if __name__ == "__main__":
	main()
