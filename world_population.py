
from data_filter import formatted_countries


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



world_pop_less_10m, world_pop_less_1b, world_pop_over_1b = get_pop_range(formatted_countries)

print(len(world_pop_less_10m), len(world_pop_less_1b), len(world_pop_over_1b))







