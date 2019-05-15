"""
title: txt_manipulation_exercise
author: eam3kzn
date: 6/15/18 11:07 AM
"""

# Opens file in read mode and saves to variable names_file
with open('names.txt', 'r') as names_file:
    names_read = names_file.readlines()  # Sets variable names_read as all of the names in a list (readlines creates a list for us)

# set variable len_names to the length of the names_read list
len_names = len(names_read)
vowels = 'AEIOU'  # Set variable vowels to capital AEIOU for future comparison

# Create a for loop around the range of the length of the names_read list
for i in range(len_names):
    if names_read[i][
        0] in vowels:  # If the first index (name) on the list AND the first character of the first index is A E I O or U, then strip the \n, add a space, the last name Phillips, and add a new line at the end
        names_read[i] = names_read[i][:-1].strip() + " " + "Phillips\n"
    else:
        names_read[i] = names_read[i][:-1].strip() + " " + "Moses\n"
print(names_read)

# Open in write mode which will create a new file we decided to call new_names.txt and set to variable new_names
with open('new_names.txt', 'w') as new_names:
    new_names.writelines(
        names_read)  # This will take the names_read as we set it in the for loop above and set it into the new_names variable which is set to create and write to our new file


"""
title: csv_sales_exercise
author: eam3kzn
date: 6/29/18 10:36 AM
"""

# Always import csv module to be able to use csv methods
import csv
import math


def dist_form(lat1, long1, lat2, long2):
    return math.sqrt((lat1 - lat2)**2 + (long1 - long2)**2)


# Using with keyword to open and read the sales data file and set as sales_data variable
with open('SalesJan2009.csv', 'r') as sales_data:
    read_csv = csv.DictReader(sales_data)  # Using the dictionary reader to read the sales_data file
    headers = list(read_csv.fieldnames)  # Putting headers into a list
    sales = []  # Creating a sales empty list for future use

    # This for loop is looping over the read csv and also noting the number index of the item in the list.
    for i, row in enumerate(read_csv):
        row = dict(row)  # Casting variable row into a dictionary
        sales.append(row)  # Adding on dictionary row inside of the sales list we previously initialized
        lat_difference = float(row['Latitude']) - 30.2672  # Setting variable lat_difference by targeting the key of the row dictionary and subtracting the Austin latitude
        long_difference = float(row['Longitude']) - 97.7431  # Setting variable long_difference by targeting the key of the row dictionary and subtracting the Austin longitude
        #print(f"Transaction # {i :>3} {round(abs(lat_difference), 2) :>10} {round(abs(long_difference),2) :>10}")  # Printing with string formatting, the index number and the rounded, absolute value of the difference. We formatted the spacing between columns by using the ":>10" syntax.

# This adds two headers onto the end of the headers list
headers.extend(['Distance', 'Potential Friend'])

# Created a new for loop to use the previous copy/pasted dist_form() function to find the distance between the given lat and long and Austin's lat and long
for i, row in enumerate(sales):
    distance = dist_form(float(row['Latitude']), float(row['Longitude']), 30.2672, 97.7431)
    sales[i]['Distance'] = distance  # This puts our newly defined distance under the Distance column on the CSV file
    sales[i]['Potential Friend'] = distance < 100  # This puts our newly defined distance as a True or False (higher or lower than 100) under the Potential Friend on the CSV file

# Write to and create a new sales csv file to write all of our previous changes into a new file!
with open('newSalesJan2009.csv', 'w') as new_sales_data:
    writer = csv.DictWriter(new_sales_data, fieldnames=headers)
    writer.writeheader()
    writer.writerows(sales)



"""
title: json_exercise
author: eam3kzn
date: 6/15/18 2:49 PM
"""

import config
import requests
import json

weather = config.weather_api_key
command = "http://api.openweathermap.org/data/2.5/weather?q=Austin,us&units=imperial&APPID=" + weather
response = requests.get(command)

# print(json.dumps(response.json(), indent=4))

austin_data = response.json()
print(f"""Temperature: {austin_data['main']['temp']} F
Humidity: {austin_data['main']['humidity']}%""")


"""
title: json_stores_exercise
author: eam3kzn
date: 6/29/18 3:36 PM
"""

import json
import math


def dist_from(lat1, long1, lat2, long2):
    return math.sqrt((lat1 - lat2)**2 + (long1 - long2)**2)

if __name__ == "__main__":
    current_latitude = 30.2672
    current_longitude = -97.7431
    closest=1000000
    closest_store=""
    with open('stores.json', 'r') as thd_stores:
        store_data=json.load(thd_stores)
        pretty_stores=json.dumps(store_data, indent=4)
        #print(store_data)
        #print(pretty_stores)
        for store in store_data:
            if store['locationType'] == 'STR':
                #print(f"{store['locationNumber']} {store['addressLine1']} {store['cityName']} {store['stateCode']} {store['postalCode']}")
                this_store=f"{store['locationNumber']} {store['addressLine1']} {store['cityName']} {store['stateCode']} {store['postalCode']}"
                distance=dist_from(float(store["latitudeNumber"]), float(store["longitudeNumber"]), current_latitude, current_longitude)
                if distance < closest:
                    closest = distance
                    closest_store=this_store
        print(closest_store)

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
