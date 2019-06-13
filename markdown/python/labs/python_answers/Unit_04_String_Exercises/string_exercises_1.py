"""
title: string_exercises_1_2
author: eam3kzn
date: 6/11/18 1:54 PM
"""

import random

# Follow Along

# 1
phrase = "Don't count your chickens before they hatch. "

# 2
slogan = "For Everything Else, There's MasterCard"

# 3
combined = phrase + slogan + "."
print(combined)

# 4
print(phrase  * 3)

# 5
print(slogan[6])

# 6
print(combined[-1])

# 7
print(phrase[::2])

# 8
print(phrase[17:25])

# 9
print(combined[::2])

# 10
print('m' in 'slogan')

# 11
print(combined.upper())

# 12
print(" ".join(combined))

# 13
print(slogan[::-1])


# Is this a letter?
letter = input("Enter a character: ")

alphabet = "qwertyuiopasdfghjklzxcvbnm"

print(letter in alphabet)
