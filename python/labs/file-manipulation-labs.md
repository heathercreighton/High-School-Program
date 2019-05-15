---
title: "file-manipulation-labs"
type: "lab"
---
Instructions

-  Download this `txt`: [Names](img/file-manipulation/names.txt) and drag it into your PyCharm project
    
-  Create a new file (if you have not already) called `txt_manipulation.py`
    
-  Read in all of the lines from `names.txt` and store it in a list called `names`. (As shown in the reference page)
    

### Modifying

Use the list `names` in this portion of the exercise.

Instructions

-  For every row in `names`, find if the name starts with a vowel. If so, add the last name `Phillips`. If not, add the last name `Moses`
    

### Writing

Instructions

-  Write all of the information from `names` to the old file called `names.txt`
    
-  Close this new file.
    

|  | 
Go to [csv Reference](unit-25-file-manipulation.html#code_csv_code_files) |

##`csv` Exercise

### Reading

Instructions

-  Download this CSV: [SalesJan2009](img/csv-image/SalesJan2009.csv) and drag it into your PyCharm project
    
-  Create a new file (if you have not already) called `csv_manipulation.py`
    
-  Read in the information from `SalesJan2009.csv` and store it in a list called `list_sales_data`. (As shown in the reference page)
    
-  Print out how many rows there are in `list_sales_data`.
    
-  Print out the row number, and the latitude/longitude of every row inside the csv file, **excluding** the header row.
    
-  Change your print statement to print out the row number and the **difference** of the current latitude from 30.2672° N, and the **difference** of the current longitude from 97.7431° W (Rounded to two past the decimal).
    
    
    - For example: If row 15's latitude and longitude is 50.2983, -120.32, the output would be: `Transaction #15: 20.0311 218.0631`. (Note there are not negative numbers)
        
    
-  Format your print statement to look like the following:
    

![bonus format](img/csv-image/bonus-format.png)

### Modifying

Use the list `list_sales_data` in this portion of the exercise.

Instructions

-  Add two additional header names to `list_sales_data` called `distance` and `potential_friend`. (Remember the location of headers)
    
-  For every row in `list_sales_data` (excluding the header row), calculate the distance between the current location and 30.2672° N, 97.7431° W (Use the distance formula! Round to two past the decimal). Append these values at the end of the row.
    
-  If the distance is less than 100, place `True` in the `potential_friend` column. Otherwise, place `False` in the `potential_friend` column.
    

### Writing

Instructions

-  Write all of the information from `list_sales_data` to a new csv file called `sales_and_friends.csv`.
    
-  Close this new file.
    

|  | 
Go to [json Reference](unit-25-file-manipulation.html#code_json_code_files) |

##`json` Exercise

### Home Depot Stores

Instructions

-  Download this `json`: [Stores](img/file-manipulation/stores.json) and drag it into your PyCharm project
    
-  Create a new file (if you have not already) called `json_manipulation.py`
    
-  Read in all of the lines from `stores.json` and load it in a json called `store_data`. (As shown in the reference page)
    
-  Print all the **stores** (Which are represented with a `STR` in the JSON file) address, city, state and zip code
    
-  Find and print out the address of the **nearest** store location to 30.410177° N, -97.661694° W.
    

Final Output

Distance from Home Depot Technology Center: 0.014446940195068895
13309 I-35 NORTH, AUSTIN, TX 78753
Bonus**

Instructions

-  Create a function that will take in any latitude and longitude and find the nearest Home Depot to that location.
    
-  Create a function that will find the weather(temperature and humidity) of the origin and the destinations.
    

### Google Maps API

- Create an API key with Google Maps Platform here: [https://cloud.google.com/maps-platform](https://cloud.google.com/maps-platform)
    
    
    - Check to enable `Maps`, `Routes`, and `Places`.
        
    - Call your project `JSON Practice`
        
    - It will make you enter credit card information. We are not going to exceed the daily limit, so your card will not be charged. We also can delete the account before the 30 day trial ends.
        
    

The following works to get the directions from `The Home Depot Technology Center` to Universal Studios Hollywood. (Remember to replace {YOUR_API_KEY} with your API key)

def find_directions(origin, destination, key):
	command = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={key}"
	response = requests.get(command)

	directions = response.json()
	route_info = directions['routes'][0]['legs'][0]

	return json.dumps(route_info, indent=4)

if__name__ == "__main__":
	origin = "the+home+depot+technology+center"
	destination = "Universal+Studios+Hollywood4"
	key = "{YOUR_API_KEY}"
	print(find_directions(origin, destination))
Using the above code as a start, create a function that takes in a starting location and ending location and print out the starting address, ending address, distance between locations, and every step. You should get an output similar to the one below:

Going from: 13011B McCallen Pass, Austin, TX 78753, USA
		To: 13609 I-35, Austin, TX 78753, USA
Total distance: 1.4 mi
1 Head <b>north</b> on <b>McCallen Pass</b>
2 Turn <b>left</b> onto <b>Center Ridge Dr</b><div style="font-size:0.9em">Pass by Mattress Firm Final Markdown (on the right in 0.6&nbsp;mi)</div>
3 Turn <b>right</b> onto <b>N Interstate 35 Frontage Rd</b>
4 Turn <b>right</b>
5 Turn <b>left</b><div style="font-size:0.9em">Destination will be on the left</div>
Bonus**

Combine Google Maps API and the Weather API to also output the temperature and humidity of each location.

Example Output

Going from: 13011B McCallen Pass, Austin, TX 78753, USA
		To: 11001 S 1st St, Austin, TX 78748, USA
Total distance: 22.1 mi
Duration: 26 mins
  1 Head <b>north</b> on <b>McCallen Pass</b>
  2 Make a <b>U-turn</b>
  3 Turn <b>right</b> onto <b>E Parmer Ln</b>
  4 Turn <b>left</b> onto <b>N Interstate 35 Frontage Rd</b>
  5 Take the ramp on the <b>left</b> onto <b>I-35 S</b><div style="font-size:0.9em">Pass by Motel 6 Austin Central - N (on the right in 4.7&nbsp;mi)</div>
  6 Keep <b>left</b> at the fork to continue on <b>I-35 S</b>/<b>US-290 W</b>/<b>N Interstate 35</b>, follow signs for <b>32nd St</b>
  7 Keep <b>left</b> to continue on <b>I-35 S</b>
  8 Take exit <b>225</b> toward <b>Onion Creek Pkwy</b>/<b>Farm to Market Rd 1626</b>
  9 Merge onto <b>S IH 35 Frontage Rd</b>
 10 Turn <b>right</b> onto <b>Farm to Market 1626 W</b>
 11 Turn <b>right</b> onto <b>S 1st St</b>
 12 Turn <b>right</b> onto <b>Colonial Dr</b><div style="font-size:0.9em">Restricted usage road</div>
 13 Turn <b>right</b><div style="font-size:0.9em">Restricted usage road</div><div style="font-size:0.9em">Destination will be on the right</div>
============================================================
Origin:
	Temperature: 85.08 F
	Humidity: 66%

Destination:
	Temperature: 85.77 F
	Humidity: 66%
Go To Classes Lesson](unit-27-classes.html)