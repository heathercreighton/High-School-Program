"""
title: json_manipulation
author: exp0ct5
date: 10/3/18 10:51 AM
"""
import json
import math
import requests
from config import *

def dist_form(lat1, long1, lat2, long2):
    return math.sqrt((lat1 - lat2)**2 + (long1 - long2)**2)


def find_farthest_store(lat, long):
    with open('stores.json') as stores:
        store_data = json.load(stores)

        # for i in range(len(store_data)):
        #     if store_data[i]['locationType'] == "STR":
        #         print(f"{store_data[i]['addressLine1']} {store_data[i]['cityName']} {store_data[i]['stateCode']} "
        #               f"{store_data[i]['postalCode']}")

        farthest_store_index = -1

        farthest_dist = dist_form(float(store_data[0]['latitudeNumber']), float(store_data[0]['longitudeNumber']),
                                  lat, long)

        for i, row in enumerate(store_data):
            distance = dist_form(float(row['latitudeNumber']), float(row['longitudeNumber']), lat, long)
            row['distance'] = distance

            if distance >= farthest_dist:
                farthest_dist = distance
                farthest_store_index = i

        print(f"Distance from Home Depot Technology Center: {farthest_dist}")
        print(f"{store_data[farthest_store_index]['addressLine1']}, {store_data[farthest_store_index]['cityName']}, "
              f"{store_data[farthest_store_index]['stateCode']} {store_data[farthest_store_index]['postalCode']}")


        store_api = f"http://api.openweathermap.org/data/2.5/weather?lat={store_data[farthest_store_index]['latitudeNumber']}&lon={store_data[farthest_store_index]['longitudeNumber']}&units=imperial&APPID={API_KEY}"
        store_response = requests.get(store_api).json()['main']
        curr_loc_api = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&units=imperial&APPID={API_KEY}"
        curr_loc_response = requests.get(curr_loc_api).json()['main']
        print(f"""Weather at {store_data[farthest_store_index]['locationNumber']}: {store_response['temp']}°F  {store_response['humidity']} %
Weather at {lat}* {long} {curr_loc_response['temp']}°F  {curr_loc_response['humidity']} %""")


def main():
    find_farthest_store(33.918970, -84.496272)


if __name__ == "__main__":
    main()
