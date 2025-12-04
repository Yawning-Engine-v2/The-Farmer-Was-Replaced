import navigation	
import field_monitor
	

def plant_one(crop_type):
	if crop_type == Entities.Grass:
		if get_ground_type() != Grounds.Grassland:
			till()
			
	elif crop_type == Entities.Tree:
		if get_pos_y()%2 == 0:
			if get_pos_x()%2 == 0:
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)
		else:
			if get_pos_x()%2 == 0:
				plant(Entities.Bush)
			else:
				plant(Entities.Tree)
	
	elif crop_type == Entities.Bush:
		plant(Entities.Bush)
		
	elif crop_type == Entities.Carrot:
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Carrot)
	
	elif crop_type == Entities.Pumpkin:
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Pumpkin)
	
	elif crop_type == Entities.Sunflower:
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Sunflower)
	
	field_monitor.record_plot_status()


def plant_one_wrapper(crop_type):
	def action():
		plant_one(crop_type)
	return action
	

def plant_one_at(crop_type, cord_x=None, cord_y=None):
	if cord_x == None or cord_y == None:
		pass
	else:
		navigation.go_to_wp(cord_x, cord_y)
	plant_one(crop_type)


def plant_many(crop_type, cords):
	for cord in cords:
		plant_one_at(cords[0], cords[1])
	
	
def plant_all(crop_type):
	wrapped_plant_one = plant_one_wrapper(crop_type) 
	navigation.traverse(wrapped_plant_one)
	
	if crop_type == Entities.Pumpkin:
		dead_pumpkin_cords = field_monitor.get_dead_pumpkins()
		plant_many(Entities.Pumpkin ,dead_pumpkin_cords)
		navigation.go_to_wp(0,0)


if __name__ == "__main__":
	plant_all(Entities.Carrot)