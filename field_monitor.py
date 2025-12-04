import navigation

# can be optimised to take set of coordinates to monitor, if none chech entire field
def get_dead_pumpkins():
	cords = []
	world_size = get_world_size()
	for y in range(world_size):
		for x in range(world_size):
			if get_entity_type() == Entities.Dead_Pumpkin:
				cords.append((get_pos_x(), get_pos_y()))
				#print((get_pos_x(), get_pos_y()))
			move(East)
		move(North)
	
	return cords

if __name__ == "__main__":
	navigation.go_to_wp(0,0)
	get_dead_pumpkins()