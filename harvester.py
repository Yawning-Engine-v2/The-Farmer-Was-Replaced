import navigation
import planter


def harvest_one(cord_x=None, cord_y=None):
	if cord_x == None and cord_y == None:
		pass
	else:
		navigation.go_to_wp(cord_x, cord_y)
	
	if (not can_harvest()) and (not Entities.Dead_Pumpkin):
		while not can_harvest():
			pass
	harvest()
			
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
	if get_entity_type() == Entities.Sunflower:
		harvest_all_sunflowers()
	else:
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if can_harvest():
					harvest()
				move(East)
			move(North)

if __name__ == "__main__":
	harvest_all()