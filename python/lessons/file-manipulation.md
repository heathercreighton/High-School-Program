---
title: "file-manipulation"
type: "lesson"
---
Before talking about how to read and write to a file, we need to figure out direct the program to the location of the file. To locate a file, there are two different ways to do so: **absolute** vs. **relative** file paths.

### Absolute File Paths

Most file systems are hierarchical, forming a **tree** that begins with a **root** directory. An absolute filename specifies where the file is stored from the root.

- In Windows, the root is typically indicated by the startup drive letter, such as `C:\`
    
- In Mac and Linux systems, the root is typically indicated by `/`

For example: the absolute file path of admin (in the green box below) is `C:\\Users\\admin`

![File System](img/file-manipulation/file-system.png)

### Relative File Paths

Most operating systems and programming languages remember one location in the file system as your "present working directory". A file can be described relative to that location: a **relative file path**.

For example: In the above picture, the relative file path of `nice.jpg` from `admin` is `../Student login/Desktop/nice.jpg`. The two dots at the beginning represent "go up one directory".

## File Permissions

To open a file in Python, we first need some way to associate the file with a variable in Python. This process is called opening a file. First, Python needs to know where the file is located. Since we created our files within the same directory and we are using relative file paths, we only need to say the name of the file.

We will use Python's `open()` function to open our files. The `open()` function requires the path the file (just the file name in our case) as the first argument. The function also allows from many other parameters. However, most important is the optional mode parameter.

**Mode** is an optional string that specifies the mode in which the file is opened. This mode you choose will depend on what you wish to do with the file. Here are some of our mode options: `r`, `r+`, `w`, `w+`, `a`, and `a+`.

|  | `r` | `r+` | `w` | `w+` | `a` | `a+` |
| --- | --- | --- | --- | --- | --- | --- |
| read | ✔ | ✔ |  | ✔ |  | ✔ |
| write |  | ✔ | ✔ | ✔ | ✔ | ✔ |
| write after seek |  | ✔ | ✔ | ✔ |  |  |
| create |  |  | ✔ | ✔ | ✔ | ✔ |
| truncate |  |  | ✔ | ✔ |  |  |
| position at start | ✔ | ✔ | ✔ | ✔ |  |  |
| position at end |  |  |  |  | ✔ | ✔ |

![opening files](img/file-manipulation/opening_files.png)

## File Types

Python is a great tool for processing data. It is likely that any program you write will involve reading, writing, or manipulating data. For this reason, it's especially useful to know how to handle different file formats, which store different types of data.

Python is super accommodating and can, with relative ease, handle a number of different file formats, including but not limited to the following:

| File Type | Description |
| --- | --- |
| txt | Plain text file stores data that represents only characters (or strings) and excludes any structured metadata |
| CSV | Comma-separated value file uses commas (or other delimiters) to structure stored data, allowing data to be saved in a table format |
| JSON | JavaScript Object Notation is a simple and efficient format, making it one of the most commonly used formats to store and transfer data |

###  `txt` Files

#### Creating

Before we can begin working in Python, we need to make sure we have a file to work with. To do this:

- Open up PyCharm.
    
- Right click on the project name in the Project panel on the left of your window. (Just like you do to create a new Python file)
    - New > File   
    - Type `days.txt`. Make sure to type the `.txt`
        
In the new file, enter a few lines of text. In this example, list the days of the week:
```
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
```
Make sure to save your file (`Command` \> `S`)

#### Opening

Create a Python file called `txt_manipulation.py`.

In this example, we only want to read from the file, so we will use the `'r'` mode. We will use the `open()` function to open the `days.txt` file and assign it to the variable `days_file`. We are going to use the `with` statement and have all lines of code that deal with the file inside of this statement. This ensures that the file is properly and safely opened and closed. The `as` operator creates a variable that is now pointing to the location of the file.
```python
with open('days.txt', 'r') as days_file:
After we have opened the file, we can then read from it.
```
#### Reading

Since our file has been opened, we can now manipulate it (i.e. read from it) through the variable we assigned to it. Python provides three related operations for reading information from a file. We will show how to use all three operations as examples that you can try out to get an understanding of how they work.

**read()**

`<file>.read()` returns the entire contents of the file as a single string. (Remember to indent so you are inside of the `with` statement)
```python
print(days_file.read())
```
Output:
```
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
```
**readline()**

`<file>.readline()` returns the next line of the file, returning the text up to and including the next newline character. More simply put, this operation will read a file line-by-line. (Remember to indent so you are inside of the `with` statement)
```python
print(days_file.readline())
```
Output:
```
Monday
```
Therefore, once you read a line with the readline operation it will pass to the next line. So if you were to call this operation again, it would return the next line in the file, as shown. c
```python
print(days_file.readline())
print(days_file.readline())
```
Output:
```
Monday

