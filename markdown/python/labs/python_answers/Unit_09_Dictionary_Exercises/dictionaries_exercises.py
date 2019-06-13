"""
title: dictionaries_exercises
author: eam3kzn
date: 6/11/18 3:24 PM
"""


# Polling Friends
def polling_friends():
    fav_animals = {}

    first_friend = input("What is your favorite animal? ")
    second_friend = input("What is your favorite animal? ")

    fav_animals["Emily"] = first_friend
    fav_animals["Elizabeth"] = second_friend
    print(fav_animals)


polling_friends()

# Birthday Month without bonus
def birthday_month(current, birthday):

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

    birth_month_num = months[birthday]

    return abs(curr_month_num - birth_month_num)


print(birthday_month("June", "December"))


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



# # Polling Friends
# fav_animals = {}
# def polling_friends(friend):
#     friends_animal = input(f"{friend}, what is your favorite animal?")
#     fav_animals[friend] = friends_animal
#
#     # first_friend = input("What is your favorite animal? ")
#     # second_friend = input("What is your favorite animal? ")
#
#     fav_animals["Emily"] = first_friend
#     fav_animals["Elizabeth"] = second_friend
#     print(fav_animals)
#
#
# polling_friends("Emily")