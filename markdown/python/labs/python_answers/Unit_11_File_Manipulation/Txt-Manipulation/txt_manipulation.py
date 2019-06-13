"""
title: file_manipulation
author: eam3kzn
date: 6/12/18 3:37 PM
"""

# #Reading
# days_file = open('days.txt','r')
# days = days_file.readlines()
#
# num_lines = len(days)
# for i in range(num_lines):
#     days[i] = "Yay! It's " + days[i]
#
# #Writing
# title = "Days of the Week\n"
#
# new_days = open('days.txt', 'w')
#
# new_days.write(title)
# new_days.writelines(days)
#
# #Closing
# days_file.close()
# new_days.close()

# Opens the text file in read mode and sets the contents of the file to variable days_file
with open('days.txt', 'r') as days_file:
    days = days_file.readlines()  # Sets variable days to a list of all of the lines within the file

# Sets num_lines as the length of the days list
# Loop through the range of num_lines length
# Set the index of the days list and append the string plus the actual value of the index
num_lines = len(days)
for i in range(num_lines):
    days[i] = "Yay! It's " + days[i]

# Sets variable title to string
title = "Days of the Week\n"

# Write is creating a new text file and setting it to variable new_days
# The next line is writing the title we set above as the first line of the new file
# The last line is writing all of the lines from the days list which was changed in the for loop into the new days file
with open('new_days.txt', 'w') as new_days:
    new_days.write(title)
    new_days.writelines(days)