Tuesday
```
There is an extra line after `Monday` due to `\\n` that is technically in the text file to start `Tuesday` on the next line. To show all of the lines of code in the file, you could use a loop and call the `days_file.readline()`, but there is a command that does this for you.

**readlines()**

`<file>.readlines()` returns a list of the lines in the file, where each item of the list represents a single line.
```python
print(days_file.readlines())
```
Output:
```
Monday\n', 'Tuesday\n', 'Wednesday\n', 'Thursday\n', 'Friday\n', 'Saturday\n', 'Sunday']
```
Something to keep in mind when you are reading from files, once a file has been read using one of the read operations, it cannot be read again. For example, if you were to first run `days_file.read()` followed by `days_file.readlines()` the second operation would return an empty string. Therefore, anytime you wish to read from a file you will have to first open a new file variable. Now that we have read from a file, let's learn how to write to a new file.

#### Modifying

It is not easy to use `open` to edit in the middle of a file. To simulate this happening, we can alter the list that is returned from `readlines()` and eventually write it directly back to the file we read it from.

For example, if we wanted to add `Yay! It's` to the beginning of every line of the file we could loop through and add it to the string at each index, like:
```python
with open('days.txt', 'r') as days_file:
  days = days_file.readlines()

num_lines = len(days)
for i in range(num_lines):
    days[i] = "Yay! It's " + days[i]
```
#### Writing

We also need to store the days of the week in a string variable, which we'll call `days`. So far we opened the file in read mode, read the file, and store the returned output from the read operation in our new variable `days`.

We state that we want to enter in `write` mode. Remember, this will truncate any text already in the file specified. That is fine for our purposes since we have stored the existing text in a list.
```python
with open('days.txt', 'w') as new_days:
```
Now we can place a single string into the new file with `write()`. (Remember to indent so you are inside of the `with` statement)
```python
new_days.write("Days of the Week\n")
print(title)
```
We can place a list of Strings into the new file with `writelines()`. (Remember to indent so you are inside of the `with` statement)
```python
new_days.writelines(days)
print(days)
```
Full Code
```python
with open('days.txt', 'r') as days_file:
  days = days_file.readlines()

num_lines = len(days)
for i in range(num_lines):
    days[i] = "Yay! It's " + days[i]

title = "Days of the Week\n"

with open('days.txt', 'w') as new_days:
  new_days.write(title)
  new_days.writelines(days)
```
Output:
```
Days of the Week

Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
```
The values of `days.txt` should look like the following:
```
Days of the Week
Yay! It's Monday
Yay! It's Tuesday
Yay! It's Wednesday
Yay! It's Thursday
Yay! It's Friday
Yay! It's Saturday
Yay! It's Sunday
```

### `csv` Files

CSV stands for "comma-separated values", and CSVs are simplified spreadsheets which are stored as plain text files, so it's easy for Python to parse through and for us to manipulate them.

CSV files are simple, lacking many of the features of an Excel spreadsheet. For example, CSV files don't have types for their values — everything is a string. The advantage of a CSV is simplicity.

- Create a new Python file called `csv_manipulation.py`
    
- Download this CSV: [Addresses](img/csv-image/addresses.csv)
    
    
    - Drag it into your PyCharm project.
        
    

#### Opening

