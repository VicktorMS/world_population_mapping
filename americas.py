import pygal 


wm = pygal.maps.world.World()
wm.title = 'Populações da America do Norte'

wm.add('America do Norte',
        {
            'ca': 3123145123, 
            'mx': 1321565657, 
            'us': 4545567689
        }
    )

wm.render_to_file('examples/north_america_pop.svg')