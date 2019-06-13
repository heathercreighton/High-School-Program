"""
title: json_hd_exercise
author: eam3kzn
date: 6/22/18 1:33 PM
"""

import json

# Home Depot Stores Exercise
with open('stores.json', 'r') as hd_stores:
    data = json.load(hd_stores)
    pretty_output = json.dumps(data, indent=4)

for hd_stores in data:
    print(f"Address: {hd_stores['addressLine1']} \n City: {hd_stores['cityName']} \n State: {hd_stores['stateCode']} \n Zip: {hd_stores['postalCode']}")
