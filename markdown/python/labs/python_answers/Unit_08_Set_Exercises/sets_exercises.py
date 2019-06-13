"""
title: sets_exercises
author: eam3kzn
date: 6/11/18 3:21 PM
"""


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