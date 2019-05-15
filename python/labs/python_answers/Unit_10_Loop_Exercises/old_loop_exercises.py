"""
title: old_loop_exercises
author: eam3kzn
date: 6/13/18 9:25 AM
"""

# Dice Historgram
a = [] # create an empty list
x = random.randint(1, 6)

for roll in range(100):
    a += [x]
    x = random.randint(1, 6)

plt.hist(a)
plt.show()

# Average String Length in List
names = ['Erick', 'Elbert', 'Bonnie', 'Leon', 'Theodore']
total = 0
for name in names:
    total += len(name)

print("\nThe average length is:", total / len(names))

# Find the Max
whole_numbers = [34, 132, 543, 908, 66, 54, 9, 0, 1, 11, 23, 456, 7, 765, 342, 435, 867, 234, 543, 678]
max_number = whole_numbers[0]

for number in whole_numbers:
    if max_number < number:
        max_number = number
print(max_number)