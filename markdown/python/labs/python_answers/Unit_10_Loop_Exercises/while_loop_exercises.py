"""
title: while_loop_exercises
author: eam3kzn
date: 6/11/18 3:51 PM
"""

# import matplotlib.pyplot as plt
# import random
#
# # Follow-along
# # 1
# number = 10
# while number >= 1:
#     print(number)
#     number -= 1
# # 2
# number_guess = int(input("Guess a number greater than zero: "))
#
# while number_guess <= 0:
#     number_guess = int(input("Guess a number greater than zero: "))
# print("You entered a valid number!")
# # 3
# first_number = int(input("Guess your first number: "))
# second_number = int(input("Guess your second number :"))
#
# while first_number < second_number:
#     first_number += 1
#     print(first_number)
# # 4
# response = input("Enter 'Y', 'y', 'yes', 'YES' or 'N', 'n', 'no', 'NO': ")
# while response != "Y" and response != "y" and response != "yes" and response != "YES" and response != "N" and \
#     response != "n" and response != "no" and response != "NO":
#     response = input("Enter 'Y', 'y', 'yes', 'YES' or 'N', 'n', 'no', 'NO': ")
# print("Your response was valid!")
# # Error handling in a while loop
# count = 0
# while count < 5:
#     try:
#         guess = int(input("Take a guess "))
#     except ValueError as e:
#         print("You've run into a", e, "value error. Please input a number.")
#     else:
#         count += 1
#     finally:
#         print("THis is the finally")

# Exercises

# count = 0
# while count < 5:
#     try:
#         guess = int(input("Take a guess "))
#     except ValueError as e:
#         print(e)
#     else:
#         count = count + 1

# import matplotlib.pyplot as plt
# import random
# # Dice Histogram - While loop style
# x = random.randint(1, 6)
# a = [x]
#
# while x != 4:
#     a += [x]
#     x = random.randint(1, 6)
#
# plt.hist(a)
# plt.show()

# # Guessing Game
# import random
# rand_number = int(input("Choose a number from 1-20: "))
# secret_number = random.randint(1, 20)
#
# while rand_number != secret_number:
#     rand_number = int(input("Guess again: "))
# print("You guessed it! The secret number was:", secret_number)
#

# # Credit Limit
# balance = int(input("Enter Account Balance: "))
#
# while balance > 0:
#     print("You have", balance, "in your account.")
#     spent = int(input("Enter Amount Spent:"))
#     balance = balance - spent
# print("All out of money!")
#
# Pig Latin


def pig_latin(pig):
    if not set('aeiouAEIOU').intersection(pig):
        pig += "ay"
    elif set('aeiouAEIOU').intersection(pig[0]):
        pig += "yay"
    else:
        vowel_index = 0
        first_chunk = ""
        second_chunk = ""
        while not set('aeiouAEIOU').intersection(pig[vowel_index]):
            first_chunk += pig[vowel_index]
            vowel_index += 1
        second_chunk += pig[vowel_index:]
        pig = second_chunk + first_chunk + "ay"
    return pig


if __name__ == '__main__':
    pig_latin_word = pig_latin("chronic")
    print(pig_latin_word)
