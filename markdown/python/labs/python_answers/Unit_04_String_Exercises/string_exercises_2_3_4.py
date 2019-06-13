"""
title: string_exercises_2_3_4
author: eam3kzn
date: 6/11/18 2:19 PM
"""

import random

# Credentials generator
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_city = input("Enter the city you were born in: ")
alumni = input("Enter the university you graduated from: ")
relative = input("Enter the name of a relative: ")
friend = input("Enter the name of a friend: ")

employee_id = first_name[:3] + last_name[-2:]
user_name = birth_city[:2] + alumni[-3:]

rnd_relative = random.randint(0, len(relative) - 1)
rnd_friend = random.randint(1, len(friend))
password = relative[rnd_relative:] + friend[:rnd_friend]

# BONUS
password = password[0].upper() + password[1:].lower()

print("Employee ID: " + employee_id)
print("User Name: " + user_name)
print("Password: " + password)

# Remove Case and Punctuation
enter_string = input("Enter a phrase: ")
string_modified = enter_string.lower().replace(",", "").replace(" ", "").replace("'", "")
print(string_modified)

# Palindrome
phrase = input("Enter a phrase: ")
print("Palindrome?", phrase == phrase[::-1])
