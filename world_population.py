import json

from country_codes import get_country_code


population_filename = 'data/population_data.json'

with open(population_filename) as pop_fo:
    world_population = json.load(pop_fo)

world_pop_2010 = [
        {
            "Country Name": country['Country Name'],
            "Country Code": get_country_code(country['Country Name']),
            "Year": country['Year'],
            "Value": int(float(country['Value']))
        }
        for country in world_population 
        if country['Year'] == '2010' and get_country_code(country['Country Name'])
    ]

world_2010_code_pop = {country['Country Code']: country['Value'] for country in world_pop_2010}


print(world_pop_2010)









#print(next((country for country in world_population if country['Country Name'] == 'Brazil'), None))