import random

city_names=['Paris', 'London', 'Rome', 'Berlin', 'Madrid']
city_temp ={city:random.randint(20,30) for city in city_names}
print(city_temp)

above_25={city:temp for (city,temp) in city_temp.items() if temp>25}
print(above_25)