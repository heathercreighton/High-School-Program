"""
title: test_file
author: eam3kzn
date: 6/12/18 10:43 AM
"""


# def subtract_total():
# #     total = 10000
# #     my_share = 20000
# #     print(my_share - total)
# # subtract_total()

# # 1
# phrase = "Don't count your chickens before they hatch. "
#
# # 2
# slogan = "For Everything Else, There's MasterCard"
#
# # 3
# combined = phrase + slogan + "."
# print(combined)
#
# # 4
# print(phrase  * 3)
#
# # 5
# print(slogan[6])
#
# # 6
# print(combined[-1])
#
# # 7
# print(phrase[::2])
#
# # 8
# print(phrase[17:25])
#
# # 9
# print(combined[::2])
#
# # 10
# print('m' in 'slogan')
#
# # 11
# print(combined.upper())
#
# # 12
# print(" ".join(combined))
#
# # 13
# print(slogan[::-1])


# # Modify this function to return a list of strings as defined above
# def list_benefits():
#     return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"
#
# # Modify this function to concatenate to each benefit - " is a benefit of functions!"
# def build_sentence(benefit):
#     return benefit + " is a benefit of functions!"
#
# def the_benefits_of_functions():
#     list_of_benefits = list_benefits()
#     for benefit in list_of_benefits:
#         print(build_sentence(benefit))
#
# if __name__ == "__main__":
#   the_benefits_of_functions()
#

#
# def divide_this(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError as e:
#         print(e)
#     else:
#         print("Executing else", result)
#
#
# print(divide_this(10, 10))

# number = -1
# while number < 0:
#   try:
#     number = int(input("Enter a number:"))
#   except ValueError as e:
#     print(e)
# print("thanks for the number")
#
# while True:
#   try:
#     first_number = int(input("Please enter a number:"))
#     break
#   except ValueError as e:
#     print(e)
#
# while True:
#   try:
#     second_number = int(input("Please enter a larger number:"))
#     if second_number > first_number:
#       break
#   except ValueError as e:
#     print(e)
#
# print(list(range(first_number, second_number + 1)))
#
# correct_responses = ['Y', 'y', 'yes', 'YES', 'N', 'n', 'no', 'NO']
# while True:
#   user_response = input("Enter your response:")
#   if user_response in correct_responses:
#     print("thanks for that")
#     break


# import matplotlib.pyplot as plt
# import random
#
# # Dice Histogram - While loop style
# a = [] # create an empty list
# x = -1
#
# while x != 4:
#     x = random.randint(1, 6)
#     a += [x]
#
# print(a)
#
# plt.hist(a)
# plt.show()
#
# # Guessing Game
# secret_number = random.randint(1, 20)
# print(secret_number)
# rand_number = int(input("Choose a number from 1-20: "))
#
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
#
# print("All out of money!")

# x = 5
# y = 8
#
# print("x == y:", x == y)
# print("x != y:", x != y)
# print("x < y:", x < y)
# print("x > y:", x > y)
# print("x <= y:", x <= y)
# print("x >= y:", x >= y)



# def adjust_balance(account_total, withdrawal):
#
#     try:
#         new_total = account_total - withdrawal
#         if new_total < 0:
#             raise ArithmeticError
#         else:
#             return new_total
#     except ArithmeticError as e:
#         print(f"Withdrawal would have resulted in negative balance {new_total}.  Withdrawal {withdrawal} rejected")
#         return account_total
#
#
# if __name__ == "__main__":
#     account_balance = int(input("Enter your account balance:  "))
#
#     while account_balance > 0:
#         withdrawal = int(input("Enter amount to be withdrawn:  "))
#         account_balance = adjust_balance(account_balance, withdrawal)
#         print(f"Account balance:  {account_balance}")
#     print("Out of money!")


# def check_bal(money):
#     if money == 0:
#         print("All out of money!")
#     elif money > 0:
#         print(f"Current balance: ${money}")
#     elif money < 0:
#         raise RuntimeError("Negative monies!")
#     else:
#         raise Exception("Something went wrong!")
#
# while True:
#     try:
#         balance = int(input("Enter beginning balance: "))
#         check_bal(balance)
#         break
#     except ValueError as e:
#         print(e)
#
# while True:
#     try:
#         spend = int(input("How much did you spend? "))
#         if spend < 0:
#             print("Thanks for the deposit!")
#         balance -= spend
#         check_bal(balance)
#     except ValueError as e:
#         print(e)

# # Pig Latin
# def pig_latin(pig):
#     if not set('aeiouAEIOU').intersection(pig):
#         pig += "ay"
#     elif set('aeiouAEIOU').intersection(pig[0]):
#         pig += "yay"
#     else:
#         vowel_index = 0
#         first_chunk = ""
#         second_chunk = ""
#         while not set('aeiouAEIOU').intersection(pig[vowel_index]):
#             first_chunk += pig[vowel_index]
#             vowel_index += 1
#         second_chunk += pig[vowel_index:len(pig)]
#         pig = second_chunk + first_chunk + "ay"
#     return pig
#
#
# if __name__ == '__main__':
#     pig_latin_word = pig_latin("chronic")
#     print(pig_latin_word)

# # Is this a letter?
# letter = input("Enter a character: ")
#
# alphabet = "qwertyuiopasdfghjklzxcvbnm"
#
# print(letter in alphabet)
# #
#
#
# def this_thing(test_two):
#     print("Testing1")
#     return test_two
#
# print(this_thing("Testing2"))







# secret_num = 10
# guess = int(input("Enter a secret number: "))
#
# if guess == secret_num:
#     print("Yay! You won!")
# elif guess > secret_num:
#     print("Too high!")
# else:
#     print("You're just wrong.")
#

from Unit_05_Functions_Exercises.my_imports import *


if __name__ == '__main__':
    print(age_calculator(2018, 1950))








