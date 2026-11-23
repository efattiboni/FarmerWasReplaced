import utils
import sunflower_farm

def plant_pumpkin():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Pumpkin)

def plant_run():
	for i in range(utils.world_size):
		for j in range(utils.world_size):
			if get_entity_type() == Entities.Sunflower:
				sunflower_farm.check_sunflower()
			else:
				plant_pumpkin()
			move(North)
		move(East)

def verify_quick():
	if get_entity_type() == Entities.Dead_Pumpkin:
		plant_pumpkin()
		global ready
		ready = False
		return True # was_dead

def verify_waiting():
	while not can_harvest():
		if get_entity_type() == Entities.Dead_Pumpkin:
			plant_pumpkin()
		else:
			if get_water() < 0.75:
				use_item(Items.Water)
			# use_item(Items.Fertilizer)
			pass

def verify_run(quick=False):
	for i in range(utils.world_size):
		if i and col_ready[i]: # first col is never skipped 
			move(East)
			continue
		col_ready[i] = True
		for j in range(utils.world_size):
			if get_entity_type() == Entities.Sunflower:
				sunflower_farm.check_sunflower()
			else:
				if quick:
					was_dead = verify_quick()
					if was_dead:
						col_ready[i] = False
				else:
					verify_waiting()
			move(North)
		move(East)

def single_run():
	utils.move_to_origin()

	plant_run()

	global ready
	global col_ready
	col_ready = []
	for i in range(utils.world_size):
		col_ready.append(False)
	for i in range(3): # num of quick verify_run
		ready = True
		verify_run(True)
		if ready:
			break
	if not ready:
		verify_run()
	move(East)
	harvest()

def main():
	clear()
	change_hat(Hats.Pumpkin_Hat)
	sunflower_farm.plant_run()
	while True:
		single_run()
		
if __name__ == "__main__":
	main()
	