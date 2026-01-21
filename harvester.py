import navigation
import field_monitor
import planter


def harvest_one():
	if get_entity_type() == Entities.Sunflower:
		while not can_harvest():
			pass
			
	if can_harvest():
		harvest()
		
	field_monitor.record_plot_status()
	

def harvest_one_at(cord_x=None, cord_y=None):
	if cord_x == None or cord_y == None:
		pass
	else:
		navigation.go_to_wp(cord_x, cord_y)
	harvest_one()
			
			
def harvest_all_sunflowers():
	for num_petals in range(15,6,-1):
		petal_list = field_monitor.sunflower_petals_list[num_petals]
		while len(petal_list) > 0:
			cord_x = petal_list[0][0]
			cord_y = petal_list[0][1]
			harvest_one_at(cord_x, cord_y)
			petal_list.pop(0)


def harvest_all_pumpkins():
	field_monitor.record_field_status()
	while len(field_monitor.dead_pumpkins_list) > 0:
		dead_pumpkin_list = field_monitor.dead_pumpkins_list[:]
		for cord_x, cord_y in dead_pumpkin_list:
			navigation.go_to_wp(cord_x, cord_y)
			if can_harvest() == False:
				if get_entity_type() == Entities.Dead_Pumpkin: 
					planter.plant_one(Entities.Pumpkin)
			else:
				field_monitor.dead_pumpkins_list.remove([cord_x, cord_y])
	harvest()
				

def harvest_all(crop_type = None):
	if crop_type == None:
		navigation.traverse(harvest_one)
	elif crop_type == Entities.Sunflower:
		harvest_all_sunflowers()
	elif crop_type == Entities.Pumpkin:
		harvest_all_pumpkins()


if __name__ == "__main__":
	harvest_all()
	for plot_num in field_monitor.field_status:
		quick_print(plot_num, field_monitor.field_status[plot_num])
		quick_print("\n")