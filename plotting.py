import pygal 
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS
from world_population import world_pop_less_10m, world_pop_less_1b, world_pop_over_1b


# LightColorizedStyle  lighten the style of charts

wm_style = RS('#4CF5E3', base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'População Mundial em 2010, por país'

wm.add('População inferior a 10 milhões de habitantes', world_pop_less_10m)
wm.add('População inferior a 1 bilhão de habitantes', world_pop_less_1b)
wm.add('População superior a 1 bilhão de habitantes', world_pop_over_1b)

wm.render_to_file('examples/world_pop_styled_light.svg')