The first step to read CSV files in Python is to import the `csv` module. Since the `csv` module comes with Python when you download it, we don't have to install it separately.
```python
import csv
```
We'll also need to open the file and save it to memory for Python to be able to read.
```python
with open('addresses.csv', 'r') as address_data:
```
#### Reading

We now have to read the file that has been opened by passing the variable `address_data` into method `reader()` which calls upon the `csv` module that we imported on the first line on this file. That is all set to a variable called `read_address_data` so that we can use that read material to list or manipulate. `read_address_data` is

read_address_data = csv.reader(address_data)
In order for Python to give us a neat `list` of our data for us to manipulate, **cast** the the `read_address_data` variable with `list()` and print it out.
```python
list_address_data = list(read_address_data)
```
This is is all of the contents of the csv file placed into a readable, mutable list.

The `Reader` object which we're calling by using `csv.reader()` can only be looped over once per call. If there was an update to the `csv` file, we would need to call `csv.reader()` again. This helps split each row into it's own list and every cell is an element in the row.

#### Accessing

Now that we have a nice list, we can access each line/cell.
Similarly to accessing indexes of a list, we're going to use the bracket notation to access the rows and columns of the CSV file. If we want to list out just the cell of the 2nd column from the 5th row, we'll print this:
```python
print(list_address_data[4][1])
```
Output:
```
Tyler
```
The syntax is `list_address_data[row][col]`

* * *

Since we can pull data out using indexes, we can also utilize a statement we learned previously to grab data more efficiently: the `for` loop. Now we can print out the rows and read them all easily within PyCharm.

Now we'll start our `for` loop below the line that states `list_address_data = list(read_address_data)`:
```python
for i, row in enumerate(list_address_data):
    print(f"Row #: {i} {row}")
```
`enumerate` in the above `print()` statement helps us keep track of the row numbers and the current row values.

#### Modifying

Now that the information is stored in a list, we are able to add or modify existing values.

Changing row 2's values
```python
list_address_data[2] = ['Reese', 'Witherspoon', '362 Main St', 'Austin', 'TX', '78704']
```
Changing row 3, column 1's value
```python
list_address_data[3][0] = 'Elizabeth'
```
The above examples changed the list, **not** the `csv` file. In order to change the actual file, we would need to write the new information to the csv file.

#### Writing

We know how to read CSV files, now let's write to one. We'll use a similar syntax: `csv.writer()` on the same file.

First, we must use the `open()` method with `w` mode: `address_data = open('addresses.csv', 'w')`

Then, we can use the `Writer` object on our new variable, and specify that we'd like to write a new row with a new set of strings.
```python
with open('addresses.csv', 'w') as address_data_file:
  write_address_data = csv.writer(address_data_file)
```
Run your code. If we open up the csv file, `addresses.csv`, we will see that there is no longer any text inside the file.

- If the file specified does not exist, `writer` creates a new, empty file with the name specified.
    
- If the file specified exists, `writer` opens up a file and "erases" any existing text inside the file.
    
---
It is not an issue that the text has been erased due to the fact we stored all of the text into the list `list_address_data`.

---

To write multiple rows, you would use `writerows` and **pass in** a list. In the following code, we are going to pass in the list, `list_address_data`. This will place all of the lines that were previously in the csv file after the above line.

write_address_data.writerows(list_address_data)
At this point, `addresses.csv` has all of the text that was originally in that file.

We can use the `writerow()` method to specify that we'd like to write to a single **row** to the **end** of the CSV file. Each value we place into `writerow()` will become its own cell in the output CSV file.

```python
write_address_data.writerow(['Alegra', 'Cole', '1 Broadway Rd', 'New York City', 'NY', 15432])
```

Full Code

```python
import csv

with open('addresses.csv', 'r') as address_data:
  read_address_data = csv.reader(address_data)
  list_address_data = list(read_address_data)
  list_address_data[2] = ['Reese', 'Witherspoon', '362 Main St', 'Austin', 'TX', '78704']
  list_address_data[3][0] = 'Elizabeth'

with open('addresses.csv', 'w') as address_data_file:
  write_address_data = csv.writer(address_data_file)
  write_address_data.writerows(list_address_data)
  write_address_data.writerow(['Alegra', 'Cole', '1 Broadway Rd', 'New York City', 'NY', 15432])
```
#### Dictionary Formatting

