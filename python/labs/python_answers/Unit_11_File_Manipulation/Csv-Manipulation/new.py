"""
title: new.py
author: eam3kzn
date: 6/29/18 9:41 AM
"""

import csv

# Read the addresses csv and set that file to variable address_data
with open('addresses.csv', 'r') as address_data:
    reader = csv.DictReader(address_data)  # Use the CSV Dictionary Reader to make an ordered dictionary called variable reader
    headers = list(reader.fieldnames)  # Set variable header to a list which is the first line of the file
    addresses = []  # Setting variable addresses to an empty list
    # Create a for loop to loop around the reader object
    for row in reader:
        row = dict(row)  # Cast each row to a dictionary saved in variable row
        addresses.append(row)  # Append each dictionary row to the empty list addresses

# Deleting all addresses in Address Line column
for row in addresses:
    del row["Address Line"]

# You have to remove Address Line from the list of headers so that it does not remain once we remove the rest of the address column
headers.remove("Address Line")

# Open and create a new csv file and set to address_data
with open('addresses_altered.csv', 'w') as address_data:
    writer = csv.DictWriter(address_data, fieldnames=headers)  # Set variable writer to the DictWriter
    writer.writeheader()
    writer.writerows(addresses)
