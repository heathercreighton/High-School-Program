"""
filename: loops_labs.py
author: Elizabeth Phillips
date: May 9th, 2018
description: All of the labs for loops
"""

import random

print("For Loops")
# link:loops-labs.html#follow_along
print("Follow Along")
#1
for i in [89, 41, 73, 90]:
    print(i)
#2
for i in range(5, 15):
    print(i)
#3
for i in range(100, 200, 10):
    print(i)
#4
for i in range(80, 30, -8):
    print(i)
#5
for i in range(3):
    print("Alright")
#6
for i in range(1, 6):
    print("*"*i)
#7
for i in range(1, 5):
    print(i*i)
#8
even = 0
odd = 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even numbers:", even)
print("Odd numbers:", odd)

# link:loops-labs.html#dice_histogram
print("Dice Histogram")
import matplotlib.pyplot as plt

a = [] # create an empty list
x = random.randint(1, 6)

for roll in range(100):
    a += [x]
    x = random.randint(1, 6)

plt.hist(a)
plt.show()

# link:loops-labs.html#dice_histogram
print("Create a String")
# Create a String
def create_string():
    letters = ['O', 'r', 'a', 'n', 'g', 'e', ' ', 'M', 'e', 't', 'h', 'o', 'd']

    for h in letters:
        print(h, end="")


if __name__ == '__main__':
    create_string()

# Caesar Cipher
def caesar_cipher():
    cipher_key = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w',
                  'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g',
                  'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm'}
    decrypted = ""
    decrypt = input("Enter a phrase: ")

    for j in decrypt:
        if j in cipher_key.keys():
            decrypted += cipher_key[j]
        else:
            decrypted += j
    print(decrypted)


if __name__ == '__main__':
    caesar_cipher()


# Short Hand
def short_hand(short):
    if 'U' in short:
        short = short.replace('U', '')
    if 'and' in short:
        short = short.replace('and', '&')
    if 'to' in short:
        short = short.replace('to', '2')
    if 'you' in short:
        short = short.replace('you', 'U')
    if 'for' in short:
        short = short.replace('for', '4')
    if 'a' in short:
        short = short.replace('a', '')
    if 'A' in short:
        short = short.replace('A', '')
    if 'e' in short:
        short = short.replace('e', '')
    if 'E' in short:
        short = short.replace('E', '')
    if 'i' in short:
        short = short.replace('i', '')
    if 'I' in short:
        short = short.replace('I', '')
    if 'o' in short:
        short = short.replace('o', '')
    if 'O' in short:
        short = short.replace('O', '')
    if 'u' in short:
        short = short.replace('u', '')
    return short


print(short_hand("Look at Uranus through a telescope and there will be some stuff for you to see"))


# Filling Tickets
def fill_tickets():
    guesses = []
    for i in range(5):
        guesses = [int(input("Enter a number: "))]
    return guesses


# Finding Matches
def find_matches(guesses, matches):
    num_matches = 0
    for i in range(len(guesses)):
        if guesses[i] == matches[i]:
            num_matches += 1
    return num_matches



if __name__ == '__main__':
    guesses = fill_tickets()
    print(guesses)

    winners = [1, 2, 3, 4, 5]
    print(find_matches(guesses, winners))

# WHILE LOOP FOLLOW ALONG AND EXERCISES

# Follow-along
# 1
number = 10
while number >= 1:
    print(number)
    number -= 1
# 2
number_guess = int(input("Guess a number greater than zero: "))

while number_guess <= 0:
    number_guess = int(input("Guess a number greater than zero: "))
print("You entered a valid number!")
# 3
first_number = int(input("Guess your first number: "))
second_number = int(input("Guess your second number :"))

while first_number < second_number:
    first_number += 1
    print(first_number)
# 4
response = input("Enter 'Y', 'y', 'yes', 'YES' or 'N', 'n', 'no', 'NO': ")
while response != "Y" and response != "y" and response != "yes" and response != "YES" and response != "N" and \
    response != "n" and response != "no" and response != "NO":
    response = input("Enter 'Y', 'y', 'yes', 'YES' or 'N', 'n', 'no', 'NO': ")
print("Your response was valid!")
# Error handling in a while loop
count = 0
while count < 5:
    try:
        guess = int(input("Take a guess "))
        count = count + 1
    except ValueError as e:
        print("You've run into a", e, "value error. Please input a number.")


# Exercises

# Dice Histogram - While loop style
a = [] # create an empty list
x = random.randint(1, 6)

while x != 4:
    a += [x]
    x = random.randint(1, 6)

plt.hist(a)
plt.show()

# Guessing Game
rand_number = int(input("Choose a number from 1-20: "))
secret_number = random.randint(1, 20)

while rand_number != secret_number:
    rand_number = int(input("Guess again: "))
print("You guessed it! The secret number was:", secret_number)

# Credit Limit
balance = int(input("Enter Account Balance: "))

while balance > 0:
    print("You have", balance, "in your account.")
    spent = int(input("Enter Amount Spent:"))
    balance = balance - spent
print("All out of money!")


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
        second_chunk += pig[vowel_index:len(pig)]
        pig = second_chunk + first_chunk + "ay"
    return pig


if __name__ == '__main__':
    pig_latin_word = pig_latin("chronic")
    print(pig_latin_word)