When using `csv` files it is possible to return the data from the file as a dictionary where the keys are the header values and the values are the corresponding rows with them. To read in the information from `addresses.csv` and convert it to an **ordered** dictionary, you can do the following:
```python
import csv

with open('addresses.csv', 'r') as address_data:
  reader = csv.DictReader(address_data)
```
#### Reading

If you wanted to print out all of the last names in the `csv` file, you can now use the key `Last Name`.
```python
import csv

with open('addresses.csv', 'r') as address_data:
  reader = csv.DictReader(address_data)

  for row in reader:
    print(row['Last Name'])
```
Output:
```
Doe
Witherspoon
Repici
Tyler
Cole
```
To get a list of all of the headers, call the `reader` object's variable, `fieldnames`. (Make sure this is indented since you are using the reader object)
```python
headers = reader.fieldnames
```
Prints out all of the information in a csv file
```python
import csv

with open('addresses.csv', 'r') as address_data:
    reader = csv.DictReader(address_data)
    headers = reader.fieldnames
    addresses = list(reader)
```
Each row is an `OrderedDict`. To convert an `OrderedDict` to a dictionary, you simply cast it to a `dict`. Since a `csv` file is essentially lists of dictionaries, we could cast each row to a dictionary and append it to a list.

The following adds each row (which is casted to a dictionary) of the `reader` object to a list
```python
import csv

with open('addresses.csv', 'r') as address_data:
    reader = csv.DictReader(address_data)
    headers = reader.fieldnames
    addresses = list(reader)
```
Output if you were to print out the contents of `addresses` you would get:
```python
[{'First Name': 'John', 'Last Name': 'Doe', 'Address Line': '120 jefferson st.', 'City': 'Riverside', 'State': ' NJ', 'Zipcode': '8075'}, {'First Name': 'Jack', 'Last Name': 'McGinnis', 'Address Line': '220 hobo Av.', 'City': 'Phila', 'State': ' PA', 'Zipcode': '9119'}, {'First Name': 'John Da Man', 'Last Name': ' Repici', 'Address Line': ' 120 Jefferson St.', 'City': 'Riverside', 'State': ' NJ', 'Zipcode': '8075'}, {'First Name': 'Stephen', 'Last Name': 'Tyler', 'Address Line': '7452 Terrace At the Plaza road', 'City': 'SomeTown', 'State': 'SD', 'Zipcode': '91234'}]
```

#### Modifying

If you wanted to alter the dictionary to no longer include the `Address Line`, you could delete `Address Line` from each row in the `list`.
```python
import csv

with open('addresses.csv', 'r') as address_data:
    reader = csv.DictReader(address_data)
    headers = reader.fieldnames
    addresses = list(reader)

for row in addresses:
    del row["Address Line"]
```
The contents of the list of dictionaries no longer contains the `Address Line` column.

Make sure to delete `Address Line` from the `headers` list. (The reason for this will be seen in the next step)
```python
headers.remove('Address Line')
```

#### Writing

A `DictWriter` object helps with writing the dictionary to a file. A `DictWriter` object requires the name of the opened file variable, and the `fieldnames`. `fieldnames` are the titles of each column, or the `keys`. We had already got a list of all of the headers and placed it in the `headers` list.
```python
with open('addresses.csv', 'w') as address_data:
  writer = csv.DictWriter(address_data, fieldnames=headers)
```
Call `writer.writeheader()` to add a row with the field names (as specified in the constructor) to the constructor.

```python
writer.writeheader()
```

Write each row by passing the list of dictionaries to the csv file with `writer.writerows(addresses)`
```python
writer.writerows(addresses)
```

#### Full Code
```python
import csv

with open('addresses.csv', 'r') as address_data:
    reader = csv.DictReader(address_data)
    headers = reader.fieldnames
    addresses = list(reader)

for row in addresses:
    del row["Address Line"]

headers.remove("Address Line")

with open('addresses_altered.csv', 'w') as address_data:
    writer = csv.DictWriter(address_data, fieldnames=headers)
    writer.writeheader()
    writer.writerows(addresses)
```

