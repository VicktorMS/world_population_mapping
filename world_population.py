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


def get_pop_range(pop_dict):
    cc_pops_1, cc_pops_2, cc_pops_3  = {}, {}, {}

    for country in pop_dict:
        if country['Value'] < 10_000_000:
            cc_pops_1[country['Country Code']] = country['Value']
        elif country['Value'] < 1_000_000_000:
            cc_pops_2[country['Country Code']] = country['Value']
        else: 
            cc_pops_3[country['Country Code']] = country['Value']
    
    return cc_pops_1, cc_pops_2, cc_pops_3 



world_pop_less_10m, world_pop_less_1b, world_pop_over_1b = get_pop_range(world_pop_2010)










#print(next((country for country in world_population if country['Country Name'] == 'Brazil'), None))