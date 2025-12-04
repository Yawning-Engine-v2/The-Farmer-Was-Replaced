clear()
for i in range(get_world_size()):
		for j in range(get_world_size()):
			if 0 == get_pos_x():
				pass
			if 2 == get_pos_x() or 3 == get_pos_x() or (4 == get_pos_x() and get_pos_y() > 2):
				plant(Entities.Bush)
			if (4 == get_pos_x() or 5 == get_pos_x()) and (get_pos_y() < 3):
				till()
				plant(Entities.Carrot)
			move(East)
		move(North)