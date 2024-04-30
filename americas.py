import pygal 


wm = pygal.maps.world.World()
wm.title = 'América do Sul, Norte e Central'

wm.add('America do Sul', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
       'gy', 'pe', 'py', 'sr', 'uy', 've'])
wm.add('America Central', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('America do Norte', ['ca', 'mx', 'us'])

wm.render_to_file('examples/simple_americas.svg')