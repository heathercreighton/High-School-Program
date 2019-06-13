"""
title: csv_to_json
author: eam3kzn
date: 8/29/18 2:00 PM
"""

import csv
import json

with open('addresses.csv', 'r') as address_data:
    reader = csv.DictReader(address_data)
    headers = list(reader.fieldnames)
    addresses = []
    for row in reader:
        row = dict(row)
        addresses.append(row)

with open('csv_to_json.json', 'w') as medical_rooms:
    json.dump(addresses, medical_rooms, indent=4)