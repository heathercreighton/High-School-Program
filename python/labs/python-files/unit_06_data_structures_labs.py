"""
filename: data_structures_labs.py
author: Elizabeth Phillips
date: May 9th, 2018
description: All of the labs for data structures
"""

import random

print("===Lists===")
'''Follow Along'''
# link:data-structures-labs.html#follow_along
print("Follow Along")
my_friends = ["Rizzo", "French", "Danny", "Kenickie", "Marty", "Sandy", "Cha-Cha", "Patty", "Sonny", "Calhoun"]
print(len(my_friends))
print(my_friends[3])
#print(my_friends[10]) # Gives an error
print(my_friends[-1])
print(my_friends[4:8])
print(my_friends[6:])
print(my_friends[:3])
print(my_friends[::2])
print(my_friends[::-3])
my_friends[7] = "Elizabeth"
print(my_friends)
my_friends.append("Danny")
print(my_friends)
del my_friends[6]
print(my_friends)
my_friends.insert(2, "Sandy")
print(my_friends)
print(my_friends.count("Sandy"))
my_friends.sort()
print(my_friends)

# link:data-structures-labs.html#magic_8_ball
print("Magic 8-Ball")
def shake_eight_ball():
    input("Ask a question: ")
    all_responses = ["Yes, definitely!", "As I see it, yes.", "Ask again later.", "Cannot predict now",
                     "Don't count on it.", "Very doubtful"]
    random_response = random.choice(all_responses)
    return random_response


print(shake_eight_ball())


print("===Tuples===")
# link:data-structures-labs.html#follow_along_2
print("Follow Along")
vowels = ("a", "e", "i", "o", "u")
print(len(vowels))
print(vowels[2])
print(vowels[0:4])
print(vowels[:4])
print(vowels[1::2])
# vowels.append('y')

# link:data-structures-labs.html#gymnast_scores
print("Gymnast Scores")
def gym_scores():
    gymnast_scores = (1, 2, 3, 4, 5)

    print("The lowest possible score is", gymnast_scores[0], "and the highest possible score is", gymnast_scores[-1])
    print("A judge can give a gymnast a score of", random.choice(gymnast_scores))


gym_scores()

'''OR'''

scores = (1, 2, 3, 4, 5)
print("The lowest possible score is", min(scores), ", and the highest possible score is", max(scores))
rnd_score = random.choice(scores)
print("A judge can give a gymnast", scores[rnd_score], "points")

print("===Sets===")
# link:data-structures-labs.html#follow_along_3
print("Follow Along")
set1 = set("aaabcccccdd")
print(set1)
set2 = {"b", "a", "t", "s", "c", "a", "t", "s"}
print(set2)
print(len(set1))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.union(set2))
set1.add("e")
print(set1)
set2.remove("b")
print(set2)

print("Remove Duplicates")
# link:data-structures-labs.html#remove_duplicates
# Remove Duplicates
def remove_duplicates():
    set1 = set(input("Enter an iterable:"))
    print(set1)


# Finding Vowels
def finding_vowels():
    word = input("Enter a word: ").upper()
    vowels = set("AEIOU")
    common = vowels.intersection(word)
    print(len(common) > 0)


remove_duplicates()
finding_vowels()

'''VOWELS'''
prompt = input("Enter a character: ").upper()
vowels = set("AEIOU")
common = vowels.intersection(prompt)
print(len(common) > 0)

print("===Dictionaries===")
# link:data-structures-labs.html#follow_along_4
print("Follow Along")
cool_ranking = {"Chandler": 1, "Monica": 10, "Ross": 5, "Phoebe": 2, "Joey": 3, "Rachel": 4}
print(cool_ranking["Monica"])
cool_ranking["Janice"] = 6
print(cool_ranking)
print(cool_ranking.keys())
print(cool_ranking.items())
cool_ranking["Monica"] = 7
print(cool_ranking)
del cool_ranking["Janice"]
print(cool_ranking)

# link:data-structures-labs.html#polling_friends
print("Polling Friends")
# Polling Friends
def polling_friends():
    fav_animals = {}

    first_friend = input("What is your favorite animal? ")
    second_friend = input("What is your favorite animal? ")

    fav_animals["Emily"] = first_friend
    fav_animals["Elizabeth"] = second_friend
    print(fav_animals)


polling_friends()

# link:data-structures-labs.html#birthday_month
from datetime import datetime
current = datetime.now().strftime('%B')
months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
print(current)
current_month_number = months[current]
print(current_month_number)
user_bday = input("What is your birth month? ")
user_bday_num = months[user_bday]

months_away = (user_bday_num +(12 - current_month_number)) % 12

print(months_away)

'''
OR
'''

# Birthday Month
def birthday_month():
    current = "June"

    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    curr_month_num = months[current]

    birth_month = input("What month were you born? ").title()

    birth_month_num = months[birth_month]

    month_diff = curr_month_num - birth_month_num

    print("Months since your birthday:", month_diff)

    months_away = (birth_month_num + (12 - curr_month_num)) % 12

    print("Months until your birthday:", months_away)


birthday_month()