### `json` Files

JSON (JavaScript Object Notation) is an easy to read, flexible text based format that can be used to store and communicate information to other products. It is mainly based on key:value pairs and is web and .NET friendly. There are many libraries and products that support JSON.

JSON could be used to store information for a door schedule, or a parts list. A report can be created on the name, size and location of all the bitmaps in a model. JSON files are used in several other places and products. JSON is also easy to display on dynamic webpages.

Here is an example of a JSON structure describing a medical office. As you will see in the example, the medical space includes 5 rooms, with square footage and pricing for each dedicated space.
```python
{
  "reception": {
    "room-number": 100,
    "sq-ft": 50,
    "price": 75
  },
  "waiting": {
    "room-number": 101,
    "sq-ft": 250,
    "price": 75
  },
  "examination": {
    "room-number": 102,
    "sq-ft": 125,
    "price": 150
  },
  "on-call": {
    "room-number": 103,
    "sq-ft": 125,
    "price": 150
  },
  "office": {
    "room-number": 104,
    "sq-ft": 150,
    "price": 100
  }
}
```
Create a new Python file called `json_manipulation.py`
    
- Create a new file called `medical.json`
    

#### Opening

The first step to read JSON files in Python is to import the `json` module. Since the `json` module comes with Python when you download it, we don't have to install it separately.

import json
We'll also need to open the file and save it to a letter for Python to be able to read.
```python
with open('medical.json', 'r') as medical_rooms:
```

#### Reading

To convert the information from the `json` file, you must use `json.load`. It reads the string from the file, parses the JSON data, populates and returns a Python `dict` with the data.
```python
data = json.load(medical_rooms)
```
If we wanted to see the entirety of the new dictionary print in a neat format you can use `json.dumps`. This takes in the dictionary you want to print and has an optional parameter to specify the number of characters you would like to use for the indent. There is a another optional parameter `sort_keys` that states if you want the keys to print in a sorted order.
```python
pretty_output = json.dumps(data, indent=4)
```
If you were to `print``pretty_output`, you would get the following output:
```python
{
  {"examination": {
        "price": 150,
        "room-number": 102,
        "sq-ft": 125
    },
    "office": {
        "price": 100,
        "room-number": 104,
        "sq-ft": 150
    },
    "on-call": {
        "price": 150,
        "room-number": 103,
        "sq-ft": 125
    },
    "reception": {
        "price": 75,
        "room-number": 100,
        "sq-ft": 50
    },
    "waiting": {
        "price": 75,
        "room-number": 101,
        "sq-ft": 250
    }
}
```

#### Accessing

If you wanted to access all of the room names in the `medical_rooms` dictionary, you could use a for loop.
```python
for room_name in data:
    print(room_name)
```
Output:
```
reception
waiting
examination
on-call
office
```
If you wanted to print out the room names and the room numbers, you could use a loop, as shown below:
```python
for room_name in data:
    print(f"{room_name} is in room {data[room_name]['room-number']}")
```
Notice that [room_name] is not surrounded with quotes. This is because `room_name` is a looping variable that is created in the for loop, returning the name of the current room for each iteration.

#### Modifying

Now that the `json` file contents have been placed in a dictionary, modifying the contents is identical to how you change a dictionary.

Say that there is a deal on rooms that makes every room 50%. If you wanted to go through and change the value of every room to half off, you could do this as follows:
```python
for room_name in data:
    data[room_name]['price'] = data[room_name]['price'] * 5
```
If you were to print out the contents of the dictionary, you would see the updated prices.

#### Writing

To write back the new information, you first need to open up the file in `w` mode.
```python
with open('medical.json', 'w') as medical_rooms:
```
Use `json.dump` to place the dictionary into the file. This method takes in the dictionary, filename to write to and optionally the number of indents to place.
```python
json.dump(data, medical_rooms, indent=4)
```
Full Code
```python
import json

with open('medical.json', 'r') as medical_rooms:
  data = json.load(medical_rooms)

for room_name in data:
    data[room_name]['price'] = data[room_name]['price'] * 0.5
    print(f"{data[room_name]['price']}")

with open('medical.json', 'w') as medical_rooms:
  json.dump(data, medical_rooms, indent=4)
```

