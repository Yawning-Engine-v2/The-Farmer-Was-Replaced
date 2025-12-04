start_time = get_time()
import full_field

iterations = 1
yield = 5
crop_list = [Entities.Carrot,Entities.Carrot,Entities.Carrot,Entities.Carrot,Entities.Carrot,Entities.Carrot,Entities.Carrot,Entities.Carrot,Entities.Carrot,Entities.Carrot]
clear()

while iterations > 0:
    full_field.harvest_and_plant(crop_list)
    iterations -= 1

end_time = get_time()
quick_print("Time",end_time-start_time)
quick_print("Ticks",get_tick_count())