import field_monitor
import planter
import navigation
import harvester

navigation.go_to_wp(0,0)
#print(measure())
planter.plant_all(Entities.Sunflower)
quick_print(planter.sunflower_list)
harvester.harvest_all()
quick_print(planter.sunflower_list)