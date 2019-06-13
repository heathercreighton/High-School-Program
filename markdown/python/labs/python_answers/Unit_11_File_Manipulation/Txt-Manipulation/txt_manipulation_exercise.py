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
    if names_read[i][0] in vowels:  # If the first index (name) on the list AND the first character of the first index is A E I O or U, then strip the \n, add a space, the last name Phillips, and add a new line at the end
        names_read[i] = names_read[i][:-1].strip() + " " + "Phillips\n"
    else:
        names_read[i] = names_read[i][:-1].strip() + " " + "Moses\n"
print(names_read)

# Open in write mode which will create a new file we decided to call new_names.txt and set to variable new_names
with open('new_names.txt', 'w') as new_names:
    new_names.writelines(names_read)  # This will take the names_read as we set it in the for loop above and set it into the new_names variable which is set to create and write to our new file
