start_time = get_time()
import full_field
import planter
import harvester
import navigation

iterations = 10
yield = 2
crop_list = [Entities.Grass,Entities.Grass,Entities.Tree,Entities.Tree,Entities.Carrot,Entities.Carrot]
clear()

while iterations >0 :
	full_field.harvest_and_plant(crop_list)
	full_field.grow_crop(Entities.Pumpkin, 2)
	planter.plant_all(Entities.Sunflower)
	harvester.harvest_all_sunflowers()
	navigation.go_to_wp(0,0)
	iterations -= 1
	
end_time = get_time()
quick_print("Time",end_time-start_time)
quick_print("Ticks",get_tick_count())