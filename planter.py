import navigation	
import field_monitor
	
sunflower_list = {}

def plant_one(crop_type, cord_x=None, cord_y=None):
	if crop_type == Entities.Grass:
		if get_ground_type() != Grounds.Grassland:
			till()
	# add support for trees as well here
	elif crop_type == Entities.Bush or crop_type == Entities.Tree:
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
		sunflower_pos = (get_pos_x(),get_pos_y())
		if measure() in sunflower_list: 
			sunflower_list[measure()].append(sunflower_pos)
		else:
			sunflower_list[measure()] = [sunflower_pos]
		#quick_print(sunflower_pos)

def plant_many(crop_type, cords):
	for cord in cords:
		navigation.go_to_wp(cord[0], cord[1])
		plant_one(crop_type)	
		
			
def plant_all(crop_type):
	if crop_type == Entities.Grass:
		clear()
		while not can_harvest():
			continue
	else:		
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				plant_one(crop_type)
				
				move(East)
			move(North)
		if crop_type == Entities.Pumpkin:
			dead_pumpkin_cords = field_monitor.get_dead_pumpkins()
			plant_many(Entities.Pumpkin ,dead_pumpkin_cords)
			navigation.go_to_wp(0,0)

if __name__ == "__main__":
	plant_all(Entities.Carrot)