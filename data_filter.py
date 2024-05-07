from pygal.maps.world import COUNTRIES
import json, re
  
    
def get_world_pop_by_year(world_pop, year):
    return [country for country in world_pop if country['Year'] == year]


def format_country_data(country, country_code):
    return {
            "Country Name": country['Country Name'],
            "Country Code": country_code,
            "Year": country['Year'],
            "Value": int(float(country['Value']))
         }
    
def find_word_in_string(word_list, string):
    pattern = r"\b(" + "|".join(word_list) + r")\b"
    if re.search(pattern, string, flags=re.IGNORECASE):
        return True
    else:
        return False
    
def filter_valid_country_name(country_name):
    invalid_keywords = ['income', 'developing', ':', 'indebted', 'developed', "st."]        
    if not find_word_in_string(invalid_keywords, country_name):
        if ',' in country_name:
            return country_name.split(',')[0]
        else:
            return country_name
    return None

def filter_invalid_countries(world_pop):
    return [country for country in world_pop if filter_valid_country_name(country['Country Name'])]
    
   
def get_formatted_world_pop_country_code(world_pop):
    formatted_countries = []
    
    # Filtrando países inválidos
    valid_world_pop = filter_invalid_countries(world_pop)
    
    for country in valid_world_pop:
        found = False
        for code, name in COUNTRIES.items():
            if filter_valid_country_name(name) == filter_valid_country_name(country['Country Name']):
                formatted_countries.append(format_country_data(country, code))
                found = True
                break

    return formatted_countries


population_filename = 'data/population_data.json'

try:
    with open(population_filename) as pop_fo:
        world_population = json.load(pop_fo)
except FileNotFoundError:
    print("Arquivo não encontrado:", population_filename)
except json.JSONDecodeError:
    print("Erro ao decodificar o arquivo JSON:", population_filename)
else:
    world_population_in_2010 = get_world_pop_by_year(world_population, '2010')
    formatted_countries = get_formatted_world_pop_country_code(world_population_in_2010)
