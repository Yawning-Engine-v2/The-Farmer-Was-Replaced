import planter
import harvester


def harvest_and_plant(crop_list):
	world_size = get_world_size()
	
	first_crop = crop_list.pop(0)
	planter.plant_all(first_crop)
	
	for crop_type in crop_list:
		for y in range(world_size):
			for x in range(world_size):
				harvester.harvest_one()
				planter.plant_one(crop_type)
				
				move(East)
			move(North)
			
	harvester.harvest_all()
				

def grow_crop(crop_type, num_harvests):
	# For Grass, since it regrows automatically
	if crop_type == Entities.Grass:
		planter.plant_all(crop_type)
		for n in range(num_harvests):
			harvester.harvest_all()
	# For all other plants
	else:
		for n in range(num_harvests):
			planter.plant_all(crop_type)
			harvester.harvest_all()

# Not optimised for more than one harvest of a particular crop
if __name__ == "__main__":
	start_time = get_time()
	clear()
	crop_list = [Entities.Bush, Entities.Bush]
	harvest_and_plant(crop_list)
	end_time = get_time()
	print("Time",end_time-start_time)
	