### Python and APIs

When a company offers an Application Programming Interface's(API) to their customers, it just means that they've built a set of dedicated URLs that return pure data responses — meaning the responses won't contain the kind of presentational overhead that you would expect in a graphical user interface like a website.

**Example Scenario**

Your business's website has a form used to sign clients up for appointments. You want to give your clients the ability to create a Google calendar event with the details for that appointment.

**API use:** The idea is to have your website's server talk directly to Google's server with a request to create an event with the given details. Your server would then receive Google's response, process it, and send back relevant information to the browser, such as a confirmation message to the user.

Alternatively, your browser can often send an API request directly to Google's server bypassing your server. To render the whole web page, your browser expects a response in HTML, which contains presentational code, while Google Calendar's API call would just return the data — likely in a format like JSON.

* * *

But why use an API instead of a static dataset you can download? APIs are useful in the following cases:

- The data is changing quickly.
    
- You want a small piece of a much larger set of data.
    
- There is repeated computation involved.
    

### Weather API

We are going to use the OpenWeatherMap API found at: [http://api.openweathermap.org](http://api.openweathermap.org).

- To use this API, you first need to create an **API key**. An **API key** acts as both a unique identifier and a secret token for authentication, and will generally have a set of access rights on the API associated with it.
    
    
    - To get an API key with OpenWeatherMap, you have to sign up here: [https://home.openweathermap.org/users/sign_up](https://home.openweathermap.org/users/sign_up)
        
    

Now that you have the API key, you can now make an API call to get the current weather information from Austin, Texas.
```python
import requests
import json
command = f"http://api.openweathermap.org/data/2.5/weather?q=Austin,us&units=imperial&APPID={API_KEY_VARIABLE}"
response = requests.get(command)
```

Replace `{YOUR_API_KEY}` with the variable you set it to within your `config.py` file. Do not forget to put your `config.py` file into a `.gitignore` file before you push to GitHub.

If you wanted to see other cities you can use and how to call them, go to: [https://openweathermap.org/current](https://openweathermap.org/current) |

`response` now holds the information that was returned from the API. If you were to print the value currently stored in `response`, you would get the output: `<Response [200]>`. This means you successfully got back a result from the API call.

To actually see the data retrieved from the API call in a `json` format, you have to do the following:
```python
print(json.dumps(response.json(), indent=4))
```
Weather changes, so here is just ONE example output:
```python

{
  "coord": {
      "lon": -97.74,
      "lat": 30.27
  },
  "weather": [
      {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03d"
      }
  ],
  "base": "stations",
  "main": {
      "temp": 84.18,
      "pressure": 1019,
      "humidity": 70,
      "temp_min": 80.6,
      "temp_max": 87.8
  },
  "visibility": 16093,
  "wind": {
      "speed": 9.17,
      "deg": 210
  },
  "clouds": {
      "all": 48
  },
  "dt": 1528903320,
  "sys": {
      "type": 1,
      "id": 2557,
      "message": 0.0041,
      "country": "US",
      "sunrise": 1528889323,
      "sunset": 1528940028
  },
  "id": 4671654,
  "name": "Austin",
  "cod": 200
}
```
If we wanted to work with the json data that is returned, we can set a variable to the value returned with `response.json()`.
Calling the 'main' key of the response
```python
import requests
import json

command = "http://api.openweathermap.org/data/2.5/weather?q=Austin,us&units=imperial&APPID={YOUR_API_KEY}"
response = requests.get(command)

austin_data = response.json()
print(austin_data['main'])
```
Output:
```
temp': 84.18, 'pressure': 1019, 'humidity': 70, 'temp_min': 80.6, 'temp_max': 87.8}
```

#### Printing response in a formatted print
```python
austin_data = response.json()
print(f"""Temperature: {austin_data['main']['temp']} F
Humidity: {austin_data['main']['humidity']}%""")
```
Output:
```
Temperature: 87.8 F
Humidity: 55%
```