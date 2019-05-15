"""
title: json_manipulation
author: eam3kzn
date: 6/13/18 4:17 PM
"""

import json

# medical_rooms = open('medical.json', 'r')
# data = json.load(medical_rooms)
# pretty_output = json.dumps(data, indent=4)
#
# for room_name in data:
#     print(room_name)
#     data[room_name]['price'] = data[room_name]['price'] * 0.5
#     print(data[room_name]['price'])

with open('medical.json', 'r') as medical_rooms:
    data = json.load(medical_rooms)
    pretty_output = json.dumps(data, indent=4)
    print(pretty_output)

for room_name in data:
    data[room_name]['price'] = data[room_name]['price'] * 0.5
    print(f"{data[room_name]['price']}")

with open('new_medical.json', 'w') as medical_rooms:
    json.dump(data, medical_rooms, indent=4)
