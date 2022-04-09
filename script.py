# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def conversion(damages):

  conversion = {"M": 1000000,
              "B": 1000000000}
  updated_damages = []

  for i in range(0, len(damages)):
    if "M" in damages[i]:
      converted = float(damages[i].strip("M")) * conversion["M"]
      updated_damages.append(converted)
    elif "B" in damages[i]:
      converted = float(damages[i].strip("B")) * conversion["B"]
      updated_damages.append(converted)
    else:
      updated_damages.append(damages[i])

  return updated_damages

updated_damages = conversion(damages)

# write your construct hurricane dictionary function here:
def create_dict(name, month, year, max_sustained_wind, areas_affected, damage, death):
  hurricane = {}
  for i in range(len(name)):
    hurricane[name[i]] = {"Month": month[i], "Year": year[i], "Max Sustained Wind": max_sustained_wind[i], "Areas Affected": areas_affected[i], "Damage": damage[i], "Death": death[i]}
  return hurricane

hurricane_dict = (create_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths))

# write your construct hurricane by year dictionary function here:
def hurricane_year(hurricanes):
  new_dict = {}
  for data in hurricanes:
    year_key = hurricanes[data]["Year"]
    year_value = hurricanes[data]
    year_value["Name"] = data
    if year_key not in new_dict:
      new_dict[year_key] = [year_value]
    else:
      new_dict[year_key].append(year_value)
  return new_dict

hurricanes_by_year = (hurricane_year(hurricane_dict))

# write your count affected areas function here:
ef count_affected_areas(dictionary):
  areas = {}
  for data in dictionary:
    areas_affected = dictionary[data]["Areas Affected"]
    for area in areas_affected:
      if area not in areas:
        areas[area] = 1
      else:
        areas[area] += 1
  return (areas)

affected_areas_count = (count_affected_areas(hurricane_dict))

# write your find most affected area function here:
def most_affected_area(dictionary):
  max_value = max(dictionary.values())
  max_key = [key for key,value in dictionary.items() if value == max_value]
  return max_key, max_value

most_affected = most_affected_area(affected_areas_count))

# write your greatest number of deaths function here:
def most_deaths(dictionary):
  highest_death_count = 0
  deadliest_hurricane = "hurricane name"
  for data in dictionary:
    if dictionary[data]["Death"] > highest_death_count:
      highest_death_count = dictionary[data]["Death"]
      deadliest_hurricane = data
  return deadliest_hurricane, highest_death_count

deadliest_hurricane = most_deaths(hurricane_dict)

# write your catgeorize by mortality function here:
def mortality_scale(dict):

  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  new_dict = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  for hurricane in dict:
    num_deaths = dict[hurricane]["Death"]
    if num_deaths == mortality_scale[0]:
      new_dict[0].append(hurricane)
    elif num_deaths <= mortality_scale[1]:
      new_dict[1].append(hurricane)
    elif num_deaths <= mortality_scale[2]:
      new_dict[2].append(hurricane)
    elif num_deaths <= mortality_scale[3]:
      new_dict[3].append(hurricane)
    elif num_deaths <= mortality_scale[4]:
      new_dict[4].append(hurricane)
    else:
      new_dict[5].append(hurricane)
  return new_dict

mortality_dict = (mortality_scale(hurricane_dict))

# write your greatest damage function here:
def highest_damage(dictionary):
  highest_damage = 0
  hurricane = "hurricane name"
  for data in dictionary:
    if dictionary[data]["Damage"] == "Damages not recorded":
      pass
    elif dictionary[data]["Damage"] > highest_damage:
      highest_damage = dictionary[data]["Damage"]
      hurricane = data
  return hurricane, highest_damage

highest_damage_hurricane = (highest_damage(hurricane_dict))

# write your catgeorize by damage function here:
def damage_scale(dict):

  damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  damage_dict = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  for hurricane in dict:
    damage_done = dict[hurricane]["Damage"]
    if damage_done == damage_scale[0]:
      damage_dict[0].append(hurricane)
    elif damage_done == damage_scale[1]:
      damage_dict[1].append(hurricane)
    elif damage_done == damage_scale[2]:
      damage_dict[2].append(hurricane)
    elif damage_done == damage_scale[3]:
      damage_dict[3].append(hurricane)
    elif damage_done == damage_scale[4]:
      damage_dict[4].append(hurricane)
    else:
      damage_dict[5].append(hurricane)
  return damage_dict

damage_dict = (damage_scale(hurricane_dict))