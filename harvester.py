import navigation
import field_monitor
import planter


def harvest_one(cord_x=None, cord_y=None):
	if cord_x == None or cord_y == None:
		pass
	else:
		navigation.go_to_wp(cord_x, cord_y)
	
	if get_entity_type() == Entities.Sunflower:
		while not can_harvest():
			pass
			
	if can_harvest():
		harvest()
		
	field_monitor.record_plot_status()
			
			
def harvest_all_sunflowers():
	for num_petals in range(15,6,-1):
		while len(planter.sunflower_list[num_petals]) > 0:
			quick_print("PETALS:", num_petals, "COUNT:",len(planter.sunflower_list[num_petals]))
			cord_x = planter.sunflower_list[num_petals][0][0]
			cord_y = planter.sunflower_list[num_petals][0][1]
			quick_print("CORD:",cord_x, cord_y)
			harvest_one(cord_x, cord_y)
			planter.sunflower_list[num_petals].pop(0)


def harvest_all():
	navigation.traverse(harvest_one)


if __name__ == "__main__":
	harvest_all()
	for plot_num in field_monitor.field_status:
		quick_print(plot_num, field_monitor.field_status[plot_num])
		quick_print("\n")