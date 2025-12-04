def move_n_blocks(direction, n):
	for i in range(n):
		move(direction)
	
def get_shortest_move(cord, axis):
	world_size = get_world_size()
	world_size_half = world_size//2
		
	if axis == "x":
		direction_pos = East
		direction_neg = West
		
		pos_x = get_pos_x()
		diff = cord - pos_x
		
	if axis == "y":
		direction_pos = North
		direction_neg = South
		
		pos_y = get_pos_y()
		diff = cord - pos_y
	
	if diff > 0:
		if diff < world_size_half:
			return direction_pos, diff
		else:
			return direction_neg, world_size - diff
	
	if diff < 0:
		diff = -diff
		if diff < world_size_half:
			return direction_neg, diff
		else:
			return direction_pos, world_size - diff
	
	return direction_pos, 0


def go_to_wp(cord_x=None, cord_y=None):
	
	if cord_x == None:
		cord_x = get_pos_x()
	if cord_y == None:
		cord_y = get_pos_y()
		
	dir_x, blocks_x = get_shortest_move(cord_x, "x")
	move_n_blocks(dir_x, blocks_x)
	
	dir_y, blocks_y = get_shortest_move(cord_y, "y")
	move_n_blocks(dir_y, blocks_y)
	

if __name__ == "__main__":
	go_to_wp(0,0)	