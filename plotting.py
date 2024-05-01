import pygal 
from world_population import world_2010_code_pop


wm = pygal.maps.world.World()
wm.title = 'População Mundial em 2010, por país'

wm.add('2010', world_2010_code_pop)

wm.render_to_file('examples/world_pop_v1.svg')