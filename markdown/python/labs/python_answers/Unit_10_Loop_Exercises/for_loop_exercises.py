"""
title: for_loop_exercises
author: eam3kzn
date: 6/11/18 3:51 PM
"""

# import matplotlib.pyplot as plt
# import random
#
# # import sandbox
# #
# # print(sandbox.divide_this(20, 10))
#
# # Follow-alongs
# # 1
# for i in [89, 41, 73, 90]:
#     print(i)
# # 2
# for a in range(5, 15):
#     print(a)
# # 3
# for b in range(100, 201, 10):
#     print(b)
# # 4
# for c in range(80, 30, -8):
#     print(c)
# # 5
# for d in range(3):
#     print("alright")
# # 6
# for e in range(1, 6):
#     print('*' * e)
# # 7
# for f in range(1, 5):
#     print(f ** 2)
# # 8
# even = 0
# odd = 0
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for g in numbers:
#     if g % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print("Even numbers: ", even)
# print("Odd numbers: ", odd)
# # 9
# a = []  # create an empty list
# x = random.randint(1, 6)
#
# for roll in range(100):
#     a += [x]
#     x = random.randint(1, 6)
#
# plt.hist(a)
# plt.show()

# Exercises


# Create a String
def create_string():
    letters = ['O', 'r', 'a', 'n', 'g', 'e', ' ', 'M', 'e', 't', 'h', 'o', 'd']

    for h in letters:
        print(h, end="")


if __name__ == '__main__':
    print("create_string() output: ", end="")
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
    print("Decrypted Caesar Cipher: ", decrypted)


if __name__ == '__main__':
    print("\n")
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


# Filling Tickets
def fill_tickets():
    guesses = []
    for i in range(5):
        guesses += [int(input("Enter a number: "))]
    return guesses


# Finding Matches
def find_matches(ticket, matches):
    num_matches = 0
    for i in range(len(ticket)):
        if ticket[i] == matches[i]:
            num_matches += 1
    return num_matches


if __name__ == '__main__':
    print("short_hand() return: ",
          short_hand("Look at Uranus through a telescope and there will be some stuff for you to see"))
    guesses = fill_tickets()
    print("Guesses: ", guesses)
    winners = [1, 2, 3, 4, 5]
    print("find_matches() return: ", find_matches(guesses, winners))
