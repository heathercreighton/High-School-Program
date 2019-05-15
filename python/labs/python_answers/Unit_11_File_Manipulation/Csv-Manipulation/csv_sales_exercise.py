"""
title: csv_sales_exercise
author: eam3kzn
date: 6/29/18 10:36 AM
"""

# Always import csv module to be able to use csv methods
import csv
import math


# Finds the difference using square root between both latitudes and longitudes.
def dist_form(lat1, long1, lat2, long2):
    return math.sqrt((lat1 - lat2)**2 + (long1 - long2)**2)


# Using with keyword to open and read the sales data file and set as sales_data variable
with open('SalesJan2009.csv', 'r') as sales_data:
    read_csv = csv.DictReader(sales_data)  # Using the dictionary reader to read the sales_data file
    headers = list(read_csv.fieldnames)  # Putting headers into a list
    sales = []  # Creating a sales empty list for future use

    # This for loop is looping over the read csv and also noting the number index of the item in the list.
    for i, row in enumerate(read_csv, 1): # Enumerate starting at 1, instead of 0
        row = dict(row)  # Casting variable row into a dictionary
        sales.append(row)  # Adding on dictionary row inside of the sales list we previously initialized
        lat_difference = float(row['Latitude']) - 30.2672  # Setting variable lat_difference by targeting the key of the row dictionary and subtracting the Austin latitude
        long_difference = float(row['Longitude']) - 97.7431  # Setting variable long_difference by targeting the key of the row dictionary and subtracting the Austin longitude
        print(f"Transaction # {i :0>3} {round(abs(lat_difference), 2) :>10} {round(abs(long_difference), 2) :>10}")  # Printing with string formatting, the index number and the rounded, absolute value of the difference. We formatted the spacing between columns by using the ":>10" syntax.

# This adds two headers onto the end of the headers list
headers.extend(['Distance', 'Potential Friend'])

# Created a new for loop to use the previous copy/pasted dist_form() function to find the distance between the given lat and long and Austin's lat and long
for i, row in enumerate(sales):
    distance = dist_form(float(row['Latitude']), float(row['Longitude']), 30.2672, 97.7431) # Invoking the dist_form() function that we defined above
    sales[i]['Distance'] = distance  # This puts our newly defined distance under the Distance column on the CSV file
    sales[i]['Potential Friend'] = distance < 100  # This puts our newly defined distance as a True or False (higher or lower than 100) under the Potential Friend on the CSV file

# Write to and create a new sales csv file to write all of our previous changes into a new file!
with open('newSalesJan2009.csv', 'w') as new_sales_data:
    writer = csv.DictWriter(new_sales_data, fieldnames=headers)
    writer.writeheader()
    writer.writerows(sales)
