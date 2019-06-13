"""
title: csv_manipulation
author: eam3kzn
date: 6/13/18 3:31 PM
"""

import csv

with open('addresses.csv', 'r') as address_data:
    reader = csv.DictReader(address_data)
    print(help(csv.DictReader))
    for i in reader:
        print(i)
    headers = reader.fieldnames
    addresses = []
    for row in reader:
        row = dict(row)
        addresses.append(row)

    for row in addresses:
        del row["Address Line"]

headers.remove("Address Line")

with open('addresses_changed.csv', 'w') as address_data:
    writer = csv.DictWriter(address_data, fieldnames=headers)
    writer.writeheader()
    writer.writerows(addresses)



# with open('addresses.csv', 'r') as address_data:
#     read_address_data = csv.reader(address_data)
#     list_address_data = list(read_address_data)
#     list_address_data[2] = ['Reese', 'Witherspoon', '362 Main St', 'Austin', 'TX', '78704']
#     list_address_data[3][0] = 'Elizabeth'
#     for i, row in enumerate(list_address_data):
#         print(f"Row #: {i} {row}")
#
# with open('new_addresses.csv', 'w', newline='') as address_data_file:
#     write_address_data = csv.writer(address_data_file)
#     write_address_data.writerows(list_address_data)
#     write_address_data.writerow(['Alegra', 'Cole', '1 Broadway Rd', 'New York City', 'NY', 15432])

# Dictionary Formatting

# Come back to the Dictionary formatting section: https://pages.github.homedepot.com/OM-Python/python-foundation/unit-25-file-manipulation.html#dictionary_formatting
