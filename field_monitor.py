import navigation


# Global dict to hold information about every plot in the field
field_status = {}

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
	
	
# Function to record details about the plot directly underneath the drone
def record_plot_status():
	field_status[(get_pos_x(),get_pos_y())] = {"entity": get_entity_type(), 
							"ground_type": get_ground_type(), 
							"companion": get_companion(), 
							"measure": measure(),
							"water_level": get_water(),
							"is_harvestable": can_harvest(),
							"is_companion": False
							}
							
def get_plot_status(cord_x=None, Cord_y=None):
	if cord_x == None or cord_y == None:
		return field_status[(get_pos_x(),get_pos_y())]
	else:
		return field_status[(cord_x,cord_y)]
							
# Function to record details about every plot in the field							
def record_field_status():
	navigation.traverse(record_plot_status)


if __name__ == "__main__":
	record_field_status()

	for plot_num in field_status:
		quick_print(plot_num, field_status[plot_num])
		quick_print("\n")