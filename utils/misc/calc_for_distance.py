import math

from utils.misc import show_on_gmaps
from aiogram import types

from data.locations import Attractions

# Радиус
R = 6378.1


def cal_distance(lat1, lon1, lat2, lon2):
    # Преобразовываем
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)

    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    delta_lon = lon2 - lon1
    delta_lat = lat2 - lat1

    a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon / 2) ** 2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Итоговое расстояние
    distance = R * c

    return distance


def choose_nearest(location: types.Location):
    distance = list()
    for attract_name, attract_local in Attractions:
        distance.append((attract_name,
                         cal_distance(location.latitude, location.longitude, attract_local["lat"], attract_local["lon"]),
                         show_on_gmaps.show(**attract_local),
                         attract_local
                         ))
        return sorted(distance, key=lambda x: x[1])[:2]
